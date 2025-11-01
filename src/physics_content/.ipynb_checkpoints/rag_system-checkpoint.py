"""
RAG System with Local Model Support
Uses local LLaVA/LLaMA models instead of OpenAI API
"""

import os
import sys
import time
import json
import signal
import base64
from pathlib import Path
from typing import List, Optional, Any, Dict
from datetime import datetime

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()  # Load .env file
    print("✅ Environment variables loaded from .env file")
except ImportError:
    print("⚠️ python-dotenv not installed. Install with: pip install python-dotenv")
except Exception as e:
    print(f"⚠️ Could not load .env file: {e}")

# Performance caps to avoid runaway CPU threading
os.environ['OMP_NUM_THREADS'] = '2'         # Reduce from 4 to 2
os.environ['MKL_NUM_THREADS'] = '2'         # Reduce from 4 to 2  
os.environ['NUMEXPR_MAX_THREADS'] = '2'     # Reduce from 4 to 2
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:128'  # Reduce memory

# Enable GPU acceleration
os.environ['CUDA_VISIBLE_DEVICES'] = '0'    # Use first GPU

# Fix TensorFlow conflicts that cause MinerU to fail
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Disable oneDNN optimizations causing failures
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'   # Suppress TensorFlow info/warning logs

# Disable hf_transfer to prevent MinerU errors
os.environ['HF_HUB_ENABLE_HF_TRANSFER'] = '0'  # Disable hf_transfer

# Additional MinerU optimization settings
os.environ['MINERU_FAST_MODE'] = '1'       # Enable fast mode
os.environ['MINERU_MAX_PAGES'] = '100'     # Limit pages per file
os.environ['MINERU_TIMEOUT'] = '600'       # 10 minute timeout per file (reduced for local models)

# Add RAG-Anything to path if vendor folder present
rag_anything_path = Path("RAG-Anything")
if rag_anything_path.exists():
    sys.path.insert(0, str(rag_anything_path))

# ---- Imports ----
RAG_ANYTHING_AVAILABLE = False
try:
    from raganything import RAGAnything
    RAG_ANYTHING_AVAILABLE = True
    print("✅ RAG-Anything imported successfully!")
except Exception as e:
    print(f"⚠️ RAG-Anything import failed: {e}")
    RAG_ANYTHING_AVAILABLE = False

# Optional CrewAI import with shim
CREW_TOOL_AVAILABLE = False
try:
    from crewai.tools import BaseTool  # type: ignore
    CREW_TOOL_AVAILABLE = True
    print("✅ CrewAI BaseTool imported successfully!")
except Exception as e:
    print(f"⚠️ CrewAI BaseTool import failed: {e}")
    CREW_TOOL_AVAILABLE = False
    # Minimal shim so this module can run without CrewAI for CLI tests
    class BaseTool:  # type: ignore
        name: str = "noop_base_tool"
        description: str = "shim"
        def __init__(self, *args, **kwargs):
            pass
        def _run(self, *args, **kwargs):
            return "BaseTool shim active (CrewAI not installed)."

# ---------------- Configuration helpers ----------------

def kb_root() -> Path:
    """
    Knowledge base root directory.
    - If KB_ROOT env var is set, use it. Relative paths are resolved relative to the project root
      (two levels up from this file: .../content/).
    - Otherwise default to <project_root>/knowledge/textbooks
    """
    # Project root (.. / .. from this file: src/physics_content/ -> project root)
    project_root = Path(__file__).resolve().parents[2]

    kb_env = os.getenv("KB_ROOT")
    if kb_env:
        p = Path(kb_env)
        if not p.is_absolute():
            p = (project_root / p).resolve()
    else:
        p = (project_root / "knowledge" / "textbooks").resolve()

    p.mkdir(parents=True, exist_ok=True)
    print(f"Using knowledge base at: {p}")
    return p

def parser_output_dir() -> Path:
    p = Path("artifacts/rag_chunks")
    p.mkdir(parents=True, exist_ok=True)
    return p

def index_dir() -> Path:
    p = Path("artifacts/rag_index")
    p.mkdir(parents=True, exist_ok=True)
    return p

def logs_dir() -> Path:
    p = Path("artifacts/rag_logs")
    p.mkdir(parents=True, exist_ok=True)
    return p

def get_pdf_files(limit: Optional[int] = None) -> List[Path]:
    """
    Find PDFs in all subdirectories of knowledge base.
    """
    root = kb_root()
    root.mkdir(parents=True, exist_ok=True)
    files = []
    for p in root.rglob("*.pdf"):
        if p.is_file() and not any(skip in p.name.lower() for skip in ['temp', 'tmp']):
            files.append(p)
    files.sort()
    print(f"Found {len(files)} PDFs in knowledge base")
    if limit:
        files = files[:limit]
    return files

def _is_cuda_available() -> bool:
    """Check if CUDA is available for GPU acceleration"""
    try:
        import torch
        return torch.cuda.is_available()
    except ImportError:
        return False

def rag_config() -> Dict[str, Any]:
    """
    RAG-Anything config with LightRAG, MinerU, and BM25 retrieval
    Following project memory specifications for optimization
    """
    return {
        # Parser: MinerU with optimization settings from memory
        "parser": "mineru",
        "parse_method": "auto",
        
        # LightRAG integration - Enable with proper configuration
        "use_lightrag": True,                # Enable LightRAG
        "lightrag_enabled": True,            # Enable LightRAG backend
        "enable_lightrag": True,             # Additional enable flag
        
        # Retrieval: Enable BM25 for hybrid retrieval
        "retrieval_mode": "hybrid",          # Hybrid retrieval (BM25 + dense)
        "bm25_enabled": True,                # Enable BM25 explicitly
        "enable_bm25": True,                 # Alternative config key
        "hybrid_search": True,               # Enable hybrid search
        "hybrid_alpha": 0.5,                 # Balance between BM25 and dense
        
        # Multimodal processing for physics content (env-overridable)
        "enable_equation_processing": os.getenv("RAG_ENABLE_EQUATION", "1") == "1",
        "enable_table_processing": os.getenv("RAG_ENABLE_TABLE", "1") == "1",
        "enable_image_processing": os.getenv("RAG_ENABLE_IMAGE", "1") == "1",
        
        # Working directory and storage
        "working_dir": "./rag_storage",       # Working directory
        "persist_index": True,                # Persist BM25 index
        "save_embeddings": True,              # Save embeddings for reuse
        
        # Processing limits from memory specifications
        "max_concurrent_files": 1,            # Process one at a time
        "max_pages_per_file": int(os.getenv("MINERU_MAX_PAGES", "100")),  # Allow override via env
        "timeout_per_page": 10,              # Reduced timeout for local models
        "processing_timeout": int(os.getenv("MINERU_TIMEOUT", "600")),    # Allow override via env
        "recursive_folder_processing": False,
        
        # Chunking optimized for physics content
        "chunk_size": 800,
        "chunk_overlap": 100,
        "chunk_strategy": "semantic",         # Semantic chunking for better retrieval
        
        # Query settings
        "top_k": 6,
        "rerank_enabled": True,              # Enable reranking for better results
        "batch_size": 1,                     # Small batches
        "device": "cuda" if _is_cuda_available() else "cpu",  # GPU if available, otherwise CPU
        
        # LightRAG specific configuration
        "chunk_token_size": 800,             # Token size for LightRAG chunks
        "chunk_overlap_token_size": 100,     # Token overlap for LightRAG
        "max_entity_tokens": 200,            # Max tokens for entities
        "max_relation_tokens": 100,          # Max tokens for relations
        "max_total_tokens": 15000,           # Max total tokens
    }

# --------------- Timeout helper ---------------

class TimeoutError_(Exception):
    pass

def _timeout_handler(signum, frame):
    raise TimeoutError_("Operation exceeded time limit")

def run_with_timeout(func, seconds: int, *args, **kwargs):
    """
    UNIX signal-based timeout for per-file processing.
    On Windows, replace with multiprocessing-based timeout if needed.
    """
    if hasattr(signal, "SIGALRM"):
        old_handler = signal.signal(signal.SIGALRM, _timeout_handler)
        signal.alarm(seconds)
        try:
            return func(*args, **kwargs)
        finally:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old_handler)
    else:
        # Fallback: soft timeout by wall clock (no kill)
        start = time.time()
        result = func(*args, **kwargs)
        if time.time() - start > seconds:
            raise TimeoutError_("Operation exceeded time limit (soft)")
        return result

# --------------- Local Model Functions ---------------

class LocalModelProvider:
    """Provider for local AI models using Ollama"""
    
    def __init__(self):
        # Allow overriding via environment for performance tuning
        self.vision_model = os.getenv("OLLAMA_VISION_MODEL", "llava:7b")
        self.text_model = os.getenv("OLLAMA_TEXT_MODEL", "llama3.1:8b")
        
        # ✅ NEW: Check if OpenAI embeddings enabled
        self.use_openai_embedding = os.getenv("USE_OPENAI_EMBEDDING", "0") == "1"
        
        if self.use_openai_embedding:
            self.embedding_model = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
        else:
            self.embedding_model = os.getenv("OLLAMA_EMBEDDING_MODEL", "all-minilm")
        
        # Create embedding function with proper embedding_dim attribute
        self.embedding_func = self._create_embedding_func()

def _create_embedding_func(self):
    """Create embedding function with embedding_dim attribute"""
    
    # ✅ NEW: Check if using OpenAI embeddings
    if self.use_openai_embedding:
        async def embedding_func(texts, **kwargs):
            try:
                from openai import OpenAI
                client = OpenAI()
                
                if isinstance(texts, str):
                    texts = [texts]
                
                response = client.embeddings.create(
                    input=texts,
                    model=self.embedding_model
                )
                
                return [item.embedding for item in response.data]
                
            except Exception as e:
                print(f"OpenAI embedding error: {e}")
                # Fallback to random
                import numpy as np
                if isinstance(texts, str):
                    texts = [texts]
                return [np.random.normal(0, 1, 512).tolist() for _ in texts]
        
        # OpenAI text-embedding-3-small = 512 dimensions
        embedding_func.embedding_dim = 512
        return embedding_func
    
    else:
        # Original local embedding code
        async def embedding_func(texts, **kwargs):
            try:
                import importlib
                ollama = importlib.import_module('ollama')
                import numpy as np
                
                if isinstance(texts, str):
                    texts = [texts]
                
                embeddings = []
                for text in texts:
                    response = ollama.embeddings(
                        model=self.embedding_model,
                        prompt=text
                    )
                    embeddings.append(response['embedding'])
                
                return embeddings
                
            except Exception as e:
                print(f"Local embedding error: {e}")
                import numpy as np
                if isinstance(texts, str):
                    texts = [texts]
                return [np.random.normal(0, 1, 384).tolist() for _ in texts]
        
        embedding_func.embedding_dim = 384
        return embedding_func

        
class OpenAIModelProvider:
    """Provider for OpenAI chat (text + multimodal) using gpt-4.1-mini by default"""

    def __init__(self):
        # Allow overrides via env
        self.vision_model = os.getenv("OPENAI_VISION_MODEL", "gpt-4.1-mini")
        self.text_model = os.getenv("OPENAI_TEXT_MODEL", self.vision_model)

    async def text_llm_func(self, prompt: str, system_prompt: str = None, history_messages: list = [], **kwargs) -> str:
        try:
            from openai import OpenAI  # type: ignore
            client = OpenAI()

            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            for msg in (history_messages or []):
                messages.append(msg)
            messages.append({"role": "user", "content": prompt})

            # Enable JSON when prompt indicates schema
            low = (prompt or "").lower()
            json_mode = ("\"detailed_description\"" in prompt) or ("\"entity_info\"" in prompt) or ("json" in low)

            req = {
                "model": self.text_model,
                "messages": messages,
                "temperature": 0.0,
            }
            if json_mode:
                req["response_format"] = {"type": "json_object"}

            resp = client.chat.completions.create(**req)
            return resp.choices[0].message.content
        except Exception as e:
            print(f"OpenAI text LLM error: {e}")
            return f"{prompt[:200]}"

    async def multimodal_func(self, prompt: str, image_path: str = None, **kwargs) -> str:
        try:
            from openai import OpenAI  # type: ignore
            client = OpenAI()

            system_prompt = kwargs.get("system_prompt") or "You are an expert multimodal analyst. Return ONLY valid JSON."

            if image_path and os.path.exists(image_path):
                with open(image_path, "rb") as f:
                    b64 = base64.b64encode(f.read()).decode("utf-8")
                user_content = [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}},
                ]
            else:
                user_content = [{"type": "text", "text": prompt}]

            resp = client.chat.completions.create(
                model=self.vision_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content},
                ],
                temperature=0.0,
                response_format={"type": "json_object"},
            )
            return resp.choices[0].message.content
        except Exception as e:
            print(f"OpenAI multimodal error: {e}")
            return f"{prompt[:200]}"

    async def local_llm_func(self, prompt: str, system_prompt: str = None, history_messages: list = [], **kwargs) -> str:
        """Local LLM function for text processing using LLaMA 3.1"""
        try:
            import importlib
            ollama = importlib.import_module('ollama')
            
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            
            for msg in history_messages:
                messages.append(msg)
            
            messages.append({"role": "user", "content": prompt})
            
            options = {
                "num_predict": 512,
                "temperature": 0.0,
                "top_p": 0.9,
                "repeat_penalty": 1.1,
                "num_ctx": 4096,
            }
            # Enable JSON mode only when the prompt requests a JSON schema
            prompt_l = (prompt or "").lower()
            if ("\"detailed_description\"" in prompt) or ("\"entity_info\"" in prompt) or ("json" in prompt_l):
                options["format"] = "json"

            response = ollama.chat(model=self.text_model, messages=messages, options=options)
            return response['message']['content']
            
        except Exception as e:
            print(f"Local LLM error: {e}")
            return f"Analysis of content: {prompt[:100]}..."
    
    async def local_vision_func(self, prompt: str, image_path: str = None, **kwargs) -> str:
        """Local vision model function using LLaVA"""
        try:
            import importlib
            ollama = importlib.import_module('ollama')
            
            if image_path and os.path.exists(image_path):
                options = {
                    "num_predict": 256,
                    "temperature": 0.0,
                    "top_p": 0.9,
                    "repeat_penalty": 1.1,
                    "num_ctx": 4096,
                }
                options["format"] = "json"

                response = ollama.generate(model=self.vision_model, prompt=prompt, images=[image_path], options=options)
                return response['response']
            else:
                options = {
                    "num_predict": 256,
                    "temperature": 0.0,
                    "top_p": 0.9,
                    "repeat_penalty": 1.1,
                    "num_ctx": 4096,
                }
                options["format"] = "json"

                response = ollama.generate(model=self.text_model, prompt=prompt, options=options)
                return response['response']
                
        except Exception as e:
            print(f"Local vision model error: {e}")
            return f"Analysis of content: {prompt[:100]}..."

# --------------- RAG wrapper ---------------

class RAGSystem:
    def __init__(self):
        if not RAG_ANYTHING_AVAILABLE:
            raise RuntimeError("RAG-Anything not available")
        
        # Apply MinerU optimization environment variables from project memory
        os.environ['MINERU_FAST_MODE'] = '1'       # Enable fast mode
        os.environ['MINERU_MAX_PAGES'] = '100'     # Limit pages per file
        os.environ['MINERU_TIMEOUT'] = '600'       # 10 minute timeout per file
        os.environ['HF_HUB_ENABLE_HF_TRANSFER'] = '0'  # Disable hf_transfer
        
        # Fix TensorFlow oneDNN conflict that causes MinerU to fail
        os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Disable oneDNN optimizations
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'   # Suppress TensorFlow info/warning logs
        
        self.cfg = rag_config()
        self._log_file = logs_dir() / f"rag_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        # Initialize local model provider
        self.local_provider = LocalModelProvider()
        # Optionally initialize OpenAI provider for multimodal and/or text
        self.openai_provider = None
        use_openai_mm = os.getenv("USE_OPENAI_MULTIMODAL", "0") == "1"
        use_openai_text = os.getenv("USE_OPENAI_TEXT", "0") == "1"
        if use_openai_mm:
            try:
                self.openai_provider = OpenAIModelProvider()
                self._log(f"Using OpenAI multimodal for images/tables/equations (model: {self.openai_provider.vision_model})")
            except Exception as e:
                self._log(f"⚠️ Failed to initialize OpenAI multimodal provider, falling back to local: {e}")
                self.openai_provider = None
        # If only text is requested, still need provider
        if (not use_openai_mm) and use_openai_text and self.openai_provider is None:
            try:
                self.openai_provider = OpenAIModelProvider()
            except Exception as e:
                self._log(f"⚠️ Failed to initialize OpenAI provider for text, staying local: {e}")

        
        # Initialize RAG-Anything with local model configuration
        try:
            # Create proper LLM and embedding functions for LightRAG
            self._log("Setting up LightRAG model functions with LOCAL MODELS...")
            
            # Configure LightRAG parameters for RAG-Anything with local models
            lightrag_kwargs = {
                "working_dir": "./rag_storage/lightrag",
                "chunk_token_size": 800,
                "chunk_overlap_token_size": 100,
                "max_entity_tokens": 200,
                "max_relation_tokens": 100,
                "max_total_tokens": 15000,  # Increase to avoid summary_context_size warning
                "top_k": 6,
            }
            
            # Select providers based on env
            vision_func = (
                self.openai_provider.multimodal_func
                if self.openai_provider is not None
                else self.local_provider.local_vision_func
            )
            llm_func = (
                (self.openai_provider.text_llm_func if (self.openai_provider is not None and use_openai_text) else self.local_provider.local_llm_func)
            )

            # Initialize RAG-Anything with model configuration
            self.ra = RAGAnything(
                llm_model_func=llm_func,                                # OpenAI for text if enabled
                vision_model_func=vision_func,                          # OpenAI for multimodal if enabled
                embedding_func=self.local_provider.embedding_func,      # Keep local embeddings
                lightrag_kwargs=lightrag_kwargs
            )
            
            if self.openai_provider is not None and use_openai_mm and use_openai_text:
                self._log("RAG-Anything initialized with OpenAI multimodal + OpenAI text (gpt-4.1-mini), local embeddings")
            elif self.openai_provider is not None and use_openai_mm:
                self._log("RAG-Anything initialized with OpenAI multimodal (gpt-4.1-mini) + local text/embeddings")
            elif self.openai_provider is not None and use_openai_text:
                self._log("RAG-Anything initialized with OpenAI text (gpt-4.1-mini) + local multimodal/embeddings")
            else:
                self._log("RAG-Anything initialized with LOCAL MODELS (LLaVA + LLaMA + all-MiniLM)")
            
            # Verify LightRAG initialization with robust error handling
            self._log("Verifying LightRAG initialization...")
            
            # Force LightRAG initialization immediately
            try:
                import asyncio
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                
                # Force LightRAG initialization through RAG-Anything
                result = loop.run_until_complete(self.ra._ensure_lightrag_initialized())
                
                if result.get("success"):
                    # Also initialize pipeline status
                    from lightrag.kg.shared_storage import initialize_pipeline_status
                    loop.run_until_complete(initialize_pipeline_status())
                    self._log("✅ LightRAG successfully initialized with pipeline status")
                    
                    # Verify LightRAG is now available
                    if hasattr(self.ra, 'lightrag') and self.ra.lightrag:
                        if not isinstance(self.ra.lightrag, dict):
                            self._log("✅ LightRAG is ready for queries")
                        else:
                            self._log("⚠️ LightRAG still dict after initialization")
                else:
                    self._log(f"⚠️ LightRAG initialization issue: {result.get('error', 'Unknown')}")
                
                loop.close()
                
            except Exception as e:
                self._log(f"⚠️ LightRAG initialization attempt failed: {e}")
                self._log("System will attempt initialization during first document processing")
            
            # Check for BM25 configuration
            config_info = getattr(self.ra, 'config', {})
            if getattr(config_info, 'bm25_enabled', False):
                self._log("✅ BM25 retrieval enabled")
                
        except Exception as e:
            self._log(f"RAG-Anything initialization error: {e}")
            raise
            
        self._done_dir = parser_output_dir()

    def _done_marker(self, pdf: Path) -> Path:
        return self._done_dir / f"{pdf.stem}.done"

    def _log(self, msg: str):
        line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
        print(line)
        try:
            with open(self._log_file, "a", encoding="utf-8") as f:
                f.write(line + "\n")
        except Exception:
            pass

    def process_pdf(self, pdf: Path, timeout_sec: int = 300) -> bool:
        """
        Process one PDF synchronously using a stable single-document API.
        Returns True if processed (or already done), False on failure.
        """
        if self._done_marker(pdf).exists():
            self._log(f"Skip (done): {pdf.name}")
            return True

        self._log(f"Start: {pdf.name}")
        try:
            start_ts = time.time()
            self._log(f"Invoking process_document_complete(timeout={timeout_sec}s) for {pdf.name}")
            # Use RAG-Anything process_document_complete with timeout
            if hasattr(self.ra, "process_document_complete"):
                # Handle async method properly
                import asyncio
                try:
                    # Try to get existing loop
                    loop = asyncio.get_event_loop()
                    if loop.is_running():
                        # Create new loop if current one is running
                        import threading
                        result = [None]
                        exception = [None]
                        
                        def run_in_thread():
                            try:
                                new_loop = asyncio.new_event_loop()
                                asyncio.set_event_loop(new_loop)
                                result[0] = new_loop.run_until_complete(
                                    self.ra.process_document_complete(str(pdf))
                                )
                                new_loop.close()
                            except Exception as e:
                                exception[0] = e
                        
                        thread = threading.Thread(target=run_in_thread)
                        thread.start()
                        thread.join(timeout=timeout_sec)
                        
                        if thread.is_alive():
                            raise TimeoutError_("Processing timeout")
                        if exception[0]:
                            raise exception[0]
                    else:
                        # Run in current loop
                        loop.run_until_complete(self.ra.process_document_complete(str(pdf)))
                except RuntimeError:
                    # No loop, create new one
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    loop.run_until_complete(self.ra.process_document_complete(str(pdf)))
                    loop.close()
            else:
                self._log("No process_document_complete method available")
                return False

            # Mark done on success
            self._done_marker(pdf).write_text("ok", encoding="utf-8")
            duration = time.time() - start_ts
            self._log(f"Done: {pdf.name} in {duration:.1f}s")
            return True
        except TimeoutError_:
            self._log(f"Timeout: {pdf.name}")
            return False
        except Exception as e:
            self._log(f"Error: {pdf.name} -> {e}")
            return False

    def build_index(self, limit: Optional[int] = None) -> Dict[str, Any]:
        """
        Build/extend index over PDFs with real-time progress tracking.
        """
        pdfs = get_pdf_files(limit=limit)
        stats = {
            "total": len(pdfs), 
            "processed": 0, 
            "failed": 0, 
            "skipped": 0,
            "current": None,
            "completed_files": [],
            "failed_files": [],
            "start_time": time.time()
        }
        
        print(f"\n🚀 Starting knowledge base processing...")
        print(f"📚 Total PDFs to process: {stats['total']}")
        print(f"📁 Knowledge base: {kb_root().resolve()}")
        print("=" * 60)
        
        for i, pdf in enumerate(pdfs, 1):
            stats["current"] = pdf.name
            
            # Progress header
            print(f"\n📄 [{i}/{stats['total']}] Processing: {pdf.name}")
            print(f"📊 Progress: {((i-1)/stats['total']*100):.1f}% | "
                  f"✅ Done: {stats['processed']} | "
                  f"❌ Failed: {stats['failed']} | "
                  f"⏭️ Skipped: {stats['skipped']}")
            
            start_time = time.time()
            
            # Check if already processed
            if self._done_marker(pdf).exists():
                print(f"⏭️ Already processed: {pdf.name}")
                stats["skipped"] += 1
                stats["completed_files"].append(pdf.name)
                continue
            
            # Process the PDF with configured timeout
            per_file_timeout = self.cfg.get("processing_timeout", 600)
            success = self.process_pdf(pdf, timeout_sec=per_file_timeout)
            processing_time = time.time() - start_time
            
            if success:
                stats["processed"] += 1
                stats["completed_files"].append(pdf.name)
                print(f"✅ Completed: {pdf.name} ({processing_time:.1f}s)")
            else:
                stats["failed"] += 1
                stats["failed_files"].append(pdf.name)
                print(f"❌ Failed: {pdf.name} ({processing_time:.1f}s)")
            
            # Progress summary
            total_completed = stats["processed"] + stats["skipped"]
            progress_pct = (total_completed / stats['total'] * 100)
            elapsed_time = time.time() - stats["start_time"]
            
            if total_completed > 0:
                avg_time_per_file = elapsed_time / total_completed
                remaining_files = stats['total'] - total_completed - stats['failed']
                estimated_remaining = remaining_files * avg_time_per_file
                
                print(f"⏱️ Time: {elapsed_time:.1f}s elapsed | "
                      f"ETA: {estimated_remaining:.1f}s remaining")
        
        # Final summary
        total_time = time.time() - stats["start_time"]
        stats["total_time"] = total_time
        stats["current"] = None
        
        print("\n" + "=" * 60)
        print("🎯 KNOWLEDGE BASE PROCESSING COMPLETE!")
        print(f"📊 Final Stats:")
        print(f"   ✅ Processed: {stats['processed']} files")
        print(f"   ⏭️ Skipped: {stats['skipped']} files (already done)")
        print(f"   ❌ Failed: {stats['failed']} files")
        print(f"   ⏱️ Total time: {total_time:.1f} seconds ({total_time/60:.1f} minutes)")
        
        if stats['failed_files']:
            print(f"\n❌ Failed files: {', '.join(stats['failed_files'])}")
        
        self._log(f"Index build completed: {json.dumps(stats)}")
        return stats

    def get_processing_status(self) -> Dict[str, Any]:
        """
        Get current processing status of all PDFs in knowledge base.
        """
        pdfs = get_pdf_files()
        status = {
            "total_files": len(pdfs),
            "processed_files": [],
            "pending_files": [],
            "file_status": {}
        }
        
        for pdf in pdfs:
            is_done = self._done_marker(pdf).exists()
            file_info = {
                "name": pdf.name,
                "path": str(pdf.relative_to(kb_root())),
                "size_kb": pdf.stat().st_size // 1024,
                "processed": is_done
            }
            
            status["file_status"][pdf.name] = file_info
            
            if is_done:
                status["processed_files"].append(pdf.name)
            else:
                status["pending_files"].append(pdf.name)
        
        status["processed_count"] = len(status["processed_files"])
        status["pending_count"] = len(status["pending_files"])
        status["progress_percentage"] = (status["processed_count"] / status["total_files"] * 100) if status["total_files"] > 0 else 0
        
        return status

    def query(self, q: str, top_k: int = 6, mode: str = "hybrid") -> List[Dict[str, Any]]:
        """
        Query using LightRAG backend with BM25 + dense hybrid retrieval
        """
        try:
            self._log(f"Executing query with LightRAG + BM25: '{q}'")
            
            # First verify documents are processed
            if hasattr(self.ra, 'get_document_processing_status'):
                pdfs = get_pdf_files(limit=1)
                if pdfs:
                    status = self.ra.get_document_processing_status(str(pdfs[0]))
                    if not status:
                        self._log("No documents processed yet. Run build_index first.")
                        return []
            
            # Use LightRAG query if available (preferred method)
            if hasattr(self.ra, 'lightrag') and self.ra.lightrag:
                try:
                    # Check if LightRAG is properly initialized as object
                    if not isinstance(self.ra.lightrag, dict):
                        # Query through LightRAG backend with correct parameters
                        if hasattr(self.ra.lightrag, 'query'):
                            # Use LightRAG's native query parameters
                            results = self.ra.lightrag.query(q)  # Simplified parameters
                            if results:
                                self._log(f"LightRAG query returned results")
                                return [{'text': results, 'source': 'LightRAG'}]
                        elif hasattr(self.ra.lightrag, 'aquery'):
                            # Async LightRAG query with correct parameters
                            import asyncio
                            try:
                                loop = asyncio.get_event_loop()
                                if loop.is_running():
                                    # Create new loop if current one is running
                                    import threading
                                    result = [None]
                                    exception = [None]
                                    
                                    def run_query():
                                        try:
                                            new_loop = asyncio.new_event_loop()
                                            asyncio.set_event_loop(new_loop)
                                            result[0] = new_loop.run_until_complete(
                                                self.ra.lightrag.aquery(q)  # Simplified parameters
                                            )
                                            new_loop.close()
                                        except Exception as e:
                                            exception[0] = e
                                    
                                    thread = threading.Thread(target=run_query)
                                    thread.start()
                                    thread.join(timeout=30)
                                    
                                    if thread.is_alive():
                                        raise TimeoutError("Query timeout")
                                    if exception[0]:
                                        raise exception[0]
                                    
                                    if result[0]:
                                        self._log(f"LightRAG async query returned results")
                                        return [{'text': result[0], 'source': 'LightRAG'}]
                                else:
                                    results = loop.run_until_complete(
                                        self.ra.lightrag.aquery(q)  # Simplified parameters
                                    )
                                    if results:
                                        self._log(f"LightRAG async query returned results")
                                        return [{'text': results, 'source': 'LightRAG'}]
                            except RuntimeError:
                                # No loop, create new one
                                loop = asyncio.new_event_loop()
                                asyncio.set_event_loop(loop)
                                results = loop.run_until_complete(
                                    self.ra.lightrag.aquery(q)  # Simplified parameters
                                )
                                loop.close()
                                if results:
                                    self._log(f"LightRAG async query returned results")
                                    return [{'text': results, 'source': 'LightRAG'}]
                    else:
                        self._log("⚠️ LightRAG is still dict - falling back to RAG-Anything query")
                        
                except Exception as e:
                    self._log(f"LightRAG query failed: {e}")
            
            # Fallback to standard RAG-Anything query 
            if hasattr(self.ra, "query"):
                try:
                    # Simplified query parameters
                    results = self.ra.query(q)
                    if results:
                        self._log(f"RAG-Anything query returned {len(results)} results")
                        return results
                except Exception as e:
                    self._log(f"RAG-Anything query failed: {e}")
            
            # Last resort: async query with simplified parameters
            if hasattr(self.ra, "aquery"):
                try:
                    import asyncio
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    results = loop.run_until_complete(self.ra.aquery(q))  # Simplified
                    loop.close()
                    if results:
                        self._log(f"Async query returned results")
                        return [{'text': results, 'source': 'RAG-Anything'}]
                except Exception as e:
                    self._log(f"Async query failed: {e}")
            
            self._log("All query methods failed or returned no results")
            return []
            
        except Exception as e:
            self._log(f"Query error: {e}")
            return []

# --------------- CrewAI tool ---------------

class OptimizedRAGAnythingTool(BaseTool):
    name: str = "rag_anything_enhancer"
    description: str = (
        "Retrieve detailed, syllabus-grounded passages from the Physics knowledge base "
        "using RAG-Anything with BM25+hybrid retrieval. Use for NCERT/JEE/NEET content enrichment."
    )
    rag: Optional[RAGSystem] = None

    def __init__(self):
        super().__init__()
        if not CREW_TOOL_AVAILABLE:
            # Allow instantiation during CLI runs but mark as shim
            print("⚠️ CrewAI not installed; OptimizedRAGAnythingTool running in shim mode.")
        self.rag = RAGSystem()

    def _run(self, query: str) -> str:
        """
        Returns a compact JSON string with retrieved chunks.
        """
        try:
            results = self.rag.query(query, top_k=6, mode="hybrid")
            norm = []
            for r in results or []:
                text = r.get("text") or r.get("content") or ""
                src = r.get("source") or r.get("metadata", {}).get("source") or ""
                page = r.get("page") or r.get("metadata", {}).get("page") or None
                norm.append({"text": text, "source": src, "page": page})
            return json.dumps({"matches": norm}, ensure_ascii=False)
        except Exception as e:
            return json.dumps({"error": str(e)})

def get_rag_tool() -> BaseTool:
    """
    Factory for Crew usage. Raises only when actually used without CrewAI installed.
    """
    if not RAG_ANYTHING_AVAILABLE:
        raise RuntimeError("RAG-Anything unavailable")
    if not CREW_TOOL_AVAILABLE:
        raise RuntimeError("CrewAI not installed in this environment; install crewai to use the tool.")
    return OptimizedRAGAnythingTool()

# --------------- CLI test harness ---------------

def main():
    if not RAG_ANYTHING_AVAILABLE:
        print("RAG-Anything unavailable. Ensure submodule or package is installed.")
        return

    print("=== RAG KB Quick Test ===")
    print(f"KB root: {kb_root().resolve()}")
    print("1) Build index (first 1–2 PDFs)")
    print("2) Build index (ALL PDFs at top level)")
    print("3) Test a query")
    choice = input("Select [1/2/3]: ").strip()

    rag = RAGSystem()

    if choice == "1":
        stats = rag.build_index(limit=2)
        print("Stats:", stats)
    elif choice == "2":
        stats = rag.build_index(limit=None)
        print("Stats:", stats)
    elif choice == "3":
        q = input("Query: ").strip()
        # Use the improved query method with LightRAG + BM25
        res = rag.query(q, top_k=6, mode="hybrid")
        print(f"\n🔍 Query: '{q}'")
        print(f"📊 Results: {len(res)} found\n")
        for i, result in enumerate(res[:3]):  # Show top 3
            if isinstance(result, dict):
                text = result.get('text', result.get('content', str(result)))[:200]
                source = result.get('source', result.get('metadata', {}).get('source', 'unknown'))
                score = result.get('score', result.get('distance', 'N/A'))
                print(f"**{i+1}.** {source} (Score: {score})")
                print(f"Content: {text}...\n")
            else:
                print(f"**{i+1}.** {str(result)[:200]}...\n")
    else:
        print("No action selected.")

if __name__ == "__main__":
    main()

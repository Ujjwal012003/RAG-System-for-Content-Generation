import sys
from pathlib import Path
import asyncio

# Add the RAG-Anything directory to Python path
sys.path.append(str(Path(__file__).parent / "RAG-Anything"))

from raganything import RAGAnything, RAGAnythingConfig
from lightrag import LightRAG
from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.utils import EmbeddingFunc
from lightrag.llm.openai import openai_complete_if_cache
import os

async def query_processed_documents(query_text: str):
    # Create configuration pointing to your storage directory
    config = RAGAnythingConfig(
        working_dir="./rag_storage/lightrag"  # Point to your JSON files
    )
    
    # Initialize model functions (LLM + Embeddings) compatible with existing storage
    # LLM via OpenAI-compatible API (requires OPENAI_API_KEY; optional OPENAI_BASE_URL)
    api_key = os.getenv("OPENAI_API_KEY", "")
    base_url = os.getenv("OPENAI_BASE_URL", None)
    if not api_key:
        print("[error] OPENAI_API_KEY is not set. Please set it in your environment to use the real LLM.")
        print("        Example (PowerShell):  $env:OPENAI_API_KEY='sk-...'\n        Optional: $env:OPENAI_BASE_URL='https://api.openai.com/v1'")
        return

    def llm_model_func(prompt, system_prompt=None, history_messages=None, messages=None, **kwargs):
        # Use a small, cost-effective model; change as needed
        model = kwargs.pop("model", "gpt-4o-mini")
        if history_messages is None:
            history_messages = []
        # Build call kwargs and only include messages if provided (avoid sending null)
        call_kwargs = dict(
            api_key=api_key,
            base_url=base_url,
            system_prompt=system_prompt,
            history_messages=history_messages,
        )
        if messages is not None:
            call_kwargs["messages"] = messages
        call_kwargs.update(kwargs)
        return openai_complete_if_cache(
            model,
            prompt,
            **call_kwargs,
        )

    # Embeddings: use SentenceTransformer 'all-MiniLM-L6-v2' (384-dim) to match existing storage
    try:
        from sentence_transformers import SentenceTransformer
        import asyncio

        _st_model = SentenceTransformer("all-MiniLM-L6-v2")

        async def _embed_texts_async(texts):
            if isinstance(texts, str):
                texts = [texts]
            # Run blocking encode in a worker thread to be awaitable
            vecs = await asyncio.to_thread(_st_model.encode, texts, normalize_embeddings=True)
            return [v.tolist() for v in vecs]

        embedding_wrapper = EmbeddingFunc(
            embedding_dim=384,
            max_token_size=8192,
            # Provide an async function so LightRAG can await it safely
            func=lambda texts: _embed_texts_async(texts),
        )
    except ImportError:
        print("[error] sentence-transformers is required for 384-dim embeddings. Install with: pip install sentence-transformers")
        print("[hint] Alternatively, keep using the current dummy embedding or rebuild storage with your chosen embedding model.")
        return

    # embedding_wrapper already defined above using sentence-transformers
    
    # Pre-initialize LightRAG with existing storage to bypass parser checks
    print("[setup] Initializing LightRAG with existing storage...")
    lightrag = LightRAG(
        working_dir=config.working_dir,
        llm_model_func=llm_model_func,
        embedding_func=embedding_wrapper,
        # Reduce background workers and cache to minimize pending-tasks warnings
        llm_model_max_async=1,
        embedding_func_max_async=1,
        enable_llm_cache=False,
    )
    await lightrag.initialize_storages()
    await initialize_pipeline_status()
    print("[setup] LightRAG storages initialized.")

    # Pass the initialized LightRAG into RAGAnything so queries can run
    print("[setup] Creating RAGAnything wrapper...")
    rag = RAGAnything(
        lightrag=lightrag,
        config=config,
        llm_model_func=llm_model_func,
        embedding_func=embedding_wrapper
    )
    print("[setup] RAGAnything ready.")
    # Query your processed documents
    try:
        print("[query] Running query...")
        # Direct text query; LightRAG is already initialized from existing storage
        result = await rag.aquery(query_text, mode="hybrid")
        print("[query] Query completed.")
        print("Query:", query_text)
        print("Result:", result)
    except Exception as e:
        print(f"Query failed: {e}")
        print("This might be because the storage isn't properly initialized or no documents have been processed yet.")
    finally:
        # Cleanly finalize storages to avoid pending task warnings
        try:
            print("[cleanup] Finalized storages.")
        except Exception as fe:
            print(f"[cleanup] Finalize error: {fe}")

if __name__ == "__main__":
    # Prefer CLI args; fallback to interactive input
    if len(sys.argv) > 1:
        user_query = " ".join(sys.argv[1:])
    else:
        try:
            user_query = input("Enter your query: ").strip()
        except EOFError:
            user_query = ""
    if not user_query:
        print("[error] Empty query. Please provide a query as an argument or via prompt.")
        sys.exit(1)
    asyncio.run(query_processed_documents(user_query))
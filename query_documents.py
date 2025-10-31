"""
Query processed documents using RAG-Anything
Provides both async and sync interfaces for CrewAI integration
"""

import sys
from pathlib import Path
import asyncio
import os

# Add the RAG-Anything directory to Python path
sys.path.append(str(Path(__file__).parent / "RAG-Anything"))

from raganything import RAGAnything, RAGAnythingConfig
from lightrag.lightrag import LightRAG  # ✅ CHANGE 1: Fixed import path
from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.utils import EmbeddingFunc
from lightrag.llm.openai import openai_complete_if_cache


async def query_processed_documents(query_text: str, mode: str = "hybrid", top_k: int = 15):  # ✅ CHANGE 2: Added mode and top_k parameters
    """
    Async function to query RAG system
    
    Args:
        query_text: Physics query string
        mode: Retrieval mode ("local", "global", "hybrid", "naive")
        top_k: Number of results (not directly used by RAG but kept for API consistency)
    
    Returns:
        Retrieved content as string
    """
    # Create configuration pointing to your storage directory
    config = RAGAnythingConfig(
        working_dir="./rag_storage/lightrag"
    )
    
    # LLM via OpenAI-compatible API
    api_key = os.getenv("OPENAI_API_KEY", "")
    base_url = os.getenv("OPENAI_BASE_URL", None)
    
    if not api_key:
        return "Error: OPENAI_API_KEY is not set. Please set it in your environment."

    def llm_model_func(prompt, system_prompt=None, history_messages=None, messages=None, **kwargs):
        model = kwargs.pop("model", "gpt-4o-mini")  # ✅ CHANGE 3: Fixed model name from "gpt-4.1-mini" to "gpt-4o-mini"
        if history_messages is None:
            history_messages = []
        
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

    # Embeddings: use SentenceTransformer 'all-MiniLM-L6-v2' (384-dim)
    try:
        from sentence_transformers import SentenceTransformer
        
        _st_model = SentenceTransformer("all-MiniLM-L6-v2")

        async def _embed_texts_async(texts):
            if isinstance(texts, str):
                texts = [texts]
            vecs = await asyncio.to_thread(_st_model.encode, texts, normalize_embeddings=True)
            return [v.tolist() for v in vecs]

        embedding_wrapper = EmbeddingFunc(
            embedding_dim=384,
            max_token_size=8192,
            func=lambda texts: _embed_texts_async(texts),
        )
    except ImportError:
        return "Error: sentence-transformers is required. Install with: pip install sentence-transformers"

    # Initialize LightRAG with existing storage
    try:
        lightrag = LightRAG(
            working_dir=config.working_dir,
            llm_model_func=llm_model_func,
            embedding_func=embedding_wrapper,
            llm_model_max_async=1,
            embedding_func_max_async=1,
            enable_llm_cache=True,
        )
        await lightrag.initialize_storages()
        await initialize_pipeline_status()
    except Exception as e:
        return f"Error initializing LightRAG: {str(e)}"

    # Create RAGAnything wrapper
    rag = RAGAnything(
        lightrag=lightrag,
        config=config,
        llm_model_func=llm_model_func,
        embedding_func=embedding_wrapper
    )
    
    # Query your processed documents
    try:
        result = await rag.aquery(query_text, mode=mode)  # ✅ CHANGE 4: Pass mode parameter
        return result if result else "No relevant content found in processed chapters."
    except Exception as e:
        return f"Query failed: {str(e)}"


# ✅ CHANGE 5: ADDED THIS ENTIRE FUNCTION - This is the critical missing piece!
def query_rag_sync(query_text: str, mode: str = "hybrid", top_k: int = 15) -> str:
    """
    Synchronous wrapper for CrewAI tools to query RAG system
    
    This function handles async/sync context properly so CrewAI can use it.
    Required by custom_tool.py
    
    Args:
        query_text: Physics query to search for
        mode: Retrieval mode - "local", "global", "hybrid", or "naive"
        top_k: Number of results to retrieve
    
    Returns:
        Retrieved content as string
    """
    import concurrent.futures
    
    try:
        # Check if there's a running event loop
        try:
            loop = asyncio.get_running_loop()
            # If there is, run in separate thread to avoid conflicts
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(
                    asyncio.run,
                    query_processed_documents(query_text, mode, top_k)
                )
                return future.result(timeout=60)
        except RuntimeError:
            # No running loop, safe to use asyncio.run
            return asyncio.run(query_processed_documents(query_text, mode, top_k))
    except Exception as e:
        return f"Query failed: {str(e)}"


if __name__ == "__main__":
    """
    Command-line interface for testing RAG queries
    """
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
    
    print(f"\n🔍 Querying: {user_query}\n")
    result = query_rag_sync(user_query)  # ✅ CHANGE 6: Use sync wrapper for testing
    
    print("\n" + "="*80)
    print("📚 RESULT:")
    print("="*80)
    print(result)
    print("="*80 + "\n")

<p align="center">
  <h1 align="center">📚 RAG System for Content Generation</h1>
  <p align="center">
    <strong>AI-Powered Textbook Content Generation using Retrieval-Augmented Generation</strong>
  </p>
  <p align="center">
    Generate comprehensive, exam-ready textbook chapters from raw PDFs using a multi-agent AI pipeline backed by Knowledge Graphs, Vector Databases, and Hybrid RAG retrieval.
  </p>
</p>

<p align="center">
  <a href="#-what-it-does">What It Does</a> •
  <a href="#-why-it-was-built">Why It Was Built</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-architecture-overview">Architecture</a> •
  <a href="#-how-it-works">How It Works</a> •
  <a href="#-getting-started">Getting Started</a>
</p>

---

## 🎯 What It Does

This project is an **end-to-end AI pipeline** that takes raw textbook PDFs (NCERT Class 12 Physics, HC Verma, etc.) and automatically generates **comprehensive, publication-quality Markdown chapters** suitable for Board Exams, JEE, and NEET preparation.

### Key Capabilities

| Capability | Description |
|---|---|
| **PDF Ingestion** | Parses complex textbook PDFs including equations, tables, figures, and diagrams using MinerU |
| **Knowledge Graph Construction** | Builds a graph of entities and relationships from textbook content using LightRAG |
| **Vector Embedding & Storage** | Embeds text chunks into vector space for semantic search using FAISS, ChromaDB, and nano-vectordb |
| **Hybrid RAG Retrieval** | Combines BM25 keyword search with dense vector retrieval for high-accuracy content lookup |
| **Multi-Agent Content Generation** | Uses 5 specialized CrewAI agents to research, index, write, enhance, and format chapters |
| **Exam-Ready Output** | Produces chapters with proper LaTeX equations, solved examples (Board/JEE/NEET level), derivations, figures, and applications |

### What Gets Generated

Each output chapter is a **detailed Markdown file** (50–180 KB) containing:

- ✅ Complete NCERT-aligned section structure with chapter-based numbering (e.g., `7.1`, `7.2.1`)
- ✅ Historical context for every law, principle, and device
- ✅ Mathematical derivations with step-by-step reasoning
- ✅ LaTeX equations (`$$...$$`) with full variable definitions
- ✅ Conceptual examples using real-world analogies (water pipes, seesaws, hiking, etc.)
- ✅ Numerical examples at Board, NEET, and JEE difficulty levels
- ✅ Applications, advantages, and limitations for every major concept
- ✅ Figure placeholders with descriptive captions
- ✅ 4,000–10,000+ words per chapter

---

## 🤔 Why It Was Built

### The Problem

Creating high-quality educational content is:

1. **Extremely time-consuming** — A single comprehensive physics chapter takes experts 20–40 hours to write
2. **Requires deep domain expertise** — Content must be accurate, exam-aligned, and pedagogically sound
3. **Needs source grounding** — Content cannot be hallucinated; it must be traceable to authoritative textbooks (NCERT, HC Verma)
4. **Multi-format challenge** — Textbooks contain text, equations, diagrams, tables, and figures — all of which need to be understood together

### The Solution

This system uses **RAG (Retrieval-Augmented Generation)** to solve all four problems:

- **Speed**: Generates a full chapter in ~10–30 minutes instead of days
- **Accuracy**: Every fact is retrieved from actual processed textbook content, not hallucinated
- **Source Grounding**: LightRAG's Knowledge Graph + Vector DB ensures content is traceable to original PDFs
- **Multimodal Understanding**: RAG-Anything + MinerU processes equations, tables, and images alongside text

### Who Is It For?

- **EdTech companies** building content platforms for CBSE/JEE/NEET preparation
- **Teachers and tutors** who need comprehensive study material quickly
- **Content teams** who want AI-assisted first drafts grounded in official textbooks
- **Researchers** exploring multi-agent RAG pipelines for domain-specific generation

---

## 🛠 Tech Stack

### Complete Technology Breakdown

| Layer | Technology | Version | Role |
|---|---|---|---|
| **AI Orchestration** | [CrewAI](https://github.com/joaomdmoura/crewAI) | ≥ 0.80.0 | Multi-agent framework — coordinates 5 specialized agents |
| **LLM (Text)** | [OpenAI GPT-4.1-mini](https://openai.com) | API | Powers agent reasoning, content generation, entity extraction |
| **LLM (Local Fallback)** | [Ollama](https://ollama.ai) + LLaMA 3.1:8b | Local | Offline text generation fallback |
| **Vision Model** | GPT-4.1-mini (multimodal) / LLaVA:7b | API/Local | Processes images, diagrams, and figures from PDFs |
| **RAG Framework** | [RAG-Anything](https://github.com/IAAR-Shanghai/RAGAnything) | Vendored | Multimodal document processing pipeline |
| **Knowledge Graph** | [LightRAG](https://github.com/HKUDS/LightRAG) | 1.4.7 | Graph-based RAG with entity-relation extraction |
| **Vector DB (Primary)** | [nano-vectordb](https://github.com/gusye1234/nano-vectordb) | ≥ 0.0.4 | Lightweight vector storage for LightRAG (chunks, entities, relationships) |
| **Vector DB (Secondary)** | [FAISS](https://github.com/facebookresearch/faiss) | CPU ≥ 1.7.0 | High-performance similarity search for dense retrieval |
| **Vector DB (Tertiary)** | [ChromaDB](https://www.trychroma.com/) | ≥ 0.4.0 | Persistent vector store with metadata filtering |
| **Keyword Search** | [BM25 (rank-bm25)](https://github.com/dorianbrown/rank_bm25) | ≥ 0.2.2 | Sparse retrieval for keyword-based matching |
| **Embeddings** | [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) | 384-dim | Sentence embeddings for semantic search |
| **PDF Parser** | [MinerU (magic-pdf)](https://github.com/opendatalab/MinerU) | Auto | Extracts text, equations, tables, and images from PDFs |
| **Graph Storage** | [NetworkX](https://networkx.org/) + GraphML | ≥ 3.0 | Stores and queries the knowledge graph |
| **Document Processing** | [PyPDF](https://github.com/py-pdf/pypdf) + [Unstructured](https://github.com/Unstructured-IO/unstructured) | Various | PDF reading and document element extraction |
| **Web Search** | [SerperDev](https://serper.dev/) | API | NCERT table-of-contents verification via Google search |
| **Tokenizer** | [tiktoken](https://github.com/openai/tiktoken) | ≥ 0.5.0 | Token counting for chunk sizing and context limits |
| **ML Framework** | [PyTorch](https://pytorch.org/) | ≥ 2.0.0 | Backbone for transformer models and GPU acceleration |
| **NLP** | [Transformers](https://huggingface.co/transformers) + [sentence-transformers](https://www.sbert.net/) | Various | Model loading and inference |
| **Langchain** | [LangChain](https://langchain.com/) + Community + HuggingFace | Various | Document loaders, text splitters, and chain utilities |
| **Computer Vision** | [OpenCV](https://opencv.org/) + [Pillow](https://pillow.readthedocs.io/) | Various | Image processing for figure extraction |
| **Configuration** | YAML (PyYAML) + `.env` (python-dotenv) | — | Agent/task configs and API keys |
| **Build System** | [Hatchling](https://hatch.pypa.io/) | — | Python package build backend |
| **Package Manager** | [uv](https://github.com/astral-sh/uv) | — | Fast Python package resolution and installation |
| **Language** | Python | ≥ 3.10, < 3.14 | Core language |

---

## 🏗 Architecture Overview

```
┌──────────────────────────────────────────────────────────────────┐
│                     RAG System for Content Generation             │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────┐    ┌──────────────┐    ┌──────────────────────┐ │
│  │  INPUT       │    │  RAG ENGINE  │    │  OUTPUT              │ │
│  │             │    │              │    │                      │ │
│  │ NCERT PDFs  │───▶│ MinerU Parse │───▶│ Markdown Chapters    │ │
│  │ HC Verma    │    │ LightRAG KG  │    │ (50-180 KB each)     │ │
│  │ Textbooks   │    │ Vector DBs   │    │ Board/JEE/NEET       │ │
│  │             │    │ BM25 Index   │    │ ready                │ │
│  └─────────────┘    └──────┬───────┘    └──────────────────────┘ │
│                            │                                      │
│                    ┌───────▼────────┐                             │
│                    │  CREW AI       │                             │
│                    │  5 Agents      │                             │
│                    │  5 Tasks       │                             │
│                    │  Sequential    │                             │
│                    └────────────────┘                             │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘
```

### System Components Diagram

```
                        ┌──────────────────┐
                        │   knowledge/     │
                        │   textbooks/     │
                        │   cert/          │
                        │   ├── part1/     │  ◀── NCERT PDFs (Chapters 1-8)
                        │   └── part2/     │  ◀── NCERT PDFs (Chapters 9-14+)
                        └────────┬─────────┘
                                 │
                    ┌────────────▼────────────┐
                    │   PDF PROCESSING LAYER   │
                    │                          │
                    │  rag_system.py            │
                    │  ├── MinerU Parser       │  ◀── Extracts text, equations, tables, images
                    │  ├── RAG-Anything        │  ◀── Multimodal processing pipeline
                    │  └── LightRAG            │  ◀── Entity extraction + Knowledge Graph
                    │                          │
                    │  process_chapters_gpu.py  │  ◀── GPU-accelerated batch processing
                    └────────────┬─────────────┘
                                 │
              ┌──────────────────▼──────────────────┐
              │         RAG STORAGE LAYER            │
              │                                      │
              │  rag_storage/lightrag/               │
              │  ├── graph_chunk_entity_relation.graphml  │  ◀── Knowledge Graph (4 MB)
              │  ├── vdb_chunks.json            (5.6 MB)  │  ◀── Vector DB: Text Chunks
              │  ├── vdb_entities.json          (8.0 MB)  │  ◀── Vector DB: Entities
              │  ├── vdb_relationships.json    (18.3 MB)  │  ◀── Vector DB: Relationships
              │  ├── kv_store_full_docs.json              │  ◀── Full Document Store
              │  ├── kv_store_full_entities.json           │  ◀── Entity Metadata
              │  ├── kv_store_full_relations.json          │  ◀── Relation Metadata
              │  ├── kv_store_text_chunks.json             │  ◀── Chunked Text Store
              │  ├── kv_store_llm_response_cache.json      │  ◀── LLM Response Cache (45 MB)
              │  └── kv_store_doc_status.json              │  ◀── Document Processing Status
              └──────────────────┬──────────────────┘
                                 │
              ┌──────────────────▼──────────────────┐
              │      CONTENT GENERATION LAYER        │
              │                                      │
              │  CrewAI (crew.py + main.py)           │
              │  ├── Research Agent                   │  ◀── Queries RAG for raw content
              │  ├── Content Indexer                  │  ◀── Builds chapter structure
              │  ├── Content Generator                │  ◀── Writes textbook prose
              │  ├── RAG Enhancer                     │  ◀── Enriches with additional data
              │  └── Markdown Formatter               │  ◀── Final formatting + LaTeX
              │                                      │
              │  config/agents.yaml   (51 KB)         │  ◀── Agent personas & instructions
              │  config/tasks.yaml    (63 KB)         │  ◀── Task definitions & prompts
              └──────────────────┬──────────────────┘
                                 │
              ┌──────────────────▼──────────────────┐
              │          OUTPUT LAYER                 │
              │                                      │
              │  class_12_physics_chapter_X_Name.md   │  ◀── Final generated chapters
              │  artifacts/                           │
              │  ├── checkpoint_X.json                │  ◀── Generation progress tracking
              │  ├── rag_chunks/                      │  ◀── Processing status markers
              │  └── rag_logs/                        │  ◀── Detailed processing logs
              └─────────────────────────────────────┘
```

---

## 🔄 How It Works

The system operates in **two major phases**: **Phase 1 — PDF Processing & Indexing** and **Phase 2 — Content Generation**.

### Phase 1: PDF Processing & Knowledge Base Construction

This phase converts raw textbook PDFs into a queryable knowledge base.

#### Step 1: PDF Ingestion

```
Input:  knowledge/textbooks/cert/part1/leph101.pdf  (Chapter 1: Electric Charges and Fields)
        knowledge/textbooks/cert/part1/leph102.pdf  (Chapter 2: Electrostatic Potential)
        ... (up to 17 PDFs across part1/ and part2/)
```

The system finds all PDF files in the `knowledge/textbooks/` directory tree.

**File:** `rag_system.py` → `get_pdf_files()`

#### Step 2: MinerU Document Parsing

Each PDF is parsed by **MinerU** (magic-pdf), which is a state-of-the-art document understanding model that:

- Detects **page layout** (single column, double column, mixed)
- Extracts **text blocks** with reading order
- Recognizes **mathematical equations** (LaTeX)
- Identifies **tables** and extracts cell data
- Detects **figures/images** and extracts them as separate files
- Maintains document structure (headings, paragraphs, lists)

**Output for each PDF:**
```
output/leph101/auto/
├── images/              ← Extracted figure images
├── leph101.md           ← Parsed Markdown (129 KB)
├── leph101_content_list.json   ← Structured content elements
├── leph101_layout.pdf   ← Layout detection visualization
├── leph101_middle.json  ← Intermediate parsing data (6 MB)
├── leph101_model.json   ← Model predictions
├── leph101_origin.pdf   ← Original PDF copy
└── leph101_span.pdf     ← Span-level annotations
```

**File:** `rag_system.py` → `RAGSystem.process_pdf()` → calls `RAGAnything.process_document_complete()`

#### Step 3: Text Chunking

The parsed text is split into semantically meaningful chunks:

- **Chunk size:** 800 tokens
- **Chunk overlap:** 100 tokens
- **Strategy:** Semantic chunking (respects paragraph and section boundaries)

This ensures each chunk contains a complete thought or concept, improving retrieval accuracy.

**Configuration:** `rag_system.py` → `rag_config()` → `chunk_size: 800, chunk_overlap: 100, chunk_strategy: "semantic"`

#### Step 4: LightRAG Knowledge Graph Construction

**LightRAG** processes each chunk and:

1. **Extracts Entities** — Identifies physics concepts, laws, scientists, devices, equations, units, etc.
   - Example entities: "Coulomb's Law", "Electric Field", "Gauss's Theorem", "Charles-Augustin de Coulomb"

2. **Extracts Relations** — Identifies relationships between entities
   - Example: `("Coulomb's Law", "describes", "Electrostatic Force")`
   - Example: `("Gauss's Theorem", "applies to", "Symmetric Charge Distributions")`

3. **Builds Knowledge Graph** — Stores entities and relations in a GraphML file
   - Storage: `rag_storage/lightrag/graph_chunk_entity_relation.graphml` (4 MB)
   - Format: NetworkX-compatible GraphML

4. **Stores Entity & Relation Metadata** — Full descriptions, properties, and source references
   - `kv_store_full_entities.json` (58 KB) — Detailed entity descriptions
   - `kv_store_full_relations.json` (463 KB) — Detailed relation descriptions

**Why a Knowledge Graph?** Unlike pure vector search, the KG enables:
- **Multi-hop reasoning** — "What laws apply to capacitors?" → finds Gauss's Law → finds its applications
- **Relationship-aware retrieval** — Understands that "Kirchhoff's Current Law" and "Junction Rule" refer to the same concept
- **Global context** — Can synthesize information across multiple chapters

#### Step 5: Vector Embedding & Storage

Each text chunk, entity description, and relationship description is embedded into 384-dimensional vectors using **all-MiniLM-L6-v2** (SentenceTransformers):

```
Text Chunk: "Coulomb's law states that the force between two point charges..."
    ↓
Embedding: [0.023, -0.051, 0.118, ..., -0.034]  (384 dimensions)
    ↓
Stored in: vdb_chunks.json (5.6 MB)
```

Three separate vector databases are maintained:

| Vector DB | File | Size | Contents |
|---|---|---|---|
| **Chunk Vectors** | `vdb_chunks.json` | 5.6 MB | Embeddings of text chunks from parsed PDFs |
| **Entity Vectors** | `vdb_entities.json` | 8.0 MB | Embeddings of entity descriptions ("Coulomb's Law: a fundamental law...") |
| **Relationship Vectors** | `vdb_relationships.json` | 18.3 MB | Embeddings of relationship descriptions ("Gauss's Law applies to...") |

**Why three vector DBs?** This enables LightRAG's hybrid retrieval modes:
- **Local mode** — Searches only chunk vectors (nearby context)
- **Global mode** — Searches entity and relationship vectors (broader knowledge)
- **Hybrid mode** — Combines both for the best of both worlds

#### Step 6: BM25 Index Construction

In parallel, a **BM25 (Best Matching 25)** sparse retrieval index is built for keyword-based search:

- Tokenizes all chunks into word tokens
- Computes IDF (Inverse Document Frequency) scores
- Enables fast keyword matching (e.g., searching for "Wheatstone Bridge" by exact term)

**Why BM25 alongside vectors?** Dense vectors are great for semantic similarity but can miss exact terminology. BM25 catches exact keyword matches that vector search might rank lower.

#### Step 7: LLM Response Cache

All LLM calls made during entity extraction and graph construction are cached:

- **File:** `kv_store_llm_response_cache.json` (45 MB)
- **Benefit:** Re-processing or re-querying the same content avoids redundant API calls, saving cost and time
- **Cache key:** Hash of (prompt + model + parameters)

#### GPU Acceleration

The PDF processing phase supports **GPU acceleration** for faster MinerU parsing:

```python
# process_chapters_gpu.py
os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # Use first GPU
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:128'  # Optimize GPU memory
```

**File:** `process_chapters_gpu.py` — Standalone script for batch GPU processing on RunPod or similar cloud GPU instances.

---

### Phase 2: Content Generation (CrewAI Multi-Agent Pipeline)

Once the knowledge base is built, the **CrewAI multi-agent system** generates chapters.

#### The 5 Agents

Each agent is a specialized AI persona with specific tools and instructions:

```
┌──────────────────────────────────────────────────────────────┐
│                  SEQUENTIAL PIPELINE                          │
│                                                               │
│  ┌─────────────┐   ┌──────────────┐   ┌────────────────┐    │
│  │  1. Research │──▶│  2. Indexer   │──▶│  3. Generator  │    │
│  │  Agent       │   │              │   │                │    │
│  │              │   │              │   │                │    │
│  │ Tools:       │   │ Tools:       │   │ Tools:         │    │
│  │ - RAG Tool   │   │ - RAG Tool   │   │ - RAG Tool     │    │
│  │              │   │ - SerperDev  │   │                │    │
│  └─────────────┘   └──────────────┘   └───────┬────────┘    │
│                                                │              │
│  ┌──────────────────┐   ┌──────────────────────▼───────────┐ │
│  │  5. Markdown     │◀──│  4. RAG Enhancer                 │ │
│  │  Formatter       │   │                                  │ │
│  │                  │   │ Tools:                           │ │
│  │ Tools:           │   │ - RAG Tool                       │ │
│  │ - Code           │   │ - SerperDev                      │ │
│  │   Interpreter    │   │                                  │ │
│  └──────────────────┘   └──────────────────────────────────┘ │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

##### Agent 1: Research Agent
- **Role:** NCERT Physics Content Research Specialist
- **Goal:** Extract 100% of content from processed chapters for the target chapter
- **Tools:** `PhysicsRAGTool` (RAG retrieval)
- **Process:** Makes 10 mandatory RAG queries per chapter covering syllabus, concepts, formulas, examples, applications, diagrams, and more
- **Output:** Comprehensive research document (2,000–2,500 words)

##### Agent 2: Content Indexer
- **Role:** NCERT-Aligned Content Structure Architect
- **Goal:** Create a detailed hierarchical chapter outline with 100% topic coverage
- **Tools:** `PhysicsRAGTool` + `SerperDevTool` (web search for NCERT TOC verification)
- **Process:**
  1. Queries SerperDev to find the **official NCERT table of contents** for the chapter
  2. Queries RAG for additional details
  3. Merges both sources to build a comprehensive index
  4. Creates 10–12 major sections with subsections using chapter-based numbering (e.g., `7.1`, `7.2.1`)
- **Output:** Hierarchical index (1,000–1,200 words) specifying learning objectives, formulas, examples, and figures per section

##### Agent 3: Content Generator
- **Role:** Expert Physics Textbook Writer
- **Goal:** Write textbook-quality prose following the index structure
- **Tools:** `PhysicsRAGTool`
- **Process:**
  1. For each section, makes 3–4 RAG queries for theory, formulas, examples, and applications
  2. Writes section content with dynamic word counts (400–1,200 words based on complexity)
  3. Includes historical context, physical meaning, derivations, conceptual examples, mathematical examples, and applications
  4. Uses proper LaTeX (`$$...$$`) with mandatory variable definitions
- **Output:** Full chapter content (4,000–10,000+ words)

##### Agent 4: RAG Enhancer
- **Role:** Content Quality Enhancer
- **Goal:** Enrich the generated content with additional RAG data and verify accuracy
- **Tools:** `PhysicsRAGTool` + `SerperDevTool`
- **Process:** Cross-references with RAG to add missing topics, verify facts, and enhance depth
- **Output:** Enhanced chapter with additional examples and corrections

##### Agent 5: Markdown Formatter
- **Role:** Markdown Formatting Expert
- **Goal:** Ensure proper Markdown formatting, LaTeX syntax, and structural consistency
- **Tools:** `CodeInterpreterTool` (Python execution for validation)
- **Process:** Validates heading hierarchy, LaTeX rendering, figure tags, and section numbering
- **Output:** Final polished Markdown file

#### The 5 Tasks

Tasks are defined in `config/tasks.yaml` (63 KB of detailed prompts):

| # | Task | Agent | Input | Output |
|---|---|---|---|---|
| 1 | `research_physics_chapter` | Research Agent | Chapter number + name | Research document with 100% NCERT content |
| 2 | `create_topic_index` | Content Indexer | Research document | Hierarchical chapter outline |
| 3 | `generate_detailed_content` | Content Generator | Topic index | Full chapter prose |
| 4 | `enhance_with_rag` | RAG Enhancer | Generated content | Enhanced content |
| 5 | `create_final_markdown` | Markdown Formatter | Enhanced content | Final `.md` file |

Tasks are executed **sequentially** — each task's output feeds into the next as context.

#### The RAG Query Flow (Custom Tool)

When any agent queries the RAG system, here's the exact flow:

```
Agent says: "Chapter 7 Alternating Current resonance frequency derivation"
    │
    ▼
PhysicsRAGTool (custom_tool.py)
    │
    ├── Check in-memory cache → Hit? Return cached result
    │
    ├── Cache miss → Call query_rag_sync()
    │
    ▼
query_documents.py → query_processed_documents()
    │
    ├── Initialize SentenceTransformer (all-MiniLM-L6-v2, 384-dim)
    ├── Initialize LightRAG with existing storage (rag_storage/lightrag/)
    │
    ▼
LightRAG.aquery(query_text, mode="hybrid")
    │
    ├── 1. VECTOR SEARCH: Embed query → search vdb_chunks.json, vdb_entities.json, vdb_relationships.json
    ├── 2. GRAPH TRAVERSAL: Find relevant entities → traverse knowledge graph → gather connected concepts
    ├── 3. BM25 KEYWORD SEARCH: Tokenize query → match against BM25 index
    ├── 4. RESULT FUSION: Combine vector + graph + BM25 results with hybrid_alpha=0.5
    ├── 5. LLM SYNTHESIS: Pass top results to GPT-4.1-mini → generate coherent answer
    │
    ▼
Return: Synthesized content string (retrieved from actual textbook data)
```

**Key Configuration:**
- **Retrieval modes:** `local` (chunk vectors only), `global` (entity/relation vectors), `hybrid` (both), `naive` (simple vector search)
- **Top-K:** 15 results per query (default for generation), 6 results for quick lookups
- **Hybrid alpha:** 0.5 (equal weight to BM25 and dense retrieval)

---

## 📁 Project Structure

```
RAG-System-for-Content-Generation/
│
├── 📄 .env                              # API keys (OpenAI, Serper)
├── 📄 pyproject.toml                    # Python project config (dependencies, scripts)
├── 📄 requirements_complete.txt         # Pip requirements file
├── 📄 uv.lock                          # UV lockfile for dependency resolution
│
├── 📂 src/physics_content/             # ═══ CORE APPLICATION ═══
│   ├── 📄 __init__.py
│   ├── 📄 main.py                      # Entry point: interactive/batch chapter generation
│   ├── 📄 crew.py                      # CrewAI crew definition (5 agents, 5 tasks)
│   ├── 📄 rag_system.py               # RAG engine: PDF processing, indexing, querying (955 lines)
│   │
│   ├── 📂 config/
│   │   ├── 📄 agents.yaml              # Agent definitions: roles, goals, backstories (51 KB)
│   │   └── 📄 tasks.yaml               # Task definitions: prompts, expected outputs (63 KB)
│   │
│   └── 📂 tools/
│       ├── 📄 __init__.py
│       └── 📄 custom_tool.py           # PhysicsRAGTool: CrewAI-compatible RAG wrapper
│
├── 📄 query_documents.py               # Standalone RAG query interface (sync + async)
├── 📄 process_chapters_gpu.py          # GPU-accelerated batch PDF processing
├── 📄 test_import.py                   # Import validation script
│
├── 📂 RAG-Anything/                    # ═══ VENDORED RAG-ANYTHING LIBRARY ═══
│   ├── 📂 raganything/
│   │   ├── 📄 raganything.py           # Main RAG-Anything pipeline class
│   │   ├── 📄 parser.py               # Document parser (MinerU integration)
│   │   ├── 📄 processor.py            # Document processing pipeline
│   │   ├── 📄 modalprocessors.py       # Multimodal content processors (images, tables, equations)
│   │   ├── 📄 query.py                # Query engine
│   │   ├── 📄 batch.py                # Batch processing
│   │   ├── 📄 config.py               # Configuration classes
│   │   ├── 📄 prompt.py               # Prompt templates
│   │   ├── 📄 enhanced_markdown.py     # Enhanced Markdown generation
│   │   └── 📄 utils.py                # Utility functions
│   ├── 📄 setup.py
│   └── 📄 requirements.txt
│
├── 📂 knowledge/                       # ═══ INPUT: SOURCE TEXTBOOKS ═══
│   └── 📂 textbooks/
│       └── 📂 cert/
│           ├── 📂 part1/               # NCERT Physics Part 1 (Chapters 1-8)
│           │   ├── leph101.pdf         # Ch 1: Electric Charges and Fields
│           │   ├── leph102.pdf         # Ch 2: Electrostatic Potential
│           │   ├── leph103.pdf         # Ch 3: Current Electricity
│           │   ├── leph104.pdf         # Ch 4: Moving Charges and Magnetism
│           │   ├── leph105.pdf         # Ch 5: Magnetism and Matter
│           │   ├── leph106.pdf         # Ch 6: Electromagnetic Induction
│           │   ├── leph107.pdf         # Ch 7: Alternating Current
│           │   └── leph108.pdf         # Ch 8: Electromagnetic Waves
│           └── 📂 part2/               # NCERT Physics Part 2 (Chapters 9-14)
│               └── ... (7 PDFs)
│
├── 📂 output/                          # ═══ MINERUP PARSED OUTPUT ═══
│   ├── 📂 leph101/auto/               # Parsed Chapter 1
│   │   ├── 📂 images/                 # Extracted figure images
│   │   ├── leph101.md                 # Parsed Markdown
│   │   ├── leph101_content_list.json  # Structured content elements
│   │   └── ...                        # Layout, model, span files
│   ├── 📂 leph102/auto/               # Parsed Chapter 2
│   └── ... (5 chapters processed)
│
├── 📂 rag_storage/                     # ═══ RAG KNOWLEDGE BASE ═══
│   └── 📂 lightrag/
│       ├── graph_chunk_entity_relation.graphml  # Knowledge Graph (4 MB)
│       ├── vdb_chunks.json                      # Chunk Vector DB (5.6 MB)
│       ├── vdb_entities.json                    # Entity Vector DB (8 MB)
│       ├── vdb_relationships.json               # Relationship Vector DB (18 MB)
│       ├── kv_store_full_docs.json              # Full document texts
│       ├── kv_store_full_entities.json          # Entity metadata
│       ├── kv_store_full_relations.json         # Relation metadata
│       ├── kv_store_text_chunks.json            # Text chunk store
│       ├── kv_store_llm_response_cache.json     # LLM call cache (45 MB)
│       ├── kv_store_doc_status.json             # Processing status
│       └── kv_store_parse_cache.json            # Parse cache
│
├── 📂 artifacts/                       # ═══ GENERATION ARTIFACTS ═══
│   ├── checkpoint_7.json ... checkpoint_14.json  # Per-chapter progress
│   ├── 📂 rag_chunks/                 # Processing completion markers (.done files)
│   ├── 📂 rag_logs/                   # Timestamped processing logs
│   ├── 📂 research/                   # Research agent outputs
│   ├── 📂 index/                      # Content indexer outputs
│   ├── 📂 content/                    # Generator outputs
│   ├── 📂 enhanced/                   # Enhancer outputs
│   └── 📂 examples_bank/             # Example collections
│
└── 📄 class_12_physics_chapter_*.md    # ═══ FINAL OUTPUT (14 chapters) ═══
    ├── class_12_physics_chapter_1_Electric_Charges_and_Fields.md   (35 KB)
    ├── class_12_physics_chapter_2_Electrostatic_Potential_and_Capacitance.md   (127 KB)
    ├── class_12_physics_chapter_3_Current_Electricity.md   (58 KB)
    ├── class_12_physics_chapter_7_Alternating_Current.md   (106 KB)
    ├── class_12_physics_chapter_9_Ray_Optics_and_Optical_Instruments.md   (73 KB)
    ├── class_12_physics_chapter_10_Wave_Optics.md   (127 KB)
    ├── class_12_physics_chapter_11_Dual_Nature_of_Radition_and_Matter.md   (112 KB)
    ├── class_12_physics_chapter_12_Atoms.md   (86 KB)
    ├── class_12_physics_chapter_13_Nuclei.md   (126 KB)
    ├── class_12_physics_chapter_14_Semiconductor_Electronics.md   (165 KB)
    └── ... (all 14 chapters generated)
```

---

## 🔍 Deep Dive: Role of Each RAG Component

### 1. RAG-Anything — The Multimodal Processing Pipeline

**What it is:** An open-source framework ([IAAR-Shanghai/RAGAnything](https://github.com/IAAR-Shanghai/RAGAnything)) that processes documents containing mixed content types — text, images, tables, and equations — into a unified knowledge base.

**Why it's needed:** Physics textbooks aren't just text. They contain circuit diagrams, ray diagrams, mathematical equations, data tables, and graphs. RAG-Anything understands all of these.

**What it does in this project:**

1. **Document Parsing** — Uses MinerU as its parser backend to extract multimodal content from PDFs
2. **Multimodal Processing** — Has specialized processors for each content type:
   - `ImageModalProcessor` — Processes figures and diagrams using vision models (GPT-4.1-mini or LLaVA)
   - `TableModalProcessor` — Extracts and structures table data
   - `EquationModalProcessor` — Handles mathematical equations
   - `GenericModalProcessor` — Handles other content types
3. **LightRAG Integration** — Passes processed content to LightRAG for knowledge graph construction
4. **Context Extraction** — Extracts surrounding context for each multimodal element to improve retrieval

**File:** `RAG-Anything/raganything/raganything.py` — The `RAGAnything` class

### 2. LightRAG — Knowledge Graph + RAG Engine

**What it is:** A graph-based RAG framework ([HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)) that combines traditional vector search with knowledge graph traversal.

**Why it's needed:** Standard vector search finds semantically similar text, but it doesn't understand relationships. LightRAG builds a knowledge graph of entities and their connections, enabling multi-hop reasoning.

**What it does in this project:**

1. **Entity Extraction** — Uses LLM to identify physics concepts, laws, scientists, devices, etc. from text chunks
2. **Relation Extraction** — Identifies how entities relate to each other (e.g., "Faraday's Law" → "describes" → "Electromagnetic Induction")
3. **Knowledge Graph Storage** — Stores the entity-relation graph in GraphML format via NetworkX
4. **Multi-Mode Retrieval:**
   - **Local mode:** Retrieves relevant text chunks directly (like standard RAG)
   - **Global mode:** Queries the knowledge graph for entities and relations, then synthesizes an answer
   - **Hybrid mode:** Combines local chunks + global graph traversal for comprehensive results
5. **LLM Response Caching** — Caches all LLM calls to avoid redundant API usage

**Storage files:**

| File | Size | Purpose |
|---|---|---|
| `graph_chunk_entity_relation.graphml` | 4 MB | The knowledge graph (nodes = entities, edges = relations, linked to source chunks) |
| `kv_store_full_entities.json` | 58 KB | Detailed descriptions of each entity |
| `kv_store_full_relations.json` | 463 KB | Detailed descriptions of each relation |
| `kv_store_text_chunks.json` | 2.4 MB | All text chunks with metadata |
| `kv_store_llm_response_cache.json` | 45 MB | Cached LLM responses for entity/relation extraction |

### 3. Vector Databases — Semantic Search Layer

**Three vector databases** store different aspects of the knowledge base:

#### a) Chunk Vector DB (`vdb_chunks.json` — 5.6 MB)

- **Contains:** 384-dimensional embeddings of every text chunk from the parsed PDFs
- **Model:** all-MiniLM-L6-v2 (SentenceTransformers)
- **Purpose:** Enable semantic similarity search — find text chunks that are semantically similar to a query
- **Example:** Query "resonance in AC circuits" → finds chunks about LC circuits, impedance matching, quality factor
- **Backend:** nano-vectordb (lightweight JSON-based vector store used by LightRAG)

#### b) Entity Vector DB (`vdb_entities.json` — 8 MB)

- **Contains:** Embeddings of entity descriptions extracted by LightRAG
- **Purpose:** Find relevant physics concepts, laws, and devices by semantic search
- **Example:** Query "device that measures small currents" → finds entity "Moving Coil Galvanometer"

#### c) Relationship Vector DB (`vdb_relationships.json` — 18 MB)

- **Contains:** Embeddings of relationship descriptions between entities
- **Purpose:** Find connections between concepts for multi-hop retrieval
- **Example:** Query "connection between electric field and potential" → finds relation "Electric Field is the negative gradient of Electric Potential"

### 4. BM25 — Keyword Retrieval Layer

**What it is:** A classic information retrieval algorithm that ranks documents by keyword frequency.

**Why it's needed alongside vectors:** Vector search excels at understanding meaning but can miss exact term matches. BM25 ensures that if a student searches for "Wheatstone Bridge", documents containing that exact phrase are highly ranked.

**How it integrates:** The hybrid retrieval mode combines BM25 scores with vector similarity scores using a configurable `hybrid_alpha` parameter (default: 0.5, equal weighting).

### 5. MinerU — PDF Document Parser

**What it is:** A state-of-the-art open-source tool for accurate PDF content extraction, especially for academic and scientific documents.

**What it handles:**
- Complex multi-column layouts
- Mathematical equations → LaTeX extraction
- Tables → structured data
- Figures → image extraction + bounding box detection
- Reading order detection across complex layouts

**Why not just use PyPDF?** Standard PDF parsers extract raw text without understanding layout. MinerU uses deep learning models to understand page structure, which is critical for textbooks where equations, figures, and text are interleaved.

### 6. Embedding Model — all-MiniLM-L6-v2

**What it is:** A 384-dimensional sentence embedding model from SentenceTransformers.

**Why this model:**
- **Fast** — 80ms per batch on CPU
- **Compact** — 384 dimensions (vs. 1536 for OpenAI ada-002)
- **Free** — Runs locally, no API costs
- **Good quality** — Top-performing model on semantic similarity benchmarks for its size

**Where it's used:**
- Embedding text chunks during indexing
- Embedding queries during retrieval
- Embedding entity and relationship descriptions

### 7. OpenAI GPT-4.1-mini — The LLM Brain

**Where it's used:**
- **Entity extraction** — Identifying physics concepts from text chunks
- **Relation extraction** — Finding relationships between entities
- **Content generation** — Writing chapter prose (via CrewAI agents)
- **Multimodal analysis** — Understanding images and figures
- **Query synthesis** — Generating coherent answers from retrieved chunks

**Configuration:**
```
MODEL=gpt-4.1-mini
OPENAI_VISION_MODEL=gpt-4.1-mini
OPENAI_TEXT_MODEL=gpt-4.1-mini
OPENAI_EMBEDDING_MODEL=text-embedding-3-small  (not used — local embeddings preferred)
```

### 8. CrewAI — Multi-Agent Orchestration

**What it is:** A framework for building multi-agent AI systems where specialized agents collaborate on complex tasks.

**Why multi-agent?** A single prompt can't produce a full, accurate, well-structured textbook chapter. Breaking the task into specialized roles (researcher, indexer, writer, enhancer, formatter) produces dramatically better results because each agent focuses on one aspect of quality.

**Key configuration:**
- **Process:** Sequential (each agent's output feeds the next)
- **Agent configs:** `config/agents.yaml` (51 KB of detailed personas, rules, and formatting instructions)
- **Task configs:** `config/tasks.yaml` (63 KB of prompts, expected outputs, and quality checks)

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10–3.13**
- **OpenAI API Key** (for GPT-4.1-mini)
- **Serper API Key** (for web search, optional but recommended)
- **8+ GB RAM** (for embedding model and processing)
- **GPU (optional)** — CUDA-compatible GPU accelerates PDF parsing significantly

### Installation

```bash
# Clone the repository
git clone https://github.com/Ujjwal012003/RAG-System-for-Content-Generation.git
cd RAG-System-for-Content-Generation

# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate
# Activate (Linux/Mac)
# source .venv/bin/activate

# Install dependencies
pip install -r requirements_complete.txt

# Or using uv (faster):
# uv sync
```

### Configuration

Create a `.env` file in the project root:

```env
MODEL=gpt-4.1-mini
OPENAI_API_KEY=sk-your-api-key-here
SERPER_API_KEY=your-serper-key-here
USE_OPENAI_MULTIMODAL=1
USE_OPENAI_TEXT=1
OPENAI_VISION_MODEL=gpt-4.1-mini
OPENAI_TEXT_MODEL=gpt-4.1-mini
USE_OPENAI_EMBEDDING=1
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
```

### Step 1: Add Source PDFs

Place your textbook PDFs in the knowledge base directory:

```
knowledge/textbooks/cert/part1/   ← NCERT Part 1 chapters
knowledge/textbooks/cert/part2/   ← NCERT Part 2 chapters
```

### Step 2: Process PDFs (Build Knowledge Base)

```bash
# Process all PDFs (CPU)
python -m src.physics_content.rag_system

# Or with GPU acceleration
python process_chapters_gpu.py
```

This takes 5–30 minutes per PDF depending on length and hardware.

### Step 3: Verify the Knowledge Base

```bash
# Test a query
python query_documents.py "What is Coulomb's law?"
```

### Step 4: Generate Chapters

```bash
# Interactive mode (single chapter)
python -m src.physics_content.main

# Batch mode (all chapters 7-14)
python -m src.physics_content.main batch

# Or directly:
physics_content    # Uses pyproject.toml entry point
run_crew           # Alternative entry point
```

### Step 5: Find Your Output

Generated chapters appear in the project root:

```
class_12_physics_chapter_7_Alternating_Current.md
class_12_physics_chapter_8_Electromagnetic_Waves.md
...
```

---

## 📊 Performance & Cost

| Metric | Value |
|---|---|
| **PDF processing time** | 5–30 min per PDF (CPU), 2–10 min (GPU) |
| **Knowledge base size** | ~95 MB total (vectors + graph + caches) |
| **Chapter generation time** | 10–30 min per chapter |
| **API cost per chapter** | ~$0.50–$2.00 (GPT-4.1-mini) |
| **Output chapter size** | 35–165 KB (4,000–10,000+ words) |
| **RAG query latency** | 2–5 seconds per query |
| **Cache hit rate** | 30–60% (reduces API costs significantly) |

---

## 🔧 Environment Variables

| Variable | Default | Description |
|---|---|---|
| `MODEL` | `gpt-4.1-mini` | Primary LLM model |
| `OPENAI_API_KEY` | — | OpenAI API key (required) |
| `SERPER_API_KEY` | — | SerperDev API key (for NCERT TOC verification) |
| `USE_OPENAI_MULTIMODAL` | `0` | Enable OpenAI for image/figure analysis (`1` = enabled) |
| `USE_OPENAI_TEXT` | `0` | Enable OpenAI for text generation (`1` = enabled) |
| `OPENAI_VISION_MODEL` | `gpt-4.1-mini` | Vision model for multimodal content |
| `OPENAI_TEXT_MODEL` | `gpt-4.1-mini` | Text model for generation |
| `USE_OPENAI_EMBEDDING` | `0` | Use OpenAI embeddings (local preferred) |
| `OPENAI_EMBEDDING_MODEL` | `text-embedding-3-small` | OpenAI embedding model (if enabled) |
| `KB_ROOT` | `knowledge/textbooks` | Knowledge base root directory |
| `OLLAMA_VISION_MODEL` | `llava:7b` | Local vision model (Ollama fallback) |
| `OLLAMA_TEXT_MODEL` | `llama3.1:8b` | Local text model (Ollama fallback) |
| `OLLAMA_EMBEDDING_MODEL` | `all-minilm` | Local embedding model (Ollama fallback) |
| `CUDA_VISIBLE_DEVICES` | `0` | GPU device for acceleration |
| `MINERU_MAX_PAGES` | `100` | Max pages per PDF to process |
| `MINERU_TIMEOUT` | `600` | Processing timeout per PDF (seconds) |

---

## 🗂 Key Files Explained

| File | Lines | Purpose |
|---|---|---|
| `src/physics_content/main.py` | 273 | Entry point — single chapter or batch generation with checkpoint recovery |
| `src/physics_content/crew.py` | 180 | CrewAI crew definition — initializes 5 agents with tools, defines 5 tasks, creates sequential pipeline |
| `src/physics_content/rag_system.py` | 955 | Core RAG engine — PDF processing, LightRAG init, vector DB management, multi-mode querying |
| `src/physics_content/tools/custom_tool.py` | 133 | CrewAI tool wrapper — bridges CrewAI agents to the RAG system with caching and metrics |
| `query_documents.py` | 178 | Standalone query interface — async/sync RAG query with LightRAG + SentenceTransformer |
| `process_chapters_gpu.py` | 91 | GPU batch processor — processes all PDFs with CUDA acceleration |
| `config/agents.yaml` | 1,285 | Agent definitions — detailed personas, rules, formatting instructions for all 5 agents |
| `config/tasks.yaml` | 1,518 | Task definitions — comprehensive prompts, expected outputs, quality checks for all 5 tasks |

---

## 📝 License

This project is open source. The vendored RAG-Anything library is under the [MIT License](RAG-Anything/LICENSE).

---

## 🙏 Acknowledgments

- **[CrewAI](https://github.com/joaomdmoura/crewAI)** — Multi-agent AI framework
- **[LightRAG (HKU)](https://github.com/HKUDS/LightRAG)** — Graph-based RAG engine
- **[RAG-Anything](https://github.com/IAAR-Shanghai/RAGAnything)** — Multimodal document processing
- **[MinerU](https://github.com/opendatalab/MinerU)** — PDF document understanding
- **[SentenceTransformers](https://www.sbert.net/)** — Embedding models
- **[OpenAI](https://openai.com)** — GPT-4.1-mini LLM
- **NCERT** — Source textbook content

---

<p align="center">
  Built with ❤️ for students preparing for Board Exams, JEE, and NEET.
</p>

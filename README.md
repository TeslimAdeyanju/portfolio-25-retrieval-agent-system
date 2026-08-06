# Portfolio 25: Retrieval Agent System

This repository documents the development of a production-minded retrieval
agent system with persistent search, tool calling, iterative retrieval, and
typed agent frameworks.

The project began as part of the
[DataTalks.Club LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp),
but the focus here is what is being built, not the course itself.

I am using this project as a public portfolio to demonstrate practical skills in:

- Retrieval-Augmented Generation (RAG)
- Agentic workflows and tool/function calling
- Vector and keyword search foundations
- Evaluation and monitoring for LLM systems
- Production-minded AI application development

## What I Have Built So Far

Current focus: **Module 1 - Agentic RAG**

Implemented in this repo:

- FAQ data ingestion from DataTalks.Club endpoints
- Lightweight keyword index using `minsearch`
- Reusable RAG pipeline class (`RAGBase`) with:
	- retrieval (`search`)
	- context construction (`build_context`)
	- prompt construction (`build_prompt`)
	- LLM answer generation via OpenAI Responses API (`llm`)
	- end-to-end pipeline (`rag`)
- Notebook-based experimentation for iterative development

## Repository Structure

```text
.
├── pyproject.toml
├── uv.lock
├── README.md
└── 01-rag-foundations/
		├── ingestion.py
		├── rag_pipeline.py
		├── faq-search.db
		├── 01-rag-basics-and-keyword-search.ipynb
		├── 02-reusable-rag-pipeline.ipynb
		├── 03-sqlite-search-index.ipynb
		├── 04-agentic-rag-function-calling.ipynb
		├── 05-agentic-loop-notes.md
		├── 05-agentic-loop.ipynb
		├── 06-toyaikit-vs-handwritten-loop-notes.md
		├── 06-toyaikit-vs-handwritten-loop.ipynb
		├── 07-pydantic-ai-vs-toyaikit-notes.md
		├── 07-pydantic-ai-vs-toyaikit.ipynb
		└── agent_loop.py
```

The numbered learning notes follow the progression from RAG foundations to
agentic systems: understand keyword search, extract the reusable pipeline,
persist the index with SQLite, add one function-calling round trip, implement
the repeated agent loop, and compare framework abstractions.

## Tech Stack

- Python 3.10+
- OpenAI Python SDK
- minsearch
- Requests
- Jupyter notebooks
- python-dotenv

## Setup

1. Clone this repository.
2. Create and activate a Python environment.
3. Install dependencies.
4. Configure environment variables.

Example using `uv`:

```bash
uv sync
```

Set your API key in `.env`:

```env
OPENAI_API_KEY=your_key_here
```

## Quick Usage (RAG Pipeline)

```python
import importlib.util
from pathlib import Path

from openai import OpenAI

def load_module(module_name, file_path):
	spec = importlib.util.spec_from_file_location(module_name, file_path)
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)
	return module

base = Path("01-rag-foundations")
ingest = load_module("ingestion", base / "ingestion.py")
rag_pipeline = load_module("rag_pipeline", base / "rag_pipeline.py")

docs = ingest.load_faq_data()
index = ingest.build_index(docs)
client = OpenAI()

rag = rag_pipeline.RAGBase(index=index, llm_client=client)
answer = rag.rag("How do I submit homework?")
print(answer)
```

The numbered folder is intentionally a learning-stage label. The helper
modules are loaded by file path in this quick-start example so they can remain
alongside the notebooks without requiring package setup.

## Learning Outcomes I Am Targeting

By the end of this Zoomcamp portfolio project, I aim to show evidence of:

- Designing robust retrieval pipelines
- Improving answer quality with better chunking and ranking
- Building agentic components that can choose tools/functions
- Evaluating retrieval and generation quality systematically
- Monitoring usage, quality, and system behavior in production-style workflows

## Roadmap

- [x] Module 1 foundations: ingest + retrieval + baseline RAG
- [ ] Module 2: semantic/vector search and hybrid retrieval
- [ ] Module 3: orchestration workflows
- [ ] Module 4: evaluation framework
- [ ] Module 5: monitoring and feedback loops
- [ ] Module 6: best practices (hybrid search, reranking, framework patterns)
- [ ] Module 7: end-to-end polished capstone

## Why This Repo Exists

This is not just course homework. It is my end-to-end AI engineering portfolio project
to showcase what I can build with LLMs, RAG, and agentic systems from prototype to
production-ready patterns.

## Credits

- Course: DataTalks.Club LLM Zoomcamp
- Course repository:
	https://github.com/DataTalksClub/llm-zoomcamp

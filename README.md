# LLM Zoomcamp 2026 Portfolio: Agentic RAG Journey

This repository tracks what I am learning and building during the
[DataTalks.Club LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp).

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
├── main.py
├── pyproject.toml
├── uv.lock
├── README.md
└── 01-agentic-rag/
		├── ingest.py
		├── rag_helper.py
		├── notebook.ipynb
		└── reusable_rag_pipeline.ipynb
```

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

base = Path("01-agentic-rag")
ingest = load_module("ingest", base / "ingest.py")
rag_helper = load_module("rag_helper", base / "rag_helper.py")

docs = ingest.load_faq_data()
index = ingest.build_index(docs)
client = OpenAI()

rag = rag_helper.RAGBase(index=index, llm_client=client)
answer = rag.rag("How do I submit homework?")
print(answer)
```

Note: because the folder name starts with a number (`01-agentic-rag`), normal `from ... import ...` syntax will not work directly unless you rename the directory. The notebooks in this repo are the current working interface.

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

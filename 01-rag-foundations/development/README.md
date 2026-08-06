# Development

This folder contains the working implementation for the retrieval agent system:

- numbered notebooks for RAG and agent experiments;
- reusable Python modules;
- the local SQLite search index;
- supporting images.

Run notebooks from this directory so imports such as `from ingestion import ...`
resolve naturally. The root project environment contains the development
dependencies and can be synchronized with `uv sync` from the repository root.

# 7. Comparison Checkpoint: PydanticAI vs ToyAIKit

This note follows [06-toyaikit-vs-handwritten-loop.ipynb](06-toyaikit-vs-handwritten-loop.ipynb) and applies the same framework-learning process to PydanticAI. The hands-on notebook is [07-pydantic-ai-vs-toyaikit.ipynb](07-pydantic-ai-vs-toyaikit.ipynb).

## Why PydanticAI

PydanticAI provides a typed agent abstraction with support for multiple model providers. It uses ordinary Python functions, type hints, and docstrings to describe tools, while the framework manages model requests, tool calls, validation, and result handling.

Install it with:

```bash
uv add pydantic-ai
```

## Typed dependencies

Runtime resources such as the search index should be passed as dependencies instead of hidden in global state. A dependency object makes the tool's requirements explicit and easier to test.

```python
@dataclass
class SearchDependencies:
    index: object
```

## Typed tools

A PydanticAI tool uses a context object to access dependencies and a typed argument for the search query:

```python
@agent.tool
def search(ctx: RunContext[SearchDependencies], query: str) -> list[dict]:
    """Search the LLM Zoomcamp FAQ for matching course information."""
    return ctx.deps.index.search(
        query,
        num_results=5,
        boost_dict={"question": 3.0, "section": 0.5},
        filter_dict={"course": "llm-zoomcamp"},
    )
```

The framework can derive the model-facing schema from the function signature and docstring. The type hint describes the argument shape; the docstring explains when the tool is useful.

## Agent execution

The agent owns the repeated request and tool-calling flow:

```python
result = agent.run_sync(
    "How do I run Olama locally?",
    deps=deps,
)
```

Compare the output and tool behavior with notebook 05. The framework removes loop plumbing, but retrieval quality, instructions, provider configuration, permissions, and observability remain application responsibilities.

## What to inspect

Depending on the installed PydanticAI version, inspect the result object for:

- final output;
- usage and token counts;
- message history;
- tool calls and results;
- validation or model errors.

Do not assume result APIs across versions. Use `dir(result)` and the installed documentation when exploring.

## Comparison checkpoint

| Approach | What you write | What the framework manages |
| --- | --- | --- |
| Handwritten loop | schemas, history, dispatch, stopping | nothing beyond the model client |
| ToyAIKit | tools, prompts, callbacks | loop, display, history, cost helpers |
| PydanticAI | typed agent, dependencies, tools | schema generation, execution, validation, result handling |

Use PydanticAI when typed tools, dependency injection, and provider flexibility are valuable. Keep the handwritten version available as a debugging reference and always measure whether the abstraction improves the application enough to justify its dependency and operational behavior.

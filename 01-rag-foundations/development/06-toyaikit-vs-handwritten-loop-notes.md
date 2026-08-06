# 6. Comparison Checkpoint: Handwritten Loop vs ToyAIKit

This note follows [05-agentic-loop-notes.md](05-agentic-loop-notes.md) and summarizes the framework lessons. The central idea is simple: frameworks package the same tool-calling loop, history management, and stopping behavior we implemented by hand.

For hands-on ToyAIKit practice, run [06-toyaikit-vs-handwritten-loop.ipynb](06-toyaikit-vs-handwritten-loop.ipynb). The notebook follows the lesson in execution order and keeps model-calling cells available for you to run after checking your environment.

## What frameworks hide

A framework typically manages:

- tool registration and schema generation;
- model requests and response parsing;
- function dispatch;
- conversation sessions and history;
- callbacks, tracing, and display;
- iteration and error handling.

The abstraction is useful when it removes repetitive plumbing. It becomes a problem when the developer cannot explain what the framework is doing underneath.

Start with the handwritten loop when learning or debugging. Move to a framework when the application needs shared conventions, integrations, persistence, tracing, or multi-agent workflows.

## Typed tools and generated schemas

Many frameworks derive a JSON schema from a typed Python function and its docstring:

```python
def search(query: str) -> dict[str, str]:
    """Search the FAQ database for matching course information."""
    return search_faq(query)
```

The type hint describes the argument shape. The docstring describes the tool's purpose and helps the model decide when to use it. Generated schemas reduce manual JSON, but they do not remove the need for clear descriptions, validation, permissions, and tests.

## A teaching framework: ToyAIKit

The DataTalks.Club lesson uses ToyAIKit because its implementation is small and easy to inspect. It can:

- register a search function and its schema;
- derive a schema from type hints and docstrings;
- run the agent loop;
- display messages and tool calls in a notebook;
- retain `all_messages`, token usage, and cost information;
- continue a conversation using previous messages.

ToyAIKit is useful for experimentation and understanding. It is a teaching library, not a default production recommendation. Treat it as a transparent bridge between the manual implementation and larger frameworks.

## Framework choices

### OpenAI Agents SDK

The official OpenAI option. It fits naturally with the Responses API used in this project and supports tools, multi-turn conversations, and handoffs between agents. Consider it when the application is primarily OpenAI-based and you want an official SDK.

### PydanticAI

A type-oriented framework with support for multiple model providers. Tools are ordinary typed Python functions, which makes validation and provider changes straightforward. Consider it when type safety and multi-provider support matter.

### LangChain and LangGraph

LangChain provides a broad integration ecosystem. LangGraph adds explicit graph-based workflow control for more complex or stateful agent patterns. Consider them when you need many integrations or want to model workflows as a graph rather than one simple loop.

### Google ADK

Google's Agent Development Kit, designed for Gemini and Google Cloud-oriented applications. Consider it when the model and deployment stack are primarily Google-based.

### Other options

- CrewAI: multi-agent orchestration.
- AutoGen: multi-agent conversations.
- Semantic Kernel: Microsoft's C# and Python ecosystem.
- Smolagents: lightweight agents from Hugging Face.
- Anthropic tool use: native tool calling through Anthropic's API.

Framework names change quickly. Evaluate the current documentation, release activity, provider support, observability, testing story, and license before choosing one.

## How to choose

Ask these questions:

1. Do I need an agent at all?
2. Do I need one provider or several?
3. Do I need graph workflows, handoffs, or multiple agents?
4. How important are type validation and structured outputs?
5. Do I need built-in tracing, evaluation, persistence, or human approval?
6. Can the team debug the abstraction when a tool call fails?
7. What is the operational cost of adding the dependency?

Keep the tool contract and domain logic independent from the framework where possible. That makes it easier to switch providers or frameworks without rewriting the search backend.

## Avoid agents when a simpler solution works

Agents introduce real costs:

- more model calls and higher token spend;
- increased latency;
- non-deterministic paths between runs;
- more monitoring and failure modes;
- possible loops, repeated searches, and tool misuse.

Try these first:

- plain RAG with one search and one answer;
- a deterministic pipeline or parser;
- one LLM call without tools;
- a normal Python function or API call.

Use an agent when the task genuinely benefits from dynamic decisions, query rewriting, clarification, multiple tools, or multi-step work. The right question is not "Which framework is best?" but "What complexity does this workflow actually require?"

## Comparison exercise

For this project, compare three implementations:

| Approach | Best for | Main trade-off |
| --- | --- | --- |
| Fixed RAG | Predictable FAQ retrieval | Cannot recover from a poor first search |
| Handwritten loop | Learning and precise control | More plumbing to maintain |
| Framework-based agent | Reusable production workflows | More abstraction and dependencies |

Write down one failure mode for each approach and one metric you would monitor. A good answer should mention retrieval quality for fixed RAG, iteration and tool errors for the handwritten loop, and framework-level tracing plus cost for the packaged agent.

## Final checkpoint

Build the simplest version that meets the requirement. Only introduce an agent framework after you can explain:

- what the model decides;
- what the application executes;
- how history is stored;
- how the loop stops;
- how tools are validated;
- how cost and failures are observed.

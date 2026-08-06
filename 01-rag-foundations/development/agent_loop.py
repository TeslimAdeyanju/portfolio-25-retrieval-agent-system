import json


def make_call(call, tool_functions):
    """Execute one model tool call and format its result for the API."""
    arguments = json.loads(call.arguments)
    function = tool_functions.get(call.name)

    if function is None:
        raise ValueError(f"Unknown tool: {call.name}")

    result = function(**arguments)
    return {
        "type": "function_call_output",
        "call_id": call.call_id,
        "output": json.dumps(result, indent=2),
    }


def process_response(response, messages, tool_functions):
    """Append response items, execute tools, and return loop state."""
    messages.extend(response.output)
    has_function_calls = False
    last_answer = None

    for item in response.output:
        if item.type == "function_call":
            messages.append(make_call(item, tool_functions))
            has_function_calls = True
        elif item.type == "message":
            last_answer = item.content[0].text

    return has_function_calls, last_answer


def agent_loop(
    openai_client,
    instructions,
    question,
    search_tool,
    tool_functions,
    model="gpt-5.4-mini",
    max_iterations=5,
):
    """Run a bounded Responses API tool-calling loop."""
    messages = [
        {"role": "developer", "content": instructions},
        {"role": "user", "content": question},
    ]

    for _ in range(max_iterations):
        response = openai_client.responses.create(
            model=model,
            input=messages,
            tools=[search_tool],
        )
        has_function_calls, last_answer = process_response(
            response, messages, tool_functions
        )

        if not has_function_calls:
            return last_answer

    raise RuntimeError("Agent stopped after reaching the iteration limit")
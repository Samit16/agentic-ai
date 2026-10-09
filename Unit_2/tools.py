from smolagents import CodeAgent, tool, LiteLLMModel


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers.

    Args:
        a: The first integer to multiply.
        b: The second integer to multiply.
    """
    return a * b


model = LiteLLMModel(
    model_id="ollama_chat/qwen2.5:7b",
    api_base="http://localhost:11434"
)
agent = CodeAgent(
    tools=[multiply],
    model=model
)

agent.run("What is 25 multiplied by 4?")
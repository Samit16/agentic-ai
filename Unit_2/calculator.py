from smolagents import CodeAgent, tool, LiteLLMModel

@tool 
def add(a:int, b:int) -> int:
    """Add two integers.
    
    
    Args:
        a: The first integer to add.
        b: The second integer to add.
    """ 
    return a+b

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
    tools=[add, multiply],
    model=model
)

agent.run("What is 25 multiplied by 4?")
agent.run("What is 25 added to 43?")
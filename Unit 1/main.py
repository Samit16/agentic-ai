from ollama import chat

response=chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role":"user",
            "content": "Explain AI agents in simple terms"
        }
    ]
)

print(response.message.content)
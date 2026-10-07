from ollama import chat

response=chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role":"user",
            "content": "My name is Samit. I am 21 years old. I know Python, Java, React and Solidity."
        },
        {
            "role":"system",
            "content":" You extract structured information. Always return valid JSON.Do not include markdown or explanations."
        }
    ]
)

print(response.message.content)
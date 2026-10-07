from pydantic import BaseModel
from ollama import chat
import json


class Person(BaseModel):
    name: str
    age: int
    skills: list[str]


response = chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role": "user",
            "content": """
            My name is Samit. I am 21 years old.
            I know Python, Java, React and Solidity.
            """
        },
        ],
        format=Person.model_json_schema()
    )
print(response.message.content)

data = json.loads(response.message.content)

person = Person.model_validate(data)

print(person.name)
print(person.age)
print(person.skills)
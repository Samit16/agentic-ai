from ollama import chat
from pydantic import BaseModel
import json


class JobAnalysis(BaseModel):
    role: str
    match_score: int
    matching_skills: list[str]
    missing_skills: list[str]


job_description = input("Enter the job description: ")
my_skills = input("Enter your skills: \n")

response = chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role": "system",
            "content": """
            You are a job analysis assistant.
            Analyze the job description against the candidate's skills.
            Return the result according to the provided schema.
            """
        },
        {
            "role": "user",
            "content": f"""
            Job Description:{job_description}
            Candidate Skills:{my_skills}
            """
        }
    ],
    format=JobAnalysis.model_json_schema()
)

data = json.loads(response.message.content)
print(data["role"])
print(data["match_score"])
print(data["matching_skills"])
print(data["missing_skills"])
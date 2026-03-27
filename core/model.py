from openai import OpenAI
import os

BASE_URL = os.getenv("LLM_BASE_URL", "http://127.0.0.1:11434/v1")
MODEL = os.getenv("LLM_MODEL", "phind-codellama:34b")

client = OpenAI(
    base_url=BASE_URL,
    api_key="local",
)

def query(messages):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )
    return response.choices[0].message.content

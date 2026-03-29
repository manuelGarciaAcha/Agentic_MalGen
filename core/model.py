import os

from openai import OpenAI


def get_client():
    return OpenAI(
        base_url=os.getenv("LLM_BASE_URL", "http://127.0.0.1:11434/v1"),
        api_key=os.getenv("LLM_API_KEY", "local"),
    )


def query(messages, model=None, temperature=0.2):
    client = get_client()
    model = model or os.getenv("LLM_MODEL", "codegemma:7b")
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content

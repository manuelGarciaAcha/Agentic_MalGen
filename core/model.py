from openai import OpenAI
import os


BASE_URL=os.getenv("LLM_BASE_URL", "http://127.0.0.1:11434/v1")
MODEL=os.getenv("LLM_MODEL", "stable-code")
# define client's provider and api key


client = OpenAI(
    base_url=BASE_URL,
    api_key="local",
    )

# define how code queries the LLM

#def chat(system: str, user: str) -> str:
#    response = client.chat.completions.create(
#        model=MODEL,
#        messages=[
#            {"role": "system", "content": system},
#            {"role": "user", "content": user},
#        ],
#    )
#    return response.choices[0].message.content


def query(messages):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        )
    return response.choices[0].message.content

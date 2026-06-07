"""
model.py — LLM querying via OpenAI-compatible local API.

Compatible with Ollama, LM Studio, or any OpenAI-spec local server.
Matches the original system's inference setup (local endpoint, no
external network calls).
"""

import json
from openai import OpenAI
from pydantic import BaseModel
from typing import Type, TypeVar

T = TypeVar("T", bound=BaseModel)

# Local inference endpoint — same as original system
LOCAL_API_BASE = "http://localhost:11434/v1"
LOCAL_API_KEY = "ollama"  # placeholder, not validated by local servers


def get_client() -> OpenAI:
    return OpenAI(base_url=LOCAL_API_BASE, api_key=LOCAL_API_KEY)


def query_model(
    model_name: str,
    system_prompt: str,
    user_prompt: str,
    temperature: float = 0.2,
) -> str:
    """
    Raw text query. Used by the Generator agent where we want
    Python code back directly, not structured JSON.
    """
    client = get_client()
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()


def query_model_structured(
    model_name: str,
    system_prompt: str,
    user_prompt: str,
    schema: Type[T],
    temperature: float = 0.1,
) -> T:
    """
    Structured query — instructs the model to return JSON matching
    the provided Pydantic schema, then validates and parses it.

    This replaces the original system's fragile freeform JSON approach
    that caused failures in Stable Code and Yi-Coder 9B. By injecting
    the schema into the system prompt and validating with Pydantic,
    we eliminate the JSON formatting failure mode.
    """
    schema_json = json.dumps(schema.model_json_schema(), indent=2)
    augmented_system = (
        f"{system_prompt}\n\n"
        f"You MUST respond with valid JSON only. No explanation text. "
        f"No markdown. No code fences. Match this exact schema:\n{schema_json}"
    )

    client = get_client()
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": augmented_system},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
    )

    raw = response.choices[0].message.content.strip()

    # Strip markdown fences if model ignores instructions
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    return schema.model_validate_json(raw)

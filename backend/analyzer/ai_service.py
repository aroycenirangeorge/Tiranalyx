import os
import json
from pathlib import Path

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / ".envvars")


HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN was not loaded")


client = InferenceClient(
    api_key=HF_TOKEN
)


MODEL = "Qwen/Qwen2.5-7B-Instruct"


def analyze_with_ai(context):

    prompt = f"""
You are Tiranalyx, an AI log analysis assistant.

Analyze the following structured incident context.

Only use evidence provided in the context.
Do not invent log events.

Incident context:
{context}

Return ONLY valid JSON.
Do not use markdown.
Do not add explanations outside the JSON.

Use exactly this structure:

{{
    "problem": "Brief description of what happened",
    "likely_cause": "Most likely cause based only on the provided evidence",
    "recommended_actions": [
        "Action 1",
        "Action 2",
        "Action 3"
    ]
}}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=400,
        temperature=0.2
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "problem": "AI returned an invalid response.",
            "likely_cause": "",
            "recommended_actions": []
        }
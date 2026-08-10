import os
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

Your task is to identify:
1. What happened
2. The likely root cause
3. Recommended action

Only use evidence provided in the context.
Do not invent log events.

Incident context:
{context}

Return the response in this format:

Problem:
<problem>

Likely Cause:
<likely cause>

Recommended Action:
<recommended action>
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=300,
        temperature=0.2
    )

    return response.choices[0].message.content
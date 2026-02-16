"""
openai_test.py — My first OpenAI GPT-4 API call
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()

# Create the client (automatically reads OPENAI_API_KEY from environment)
client = OpenAI()

# Same prompt as Claude for a fair comparison
PROMPT = "Explain what an API is in 3 sentences, as if talking to a 10-year-old."

# Make the API call
response = client.chat.completions.create(
    model="gpt-4o",              # GPT-4o — OpenAI's flagship model
    max_tokens=1024,
    messages=[
        {"role": "user", "content": PROMPT}
    ]
)

# Print the response
print("=" * 60)
print("GPT-4o's RESPONSE")
print("=" * 60)
print(f"Model: {response.model}")
print(f"Tokens used: {response.usage.prompt_tokens} in / {response.usage.completion_tokens} out")
print("-" * 60)
print(response.choices[0].message.content)
print("=" * 60)
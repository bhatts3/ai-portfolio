"""
claude_test.py — My first Claude API call
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

try:
    from anthropic import Anthropic
except ModuleNotFoundError:
    print("Error: Missing dependency 'anthropic'. Install with:")
    print("  pip install -r requirements.txt")
    print("Or activate your venv: source venv/bin/activate")
    sys.exit(1)

if not os.environ.get("ANTHROPIC_API_KEY"):
    print("Error: ANTHROPIC_API_KEY not set. Add it to .env in the project root.")
    sys.exit(1)

client = Anthropic()
PROMPT = "Explain what an API is in 3 sentences, as if talking to a 10-year-old."

try:
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        messages=[{"role": "user", "content": PROMPT}],
    )
except Exception as e:
    err = str(e).lower()
    if "credit" in err or "balance" in err or "billing" in err:
        print("Error: Your Anthropic account has insufficient credits.")
        print("Go to https://console.anthropic.com → Plans & Billing to add credits.")
    else:
        print(f"API error: {e}")
    sys.exit(1)

print("=" * 60)
print("CLAUDE'S RESPONSE")
print("=" * 60)
print(f"Model: {message.model}")
print(f"Tokens used: {message.usage.input_tokens} in / {message.usage.output_tokens} out")
print("-" * 60)
print(message.content[0].text)
print("=" * 60)
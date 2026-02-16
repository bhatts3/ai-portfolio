"""
compare_models.py — Compare Claude vs GPT-4o on the same prompt
"""

import os
import time
from dotenv import load_dotenv
from anthropic import Anthropic
from openai import OpenAI

load_dotenv()

# Initialize both clients
claude_client = Anthropic()
openai_client = OpenAI()

# The prompt to compare
PROMPT = "Explain what an API is in 3 sentences, as if talking to a 10-year-old."

print("\n" + "=" * 70)
print(f"PROMPT: {PROMPT}")
print("=" * 70)

# --- Claude ---
print("\n🟠 CALLING CLAUDE (claude-sonnet-4-5-20250929)...")
start = time.time()

claude_response = claude_client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    messages=[{"role": "user", "content": PROMPT}]
)

claude_time = time.time() - start
claude_text = claude_response.content[0].text
claude_tokens_in = claude_response.usage.input_tokens
claude_tokens_out = claude_response.usage.output_tokens

print(f"   Response time: {claude_time:.2f}s")
print(f"   Tokens: {claude_tokens_in} in / {claude_tokens_out} out")
print(f"\n{claude_text}")

# --- GPT-4o ---
print("\n🟢 CALLING GPT-4o...")
start = time.time()

openai_response = openai_client.chat.completions.create(
    model="gpt-4o",
    max_tokens=1024,
    messages=[{"role": "user", "content": PROMPT}]
)

gpt_time = time.time() - start
gpt_text = openai_response.choices[0].message.content
gpt_tokens_in = openai_response.usage.prompt_tokens
gpt_tokens_out = openai_response.usage.completion_tokens

print(f"   Response time: {gpt_time:.2f}s")
print(f"   Tokens: {gpt_tokens_in} in / {gpt_tokens_out} out")
print(f"\n{gpt_text}")

# --- Summary ---
print("\n" + "=" * 70)
print("COMPARISON SUMMARY")
print("=" * 70)
print(f"{'Metric':<25} {'Claude':<22} {'GPT-4o':<22}")
print("-" * 70)
print(f"{'Response time':<25} {claude_time:<22.2f} {gpt_time:<22.2f}")
print(f"{'Input tokens':<25} {claude_tokens_in:<22} {gpt_tokens_in:<22}")
print(f"{'Output tokens':<25} {claude_tokens_out:<22} {gpt_tokens_out:<22}")
print(f"{'Response length (chars)':<25} {len(claude_text):<22} {len(gpt_text):<22}")
print("=" * 70)

# --- Save to file ---
with open("comparison_output.txt", "w") as f:
    f.write(f"Prompt: {PROMPT}\n\n")
    f.write(f"--- CLAUDE ---\n{claude_text}\n\n")
    f.write(f"--- GPT-4o ---\n{gpt_text}\n")

print("\n✅ Full outputs saved to comparison_output.txt")
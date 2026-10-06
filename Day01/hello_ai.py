"""Day 01 - Hello AI.

Purpose: the smallest possible program that sends one question to Claude
and prints the answer.

How to run:
    1. Set the ANTHROPIC_API_KEY environment variable (see the main README).
    2. python hello_ai.py
"""

import anthropic

client = anthropic.Anthropic()  # Reads the API key from the ANTHROPIC_API_KEY env var

# Send a single question to Claude
response = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=200,
    messages=[{"role": "user", "content": "what is llm"}],
)

# The response may also contain a thinking block, so index 1 is used here
# to reach the text block
print(response.content[1].text)

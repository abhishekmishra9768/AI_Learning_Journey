"""Day 01 - Simple chat assistant.

Purpose: a terminal chat loop. Each question is sent to Claude on its own,
so the assistant does NOT remember earlier messages.

How to run:
    python assitent.py
    Type your question, or type "quit" to exit.
"""

import anthropic

# Create the API client (reads ANTHROPIC_API_KEY from the environment)
client = anthropic.Anthropic()

# Print a simple banner
print("*" * 40)
print("My AI Assistant")
print("*" * 40)

# Chat loop: each question is sent on its own (no memory of earlier turns)
while True:
    user_input = input("\nYou : ")

    # Exit the program when the user types "quit"
    if user_input.lower() == "quit":
        print("\nAI  : Goodbye! Have a great day.")
        break

    # Send the user's message to Claude
    response = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=1000,
        messages=[{"role": "user", "content": user_input}],
    )

    # The response can contain several blocks; print only the text ones
    for block in response.content:
        if block.type == "text":
            print("\nAI  :", block.text)

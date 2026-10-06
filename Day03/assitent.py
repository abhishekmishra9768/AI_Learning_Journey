"""Day 03 - Chat assistant with roles (system prompts).

Purpose: the user first chooses a role (English Teacher, Travel Guide or
Motivational Coach). The role's system prompt controls how Claude answers.

How to run:
    python assitent.py
    Choose a role (1-3), then chat. Type "quit" to exit.
"""

import anthropic

# Create the API client (reads ANTHROPIC_API_KEY from the environment)
client = anthropic.Anthropic()

print("*" * 40)
print("My AI Assistant")
print("*" * 40)

# Available roles; each role has a system prompt that sets the assistant's behaviour
roles = {
    "1": {
        "name": "English Teacher",
        "prompt": "You are an English teacher. Explain in simple words and don't use technical jargon.",
    },
    "2": {
        "name": "Travel Guide",
        "prompt": "You are a travel guide. Suggest places, hotels and travel tips.",
    },
    "3": {
        "name": "Motivational Coach",
        "prompt": "You are a motivational coach. Inspire and encourage the user.",
    },
}

print("1. English Teacher")
print("2. Travel Guide")
print("3. Motivational Coach")

# Let the user pick a role and use its prompt as the system prompt
choice = input("Choose role: ")

system_prompt = roles[choice]["prompt"]

# Conversation history sent with every request
msg = []

while True:
    user_input = input("\nYou : ")

    # Exit the program when the user types "quit"
    if user_input.lower() == "quit":
        print("\nAI : Goodbye! Have a great day.")
        break

    msg.append({"role": "user", "content": user_input})

    # The system prompt makes Claude answer in the chosen role
    response = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=500,
        system=system_prompt,
        messages=msg,
    )

    # Take the first text block as the reply
    for block in response.content:
        if block.type == "text":
            ai_reply = block.text
            break

    print("\nAI :", ai_reply)

    msg.append({"role": "assistant", "content": ai_reply})

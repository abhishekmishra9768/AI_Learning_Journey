"""Day 04 - Assistant with local tools.

Purpose: before calling Claude, the input is checked by execute_tool()
(tools_manager.py). If it asks for the time, a dice roll or a password,
the answer comes from a local Python function and no API call is made.

How to run:
    python assitent.py
    Choose a role, then try: "what time is it", "roll a dice",
    "generate a password". Type "quit" to exit.
"""

import anthropic
from tools import *
from tools_manager import *

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

    # Try the local tools first (time, dice, password).
    # If one matches, print its result and skip the API call.
    tools_result = execute_tool(user_input)
    if tools_result:
        print("\nAI: ", tools_result)
        continue

    # Older version of the tool routing, replaced by execute_tool() above
    # if "time" in user_input.lower():

    #     print("\nAI :", get_current_time())

    #     continue

    # if "dice" in user_input.lower():

    #     print("\nAI : You rolled", roll_dice())

    #     continue

    # if "password" in user_input.lower():

    #     print("\nAI :", generate_password())

    #     continue

    # Exit the program when the user types "quit"
    if user_input.lower() == "quit":
        print("\nAI : Goodbye! Have a great day.")
        break

    # Save the user's message
    msg.append({"role": "user", "content": user_input})

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

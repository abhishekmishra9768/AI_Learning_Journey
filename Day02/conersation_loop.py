"""Day 02 - Chat assistant with conversation memory.

Purpose: same chat loop as Day 01, but the full conversation history is
sent with every request, so Claude remembers what was said before.

How to run:
    python conersation_loop.py
    Type your question, or type "quit" to exit.
"""

import anthropic

# Create the API client (reads ANTHROPIC_API_KEY from the environment)
client = anthropic.Anthropic()

print("*" * 40)
print("My AI Assistant")
print("*" * 40)

# Conversation history: every user and assistant message is stored here
# and sent again with each request, so the model remembers the chat
msg = []

while True:
    user_input = input("\nYou : ")

    # Exit the program when the user types "quit"
    if user_input.lower() == "quit":
        print("\nAI : Goodbye! Have a great day.")
        break

    # Add the user's message to the history
    msg.append({"role": "user", "content": user_input})

    # Send the whole history to Claude
    response = client.messages.create(
        model="claude-sonnet-5-5", max_tokens=500, messages=msg
    )

    # Take the first text block as the reply
    for block in response.content:
        if block.type == "text":
            ai_reply = block.text
            break

    print("\nAI :", ai_reply)

    # Add the assistant's reply to the history for the next turn
    msg.append({"role": "assistant", "content": ai_reply})

    # Optional debugging: print the stored conversation history
    # print()
    # print("******Conversation history start****************\n")

    # for message in msg:
    #     print(message)
    #     print()  # blank line after every message

    # print("******Conversation history end****************\n")
    # print()
    # print("******Conversation history clean way****************\n")

    # for message in msg:
    #     print(f"{message['role'].title()}:{message['content']}")
    #     print()  # blank line after every message

    # print("******Conversation history clean way end****************\n")

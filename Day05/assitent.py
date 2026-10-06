"""Day 05 - Assistant that can read files.

Purpose: adds file commands on top of Day 04. Files are read from the
data/ folder and sent to Claude inside the prompt.

Commands:
    summarize <file>           Summarize a file, e.g. summarize notes.txt
    explain <file>             Send a file to Claude (uses the same prompt as summarize)
    ask <file> <question>      Answer a question using only that file
    time / dice / password     Handled locally by the tools
    quit                       Exit

How to run (from inside the Day05 folder, so data/ is found):
    python assitent.py
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
    # Save the user's message

    text = user_input.lower()

    # Command: "summarize <file>" -> summarize a file from the data/ folder
    if text.startswith("summarize "):
        # Everything after "summarize " is the file name
        filename = user_input[10:].strip()
        file_content = read_text_file("data/" + filename)

        # Put the file content inside the prompt so Claude can read it
        prompt = f"""
        Summarize the following document.

        Document:

        {file_content}
        """

        response = client.messages.create(
            model="claude-sonnet-5-5",
            max_tokens=500,
            system="You are a helpful assistant.",
            messages=[{"role": "user", "content": prompt}],
        )
        print(response.content[0].text)
        continue

    # Command: "explain <file>" -> send a file from data/ to Claude
    # (the prompt still says "Summarize"; it was copied from the command above)
    if text.startswith("explain "):
        # Everything after "explain " is the file name
        filename = user_input[8:].strip()
        print("filename =", filename)
        file_content = read_text_file("data/" + filename)

        prompt = f"""
            Summarize the following document.
    
            Document:
    
            {file_content}
            """
        # Print the final prompt for debugging
        print(prompt)

        response = client.messages.create(
            model="claude-sonnet-5-5",
            max_tokens=500,
            system="You are a helpful assistant.",
            messages=[{"role": "user", "content": prompt}],
        )
        print(response.content[0].text)
        continue

    # Command: "ask <file> <question>" -> answer a question using only that file
    if text.startswith("ask"):
        # Split into 3 parts: the word "ask", the file name, and the question
        parts = user_input.split(maxsplit=2)
        # print(parts)
        filename = parts[1]
        question = parts[2]

        file_content = read_text_file("data/" + filename)

        # The prompt tells Claude to answer only from the document
        prompt = f"""
You are given a document.

Answer the user's question using
only the information present
in the document.

If the answer is not available,
say:
'I couldn't find that information
in the document.'

Document:

{file_content}

Question:

{question}
"""

        response = client.messages.create(
            model="claude-sonnet-5-5",
            max_tokens=500,
            system="You are a helpful assistant.",
            messages=[
                {"role": "user", "content": prompt},
            ],
        )

        print(response.content[0].text)
        continue

    # Try the local tools (time, dice, password); skip the API call if one matches
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

    msg.append({"role": "user", "content": user_input})

    # Normal chat: send the full history with the chosen role's system prompt
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

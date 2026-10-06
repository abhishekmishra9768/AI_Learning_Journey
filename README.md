# AI Learning Journey: Building a Claude Assistant, Day 01 to Day 06

A step-by-step learning project. It starts with a single API call to Claude and
grows, one day at a time, into a terminal assistant with memory, roles, local
tools, file reading and a small RAG (Retrieval Augmented Generation) pipeline.

Each day adds one idea on top of the previous one, and every file starts with a
short description and run instructions.

## What you will find here

| Day | Topic | What it adds | Main files |
|-----|-------|--------------|------------|
| 01 | First API call | Send a prompt to Claude and print the answer; a simple chat loop | `hello_ai.py`, `assitent.py` |
| 02 | Conversation memory | Keep the message history and send it with every request | `conersation_loop.py` |
| 03 | Roles | Use a system prompt to make Claude act as a teacher, travel guide or coach | `assitent.py` |
| 04 | Local tools | Answer time, dice and password requests in Python, without calling the API | `assitent.py`, `tools.py`, `tools_manager.py` |
| 05 | Reading files | `summarize`, `explain` and `ask` commands that put a file's text into the prompt | `assitent.py`, `tools.py` |
| 06 | RAG | Embed documents, find the one closest to the question, give it to Claude as context | `rag.py`, `embeddings_rag.py`, `similart.py`, `retriever.py` |

## Project structure

```
AI/
├── Day01/   hello_ai.py, assitent.py
├── Day02/   conersation_loop.py
├── Day03/   assitent.py
├── Day04/   assitent.py, tools.py, tools_manager.py, test_tools.py, test_tools_manager.py
├── Day05/   assitent.py, tools.py, tools_manager.py, test_file.py, data/
├── Day06/   rag.py, embeddings_rag.py, similart.py, retriever.py, test_retriever.py, knowledge/
├── README.md
└── .gitignore
```

## Requirements

- Python 3.9 or newer
- An Anthropic API key (Days 01 to 06 use it for the chat replies)
- Day 06 also needs `sentence-transformers`. The embedding model runs on your own
  machine and does not need an API key. It is downloaded from HuggingFace the first
  time it is used.

## Setup

```powershell
# 1. Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Install the packages
pip install anthropic
pip install sentence-transformers      # only needed for Day 06

# 3. Set your API key (then close and reopen the terminal)
setx ANTHROPIC_API_KEY "your-api-key"
```

On macOS or Linux, activate with `source .venv/bin/activate` and set the key with
`export ANTHROPIC_API_KEY="your-api-key"`.

Never commit your API key. The `.gitignore` already excludes `.venv/`,
`__pycache__/` and `.env`.

## How to run

Run each program from inside its own Day folder, because the Day 05 and Day 06
programs look for the `data/` and `knowledge/` folders relative to where they start.

```powershell
cd Day05
python assitent.py
```

Type `quit` to leave any chat loop.

## Day by day

### Day 01: Hello, Claude
`hello_ai.py` sends one question and prints the reply. `assitent.py` wraps that in a
loop so you can keep asking questions. Each question is independent, so the assistant
does not remember what you said before.

### Day 02: Conversation memory
The model has no memory between requests. `conersation_loop.py` stores every user and
assistant message in a list and sends the whole list each time, which is how the
assistant can follow the conversation.

### Day 03: Roles with system prompts
You choose a role at the start (English Teacher, Travel Guide or Motivational Coach).
The role's text is sent as the `system` prompt, which changes the tone and behaviour of
every answer.

### Day 04: Local tools
Some questions do not need an AI model. `tools_manager.execute_tool()` checks the
input first:

| You type something containing | Result |
|-------------------------------|--------|
| `time` or `clock` | Current date and time |
| `dice` or `die` | A random number from 1 to 6 |
| `password` | A random 12-character password |

If a tool matches, the answer comes from Python and no API call is made. Otherwise the
message goes to Claude as usual.

### Day 05: Working with files
Text files in `Day05/data/` can be sent to Claude inside the prompt:

| Command | What it does |
|---------|--------------|
| `summarize notes.txt` | Summarize the file |
| `explain project.txt` | Send the file to Claude (it currently uses the same prompt as `summarize`) |
| `ask project.txt What is the project duration?` | Answer using only the information in that file |

The `ask` prompt tells Claude to say it could not find the information when the answer
is not in the document.

### Day 06: RAG (Retrieval Augmented Generation)
Instead of choosing the file yourself, the program chooses it for you:

1. `retriever.load_documents()` reads every `.txt` file in `knowledge/`.
2. `embeddings_rag.create_embedding()` turns each document into a vector using the
   local `nomic-ai/nomic-embed-text-v1.5` model.
3. Your question is turned into a vector the same way.
4. `similart.cosine_similarity()` scores the question against every document, and the
   best match is picked.
5. That document is sent to Claude as context, and Claude answers from it.

`retriever.retrieve()` is a plain keyword search, kept as a simple comparison with the
embedding approach.

Current limits: the whole document is used as context (no chunking), only the single
best document is used, and the document embeddings are recomputed on every start.

## Testing the small pieces

These scripts check individual parts without the chat loop:

```powershell
cd Day04
python test_tools.py
python test_tools_manager.py

cd ..\Day06
python test_retriever.py
```

## What I learned

- How the Messages API works: roles, `max_tokens` and response blocks.
- Why conversation memory is something your own code has to provide.
- How system prompts change the behaviour of a model.
- When a plain Python function is a better choice than a model call.
- How to put documents into a prompt, and how embeddings and cosine similarity pick the
  right document automatically.

## Next ideas

- Split long documents into chunks and retrieve the top few instead of one file.
- Save the embeddings so they are not recomputed on every run.
- Let Claude decide when to call a tool (tool use / function calling).

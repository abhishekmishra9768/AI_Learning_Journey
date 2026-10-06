# AI Learning Journey (Day 01 - Day 06)

Small Python projects that build a terminal AI assistant step by step using the
Anthropic (Claude) API.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install anthropic
setx ANTHROPIC_API_KEY "your-api-key"   # then reopen the terminal
```

Never commit your API key. Day 06 also needs `pip install sentence-transformers`.

## Days

| Day | Topic | Main file |
|-----|-------|-----------|
| 01 | Send a question to Claude; simple chat loop | `Day01/hello_ai.py`, `Day01/assitent.py` |
| 02 | Conversation memory (send the full history) | `Day02/conersation_loop.py` |
| 03 | Roles using system prompts | `Day03/assitent.py` |
| 04 | Local tools (time, dice, password) | `Day04/assitent.py`, `tools.py`, `tools_manager.py` |
| 05 | Read files: `summarize`, `explain`, `ask` | `Day05/assitent.py` |
| 06 | RAG: embeddings + similarity search over `knowledge/` | `Day06/rag.py` |

Each file starts with a short description and run instructions. Run the files
from inside their own Day folder, for example:

```powershell
cd Day05
python assitent.py
```

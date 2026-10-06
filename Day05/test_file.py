"""Day 05 - Manual test for the file helpers in tools.py.

How to run (from inside the Day05 folder):
    python test_file.py
"""

from tools import *

# Read an existing file
text = read_text_file("data/notes.txt")
print()
print(text)
print()




# "note.txt" does not exist (the real file is notes.txt),
# so this prints "File not found" and shows the error handling
text = read_file("data/note.txt")
print()
print(text)
print()

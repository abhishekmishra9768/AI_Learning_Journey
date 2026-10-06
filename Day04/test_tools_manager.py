"""Day 04 - Manual test for tools_manager.py.

How to run:
    python test_tools_manager.py
It prints the result of execute_tool() for four sample inputs.
"""

from tools_manager import execute_tool

# Each of the first three inputs should trigger a tool
print(execute_tool("What time is it?"))

print(execute_tool("Roll a dice"))

print(execute_tool("Generate a password"))

# No tool matches this one, so the result should be None
print(execute_tool("Explain Python"))

"""Day 04 - Tool router.

Purpose: execute_tool() looks at the user's text, runs the matching tool
from tools.py and returns the result (or None if no tool matches).
"""

from tools import *


def execute_tool(user_input):
    """Run a tool if the user's text mentions one; otherwise return None."""
    text = user_input.lower()

    # Time tool
    if "time" in text or "clock" in text:
        return get_current_time()

    # Dice tool
    if "dice" in text or "die" in text:
        return "You roolled : " +str(roll_dice())

    # Password tool
    if "password" in text:
        return generate_password()

    # No tool matched, so the caller should send the text to the model
    return None

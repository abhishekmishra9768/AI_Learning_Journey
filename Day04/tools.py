"""Day 04 - Tool functions.

Purpose: plain Python functions the assistant can use instead of the model:
get_current_time(), roll_dice() and generate_password().
"""

from datetime import datetime


def get_current_time():
    """Return the current date and time."""

    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")


import random


def roll_dice():
    """Return a random number between 1 and 6."""

    return random.randint(1, 6)


import secrets
import string


def generate_password(length=12):
    """Generate a secure random password."""

    # Letters, digits and punctuation are all allowed in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    # Pick one random character at a time using a cryptographically secure source
    for _ in range(length):
        password += secrets.choice(characters)

    return password

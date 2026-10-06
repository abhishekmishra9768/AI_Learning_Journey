"""Day 05 - Tool functions.

Purpose: Day 04 tools plus two file helpers:
read_text_file() raises an error if the file is missing, and
read_file() returns "File not found" instead.
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

def read_text_file(filename):
    """Read and return the full text of a file (raises an error if it is missing)."""
    with open(filename,"r") as file:
     content = file.read()
     return content

def read_file(filename):
    """Read and return a file's text, or "File not found" if it does not exist."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"

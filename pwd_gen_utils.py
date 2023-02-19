import random
import string
import pyperclip

"""
Remember to install the pyperclip module
pip install pyperclip
"""

def generate_password(length: int, characters: str) -> str:
    # generate a password using the random module with the needs of the user
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_settings(upperl: str, lowerl: str, nums: str, symbols: str) -> str:
    characters = ""

    if upperl == "y":
        characters += string.ascii_uppercase
    if lowerl == "y":
        characters += string.ascii_lowercase
    if nums == "y":
        characters += string.digits
    if symbols == "y":
        characters += string.punctuation
    
    return characters

def copy_to_clipboard(password: str):
    pyperclip.copy(password)
    print("\nPassword copied to clipboard.\n")
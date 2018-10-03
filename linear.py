import sys

from cs50 import get_string

# Names in a phone book

book = [
    "chen",
    "Kernighan",
    "Leitner",
    "Lewis",
    "Malan",
    "Smith",
    "Charwin",
    "Johnston",
    "Seltzer",]

# Prompt user for name
name = get_string("Name: ")
if name in book:
    print(f"Calling {name}")
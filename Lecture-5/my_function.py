import os
from rich import print

def greet(name: str):
    print("[bold Blue]Hello",name)
    return greet

greet("Vanya")

def change_name(name: str):
    print("Artem hero")
    return change_name

change_name("aa")

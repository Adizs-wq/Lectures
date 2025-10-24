import os
from rich import print

def greet(name: str):
    print("[bold Blue]Hello",name)
    return greet

greet("[bold Blue]Vanya")

def change_name(name: str):
    print("Artem pidoras")
    return change_name

change_name("aa")

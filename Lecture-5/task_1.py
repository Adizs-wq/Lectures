from rich import print

def change_name(name):
    result = ""
    for i in range(len(name)):
        if i % 2 == 1:
            result += name[i].upper()
        else:
            result += name[i].lower()
    return result
print(change_name("Aleksey"))

def greet(name: str):
    print("[bold Blue]Hello",name)
    return greet

greet("Vanya")
from rich import print as rich_print

rich_print("[bold blue]Hi my dear friend")
rich_print("Today we want to see film named [bold red]Deadpool[/bold red]")
decision: str = input("Wanna go? [yea/no]: ")

print(decision.capitalize())
print(decision)

if decision == "yea":
    print("Fillip Kirkorov")
elif decision == "no":
    print("0_0")
else:
    print("@_@")
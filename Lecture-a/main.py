import os
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

load_dotenv("key.env")
api_key = os.getenv("API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

console = Console()

memories = [
    {"role": "system",
     "content": "Ты помощник, всегда готовый всё объяснить."},
]

def respond_to_user(user_input):
    memories.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=memories
    )
    assistant_message = response.choices[0].message.content
    memories.append
    ({
            "role": "assistant",
            "content": assistant_message
    })
    return assistant_message

def letsbegin():
    console.print(Panel(
        "[bold green]Приветствую![/bold green]"
        "Commands: /exit to quit, /clear to clear history. If the message begins with /system, then it is a system message.",
        title="Чат с моделькой",
        subtitle="Стартуем!"
        ))
    
    while True:
        
        user_input = console.input("[bold blue]Вы:[/bold blue] ")
        print(user_input)
        
        if user_input.lower() == "/exit":
            console.print("[bold red]Выход из чата. Пока![/bold red]")
            break
        
        elif user_input.lower() == "/clear":
            uno = memories[0]
            memories.clear()
            memories.append(uno)
            console.print("[bold yellow]История очищена.[/bold yellow]")
            continue
        
        #role change
        elif user_input.lower().startswith("/system"):
            system_message = user_input[len("/system"):].strip()
            memories.append({"role": "system", "content": system_message})
            console.print("[bold magenta]Роль изменена.[/bold magenta]")
            continue
        
        memories.append({"role": "user", "content": user_input})
        assistant_message = respond_to_user(user_input)
        
        md = Markdown(assistant_message)
        console.print(Panel(md, title="[bold green]MODELKA HAS SPOKEN...:[/bold green]"))

import json

from rich.console import Console

console = Console()


def show_tool_call(item) -> None:
    console.print(f"\n[cyan]🔧 {item.raw_item.name}[/cyan]")

    args = json.loads(item.raw_item.arguments)

    for key, value in args.items():
        console.print(f"   [yellow]{key}[/yellow] = {value}")


def show_tool_result() -> None:
    console.print("[green]✓ completed[/green]\n")

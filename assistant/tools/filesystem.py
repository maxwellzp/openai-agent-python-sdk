from agents import function_tool
from pathlib import Path


@function_tool
def list_directory(path: str) -> str:
    """Return names of files and directories."""
    try:
        return sorted([p.name for p in Path(path).iterdir()])
    except Exception as e:
        return f"Error during reading a file or a directory."


@function_tool
def read_file(path: str) -> str:
    """Read a UTF-8 text file."""
    try:
        return Path(path).read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return f"Error during reading a file: {e}"


@function_tool
def search_text(path: str, query: str) -> list[str]:
    """Search for a text in a text file."""
    results = []

    file = Path(path)

    try:
        with file.open(encoding="utf-8", errors="replace") as f:
            for line_number, line in enumerate(f, start=1):
                if query.lower() in line.lower():
                    results.append(f"{line_number}: {line.rstrip()}")
    except Exception as e:
        return [f"Error: {e}"]

    return results


@function_tool
def write_file(path: str, text: str) -> str:
    """Write a text string to a text file."""
    try:
        Path(path).write_text(text, encoding="utf-8")
        return "File written successfully."
    except Exception as e:
        return f"Error: {e}"


TOOLS = [
    read_file,
    write_file,
    search_text,
]

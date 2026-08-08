# OpenAI Agent Python SDK — Developer Assistant

A small CLI developer assistant built with the **OpenAI Agents SDK**.

The project is a learning-oriented implementation of an AI coding/developer assistant with streaming responses, persistent conversation history, local tools, automated tests, and code quality checks.

## Prerequisites

- Python 3.12+
- An OpenAI API key
- Git

## Installation

Clone the repository and enter the project directory

```bash
git clone git@github.com:maxwellzp/openai-agent-python-sdk.git
cd maxwellzp/openai-agent-python-sdk
```

Create a virtual environment and activate it

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project in editable mode:

```bash
pip install -e .
```

For development dependencies:

```bash
pip install -e ".[dev]"
```

Export your OpenAI API key in the shell:

```bash
export OPENAI_API_KEY="your_api_key"
```

## Usage

Start the application with:

```bash
python3 main.py
```

You should see:

```text
>
```

Enter a request:

```text
> Create a new file called 'log.txt' with a text message 'Line #1'.
```

The assistant responds using streaming output.

To exit:

```text
> exit
```

or:

```text
> quit
```

## Testing

Run the complete test suite:

```bash
pytest -v
```

## Code Quality

Run Ruff:

```bash
ruff check .
```

Automatically fix supported issues:

```bash
ruff check . --fix
```

The project uses Ruff rules configured in `pyproject.toml`.

## License

MIT

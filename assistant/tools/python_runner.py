from agents import function_tool
import os
import subprocess
import tempfile
from assistant.config import WORKSPACE
from assistant.config import PYTHON_TIMEOUT


@function_tool
def run_python(script: str) -> str:
    """
    Execute a Python script and return stdout/stderr.
    """

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".py",
        delete=False,
        encoding="utf-8",
    ) as f:
        f.write(script)
        filename = f.name

    try:
        result = subprocess.run(
            ["python3", filename],
            cwd=WORKSPACE,
            capture_output=True,
            text=True,
            timeout=PYTHON_TIMEOUT,
        )

        output = ""

        if result.stdout:
            output += f"STDOUT:\n{result.stdout}"

        if result.stderr:
            output += f"\nSTDERR:\n{result.stderr}"

        return output.strip()
    except subprocess.TimeoutExpired:
        return "Execution timed out after 10 seconds."
    finally:
        os.remove(filename)


TOOLS = [
    run_python,
]

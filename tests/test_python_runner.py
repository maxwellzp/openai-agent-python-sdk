from assistant.tools.python_runner import run_python


def test_run_python_stdout():
    result = run_python('print("Hello!")')

    assert result == "STDOUT:\nHello!"


def test_run_python_calculation():
    result = run_python("print(2 + 3)")

    assert result == "STDOUT:\n5"


def test_run_python_stderr():
    script = """
import sys

print("Something went wrong", file=sys.stderr)
"""

    result = run_python(script)

    assert "STDERR:" in result
    assert "Something went wrong" in result


def test_run_python_exception():
    script = """
raise ValueError("test error")
"""

    result = run_python(script)

    assert "STDERR:" in result
    assert "ValueError: test error" in result


def test_run_python_timeout():
    script = """
import time

time.sleep(11)
"""

    result = run_python(script)

    assert result == "Execution timed out after 10 seconds."

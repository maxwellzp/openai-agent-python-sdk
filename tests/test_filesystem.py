from pathlib import Path

from assistant.tools.filesystem import (
    read_file,
    search_text,
    write_file,
)


def test_read_file(tmp_path: Path):
    file = tmp_path / "hello.txt"
    file.write_text("Hello!", encoding="utf-8")

    result = read_file(str(file))

    assert result == "Hello!"


def test_read_file_not_found(tmp_path: Path):
    file = tmp_path / "missing.txt"

    result = read_file(str(file))

    assert result.startswith("Error during reading a file:")


def test_write_file(tmp_path: Path):
    file = tmp_path / "hello.txt"

    result = write_file(str(file), "Hello!")

    assert result == "File written successfully."
    assert file.read_text(encoding="utf-8") == "Hello!"


def test_search_text(tmp_path: Path):
    file = tmp_path / "hello.txt"
    file.write_text(
        "Hello\n" "Python\n" "Hello again\n",
        encoding="utf-8",
    )

    result = search_text(str(file), "hello")

    assert result == [
        "1: Hello",
        "3: Hello again",
    ]


def test_search_text_not_found(tmp_path: Path):
    file = tmp_path / "hello.txt"
    file.write_text("Hello\nPython\n", encoding="utf-8")

    result = search_text(str(file), "Java")

    assert result == []

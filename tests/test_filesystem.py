from pathlib import Path

from assistant.tools.filesystem import read_file


def test_read_file(tmp_path: Path):
    file = tmp_path / "hello.txt"
    file.write_text("Hello!", encoding="utf-8")

    result = read_file(str(file))

    assert result == "Hello!"

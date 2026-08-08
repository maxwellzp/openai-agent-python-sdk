import platform

from assistant.tools.system import get_os_info


def test_get_os_info():
    result = get_os_info()

    assert isinstance(result, dict)

    assert result["system"] == platform.system()
    assert result["release"] == platform.release()
    assert result["version"] == platform.version()
    assert result["machine"] == platform.machine()
    assert result["python"] == platform.python_version()

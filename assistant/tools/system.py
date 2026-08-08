import platform

from agents import function_tool


def get_os_info() -> dict[str, str]:
    """Returns system info including os, version, release, machine, version of python"""
    return {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "python": platform.python_version(),
    }


TOOLS = [
    function_tool(get_os_info),
]

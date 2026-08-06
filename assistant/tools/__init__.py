from .filesystem import TOOLS as filesystem_tools
from .python_runner import TOOLS as python_tools
from .system import TOOLS as system_tools


def load_tools():
    return [
        filesystem_tools,
        python_tools,
        system_tools,
    ]

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

WORKSPACE = Path(os.getenv("WORKSPACE", "workspace"))
WORKSPACE.mkdir(exist_ok=True)

MODEL = os.getenv("OPENAI_MODEL", "gpt-5-mini")

PYTHON_TIMEOUT = int(os.getenv("PYTHON_TIMEOUT", "10"))

SESSION_ID = os.getenv("SESSION_ID", "default")

DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    "data/conversations.db",
)

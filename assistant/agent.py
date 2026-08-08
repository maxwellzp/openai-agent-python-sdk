from agents import Agent

from assistant.prompts import SYSTEM_PROMPT
from assistant.tools import load_tools


def create_agent() -> Agent:
    return Agent(
        name="Developer Assistant",
        instructions=SYSTEM_PROMPT,
        tools=load_tools(),
    )

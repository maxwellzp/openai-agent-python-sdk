from agents import Agent, Runner

from assistant.prompts import SYSTEM_PROMPT
from assistant.tools import load_tools

agent = Agent(
    name="Developer Assistant",
    instructions=SYSTEM_PROMPT,
    tools=load_tools(),
)

while True:
    prompt = input("> ")

    if prompt.lower() in {"exit", "quit"}:
        break

    result = Runner.run_sync(agent, prompt)

    print(result.final_output)

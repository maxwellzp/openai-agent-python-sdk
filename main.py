import asyncio

from agents import Agent, Runner

from assistant.prompts import SYSTEM_PROMPT
from assistant.streaming import handle_stream_event
from assistant.tools import load_tools

agent = Agent(
    name="Developer Assistant",
    instructions=SYSTEM_PROMPT,
    tools=load_tools(),
)


async def main() -> None:
    while True:
        prompt = input("> ")

        if prompt.lower() in {"exit", "quit"}:
            break

        stream = Runner.run_streamed(
            agent,
            prompt,
        )

        async for event in stream.stream_events():
            handle_stream_event(event)

        print()


if __name__ == "__main__":
    asyncio.run(main())

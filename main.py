import asyncio

from agents import Agent, Runner
from openai.types.responses import ResponseTextDeltaEvent

from assistant.prompts import SYSTEM_PROMPT
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
            if event.type == "raw_response_event" and isinstance(
                event.data, ResponseTextDeltaEvent
            ):
                print(event.data.delta, end="", flush=True)

        print()


if __name__ == "__main__":
    asyncio.run(main())

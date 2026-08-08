from agents import Runner

from assistant.agent import create_agent
from assistant.session import create_session
from assistant.streaming import handle_stream_event


async def run_cli() -> None:
    agent = create_agent()
    session = create_session()
    while True:
        prompt = input("> ")

        if prompt.lower() in {"exit", "quit"}:
            break

        stream = Runner.run_streamed(
            agent,
            prompt,
            session=session,
        )

        async for event in stream.stream_events():
            handle_stream_event(event)

        print()

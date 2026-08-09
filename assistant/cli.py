from agents import Runner

from assistant.agent import create_agent
from assistant.logger import logger
from assistant.session import create_session
from assistant.streaming import handle_stream_event


async def run_cli() -> None:
    logger.info("Starting Developer Assistant")

    agent = create_agent()
    session = create_session()

    while True:
        prompt = input("> ")

        if prompt.lower() in {"exit", "quit"}:
            logger.info("Stopping Developer Assistant")
            break

        logger.info("Processing user request")

        try:
            stream = Runner.run_streamed(
                agent,
                prompt,
                session=session,
            )

            async for event in stream.stream_events():
                handle_stream_event(event)

        except Exception:
            logger.exception("Error while running agent")

        print()

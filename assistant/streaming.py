from agents.items import ToolCallItem, ToolCallOutputItem
from openai.types.responses import ResponseTextDeltaEvent

from assistant.ui import show_tool_call, show_tool_result


def handle_stream_event(event) -> None:
    """Pretty-print streaming events from the Agents SDK."""

    if event.type == "raw_response_event" and isinstance(
        event.data, ResponseTextDeltaEvent
    ):
        print(event.data.delta, end="", flush=True)

    elif event.type == "run_item_stream_event":
        if isinstance(event.item, ToolCallItem):
            show_tool_call(event.item)
        elif isinstance(event.item, ToolCallOutputItem):
            show_tool_result()

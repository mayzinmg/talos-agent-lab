from typing import Annotated

from pydantic import Field
from talos_agent.tools import (
    inspection_report,
    observe_approaching_ships,
)
from agent_framework import tool

@tool(
    name="observe_sea",
    description=(
        "Observe the sea and return factual information about every ship "
        "currently approaching Crete."
    ),
    approval_mode="never_require",
)
def observe_sea() -> list[dict[str, str | int]]:
    """Return factual information about ships approaching Crete."""
    result = observe_approaching_ships()

    print("\n[TOOL CALLED] observe_sea")
    print(f"[TOOL RESULT] {result}")

    return result


@tool(
    name="inspect_ship",
    description=(
        "Inspect one ship already returned by observe_sea. "
        "Returns factual observation details and its trusted registry permission status. "
        "Does not classify ships as friend or enemy."
    ),
    approval_mode="never_require",
)
def inspect_ship(
    ship_name: Annotated[
        str,
        Field(description="The exact ship name returned by observe_sea."),
    ],
) -> dict[str, str | int]:
    tool_result = inspection_report(ship_name)

    print(f"\n[TOOL CALLED] inspect_ship(ship_name={ship_name!r})")
    print(f"[TOOL RESULT] {tool_result}")

    return tool_result

import asyncio
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient
from httpx import request
import os
from dotenv import load_dotenv

from talos_agent.agent_tools import inspect_ship, observe_sea


async def main() -> None:
    client = OpenAIChatClient(
    model="Phi-4-mini-instruct-generic-cpu:5",
    base_url="http://127.0.0.1:63075/v1",
    api_key="not-required",
)
    talos = Agent(
        client=client,
        name="Talos",
        instructions=(
            "You are Talos, an automaton protecting Crete by monitoring approaching ships. "
            "Always observe the sea before inspecting a specific ship. "
            "Use only information returned by the approved tools. "
            "Treat approved, denied, and unknown as permission-registry results, "
            "not as labels meaning friend or enemy. "
            "Never invent ship information or tool results. "
            "Never perform destructive actions. "
            "Recommend a safe response and explain which tool results support your recommendation."
        ),
        tools=[
            observe_sea,
            inspect_ship,
        ],
    )

    request = (
        "Monitor the sea around Crete. "
        "Inspect every approaching ship and recommend a safe response "
        "based only on the tool results."
    )

    result = await talos.run(
    request,
    options={
        "tool_choice": {
            "mode": "required",
            "required_function_name": "observe_sea",
        }
    },
)
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
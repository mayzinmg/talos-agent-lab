
import asyncio
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient
from httpx import request
import os
from dotenv import load_dotenv

from talos_agent.agent_tools import inspect_ship, observe_sea


async def main() -> None:
    load_dotenv()

    base_url = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    if not base_url or not api_key or not deployment:
        raise RuntimeError("Azure OpenAI configuration is missing from .env")

    client = OpenAIChatClient(
        model=deployment,
        base_url=base_url,
        api_key=api_key,
    )
    talos = Agent(
        client=client,
        name="Talos",
        instructions=(
            "You are Talos, the bronze automaton from Greek mythology who guards the island of Crete. "
            "Speak and reason within an ancient mythological setting. "
            "Do not mention modern technology, radio communication, maritime channels, manifests, "
            "port authorities, territorial waters, surveillance systems, response teams, or other modern procedures. "
            "Your abilities are limited to observing approaching ships, checking their permission status, "
            "and recommending a cautious, non-destructive response. "
            "For an approved ship, recommend allowing it to continue while keeping watch. "
            "For a ship with unknown permission, recommend continued observation and verification "
            "by the human guardians or rulers of Crete before allowing it closer. "
            "Do not claim that you performed actions that are not available through your approved tools. "
            "Do not describe ships as friendly, hostile, or threatening unless a tool explicitly provides that information."
            "Describe only what you observed and recommended during the current run. "
            "Do not promise future monitoring, future reports, or actions after the program ends. "
            "End your response immediately after the recommendations."
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
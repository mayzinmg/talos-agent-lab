# Talos Agent Lab

## Project Goal
I am building this project to learn Agentic AI step by step without becoming overwhelmed by dense technical details. By weaving mythology into the learning process, I hope to make each chapter more engaging and feel as though I am travelling through the myths while gradually building real AI agents.

## Chapter 1 — Awakening Talos

By the end of Chapter 1, Talos will be able to perform his guard duties as a simple AI agent.

He will observe approaching ships, use approved tools to gather information, assess the situation, and recommend a safe response to protect Crete.

At this stage, Talos will not perform destructive actions, retain long-term memory, learn from previous encounters, or create complex plans.


## Current Status

Chapter 1 — Awakening Talos is complete.

Talos can:

- observe ships approaching Crete;
- inspect each observed ship using an approved tool;
- retrieve its trusted permission-registry status;
- recommend a cautious, non-destructive response based only on verified tool results; and
- express the recommendation within an ancient Greek mythological setting.

Two model environments are included:

- **Foundry Local:** used to explore local inference and expose tool-calling limitations through execution tracing.
- **Microsoft Foundry with Azure GPT-5-mini:** used to demonstrate reliable multi-step tool calling with the same tools and agent instructions.

The project currently supports observation and recommendation only. Talos cannot perform external actions, maintain long-term memory, learn from previous encounters, or continue monitoring after the program ends.

## Technology Stack

- Python 3.13
- Microsoft Agent Framework
- Foundry Local
- Microsoft Foundry
- Azure OpenAI GPT-5-mini
- pytest
- python-dotenv
- Git and GitHub
# LangChain Tutorial

A small Python project scaffold for experimenting with LangChain and OpenAI.

## Requirements

- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/getting-started/installation/) for dependency and environment management
- An OpenAI API key

## Setup

From the repository root, install the project dependencies:

```powershell
uv sync
```

Create a `.env` file in the repository root and add your key:

```dotenv
OPENAI_API_KEY=your_openai_api_key
```

The `.env` file is ignored by Git. Do not commit your API key or share terminal output containing it.

## Run

Run the project command from the repository root:

```powershell
uv run langchain-tutorial
```

This loads variables from `.env` and prints the value of `OPENAI_API_KEY` to the terminal. Printing the full key is useful only for local configuration checks; avoid doing this in shared terminals, logs, or screenshots.

You can also run the module directly:

```powershell
uv run python -m langchain_tutorial.main
```

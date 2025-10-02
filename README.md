# Anthropic Agent SDK - Quick Getting Started - Python

A quick start tutorial project demonstrating how to use the Anthropic Claude Agent SDK to build interactive AI agents with custom tools and conversational interfaces.

## Project Files

- **`main.py`** - Main entry point that loads environment variables and runs the agent with tools
- **`basic_query.py`** - Simple examples for making basic queries to the Claude API
- **`agent_with_tools.py`** - Interactive chat loop with custom tools (calculator) and MCP server integration
- **`interactive_terminal.py`** - Two chat loop implementations:
  - `start_chat_loop()` - Chat without history
  - `start_chat_loop_continuous()` - Chat with conversation history
- **`.env.local`** - Local environment variables (not tracked in git)
- **`.env.example`** - Template for environment variables

## Setup Guide

### 1. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install claude-agent-sdk python-dotenv numexpr anyio
```

### 3. Get Your API Key

1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key

### 4. Configure Environment

Copy the example environment file:

```bash
# Windows
copy .env.example .env.local

# macOS/Linux
cp .env.example .env.local
```

Edit `.env.local` and add your API key:

```
ANTHROPIC_API_KEY=your_actual_api_key_here
```

### 5. Run the Project

```bash
python main.py
```

## Usage Examples

The current `main.py` runs the agent with tools demo. You can modify it to run different examples:

```python
# For basic query
anyio.run(basic_query)

# For interactive chat without history
anyio.run(start_chat_loop)

# For interactive chat with history
anyio.run(start_chat_loop_continuous)

# For agent with custom tools (default)
anyio.run(start_chat_tools)
```

## Features

- Basic Claude API queries
- Interactive terminal chat interface
- Conversation history management
- Custom tool integration (calculator example)
- MCP (Model Context Protocol) server support
- Permission modes for tool usage

## Notes

- Type `exit` or `quit` to end any chat session
- The calculator tool uses numexpr for safe expression evaluation
- Default model: `claude-sonnet-4-5-20250929`

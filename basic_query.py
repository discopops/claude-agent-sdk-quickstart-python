from claude_agent_sdk import query, AssistantMessage, TextBlock, ClaudeAgentOptions


async def basic_query():
    options = ClaudeAgentOptions(system_prompt="You are helpful assistant. You speak latin and show your working", max_turns=1, model="claude-sonnet-4-5-20250929")

    async for message in query(prompt="calculate 2+2", options=options):
        # Extract model message
        if isinstance(message, AssistantMessage):  # Check for an assistant message
            for block in message.content:
                if isinstance(block, TextBlock):  # Check for text block
                    print(message.content[0].text)


async def basic_query_ext(system_message:str, input_message:str):

    options = ClaudeAgentOptions(system_prompt=system_message, max_turns=1, model="claude-sonnet-4-5-20250929")

    async for message in query(prompt=input_message, options=options):
        # Extract model message
        if isinstance(message, AssistantMessage):  # Check for an assistant message
            for block in message.content:
                if isinstance(block, TextBlock):  # Check for text block
                    print(message.content[0].text)
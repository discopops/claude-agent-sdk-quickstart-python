
from typing import Any

from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, AssistantMessage, TextBlock, tool, \
    create_sdk_mcp_server, ToolUseBlock, ResultMessage, UserMessage, ToolResultBlock
import numexpr as ne

async def start_chat_tools():
    print("Welcome to the latest claude agent sdk")
    print("type exit to leave or chat with the claude agent")

    @tool(name="calculator",
          description="Evaluate an expression using our calculator. The calculator evaluates numexpr expressions eg. 0.5 * 70 * 25**2",
          input_schema={"expression": str})
    async def calculator(args: dict[str, Any]) -> dict[str, Any]:
        try:
            # read data
            expression = args.get("expression")

            # process (service)
            result = ne.evaluate(expression)

            # return
            return {
                "content": [{"type": "text", "text": f"{result}"}]
            }
        except Exception as e:
            return {
                "content": [{"type": "text", "text": f" Error: {e}"}]
            }

    tools_mcp = create_sdk_mcp_server(name="General tools", version="2.0.0", tools=[calculator])

    system_message = "You are a helpful assistant"
    allowed_tools = ["Read", "Write", "Bash", "mcp__extra_tools__calculator"]

    options = ClaudeAgentOptions(system_prompt=system_message, mcp_servers={"extra_tools": tools_mcp},
                                 allowed_tools=allowed_tools, permission_mode="acceptEdits")

    async with ClaudeSDKClient(options=options) as client:
        while True:
            try:
                user_input = input(">>>").strip()

                if user_input.lower() in ['exit', 'quit']:
                    print("Goodbye!")
                    break
                elif user_input:
                    # send message to the model
                    await client.query(prompt=user_input)
                    async for message in client.receive_response():

                        if isinstance(message, UserMessage):
                            for block in message.content:
                                if isinstance(block, TextBlock):  # show user messages
                                    print(f"User: {block.text}")
                                elif isinstance(block, ToolResultBlock):  # show tool results
                                    print(
                                        f"Tool Result: {block.content[:100] if block.content else 'None'}..."
                                    )

                        elif isinstance(message, AssistantMessage):
                            for block in message.content:

                                if isinstance(block, ToolUseBlock):
                                    print(f"Using tool: {block.name}")
                                    if block.input:
                                        print(f"  Input: {block.input}")

                                elif isinstance(block, TextBlock):  # If the model is responding in text
                                    print(f"Claude: {block.text}")





            except KeyboardInterrupt:

                print("\nGoodbye!")

                break

            except EOFError:

                break

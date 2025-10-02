from claude_agent_sdk import ClaudeSDKClient, AssistantMessage, TextBlock, ClaudeAgentOptions

from basic_query import basic_query_ext
from typing import List, Dict, Any






async def start_chat_loop(): # Has no chat history
    print("Welcome to the latest claude agent sdk")
    print("type exit to leave or chat with the claude agent")
    system_message = "You are a helpful assistant"

    while True:
        try:
            user_input = input(">>>").strip()

            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            elif user_input:
                # send message to the model
                await basic_query_ext(system_message=system_message, input_message=user_input)


        except KeyboardInterrupt:

            print("\nGoodbye!")

            break

        except EOFError:

            break


async def start_chat_loop_continuous(): #Maintains chat history
    print("Welcome to the latest claude agent sdk")
    print("type exit to leave or chat with the claude agent")
    system_message = "You are a helpful assistant"
    async with ClaudeSDKClient(options=ClaudeAgentOptions(system_prompt=system_message)) as client:
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
                        if isinstance(message, AssistantMessage):
                            for block in message.content:
                                if isinstance(block, TextBlock):
                                    print(f"Claude: {block.text}")



            except KeyboardInterrupt:

                print("\nGoodbye!")

                break

            except EOFError:

                break

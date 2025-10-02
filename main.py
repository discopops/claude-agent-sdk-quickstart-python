# main.py
from os.path import join, dirname

import anyio
from dotenv import load_dotenv

from agent_with_tools import start_chat_tools
from basic_query import basic_query
from interactive_terminal import start_chat_loop, start_chat_loop_continuous

dot_envpath = join(dirname(__file__), ".env.local")
load_dotenv(dot_envpath)


anyio.run(start_chat_tools)



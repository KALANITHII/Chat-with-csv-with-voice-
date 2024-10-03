import io
import os

import chainlit as cl
import pandas as pd
from chainlit import on_chat_start, on_message
from chainlit.element import ElementBased
from dotenv import load_dotenv
from pandasai import Agent
from pandasai.llm import BambooLLM


load_dotenv()
llm = BambooLLM(api_key=os.getenv("PANDASAI_API_KEY"))



@on_chat_start
async def main():
    files = None

    # Wait for the user to upload a file
    while files is None:
        files = await cl.AskFileMessage(
            content="Please upload a csv to begin!", accept=["text/csv"]
        ).send()

    file = files[0]

    data = pd.read_csv(file.path, encoding="latin1")
    pandas_ai = Agent(data, config={"llm": llm})

    cl.user_session.set("agent", pandas_ai)

    await cl.Message(
        content=data.head()
    ).send()


@on_message
async def on_message(message):
    agent = cl.user_session.get("agent")
    if agent is None:
        return
    
    thinking_msg = cl.Message(content="")
    await thinking_msg.send()

    response = agent.chat(message.content)
    thinking_msg.content = response

    await thinking_msg.update()
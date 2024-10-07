from openai import AsyncOpenAI
from dotenv import load_dotenv
import panel as pn
import os
import asyncio

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

aclient = AsyncOpenAI(api_key=OPENAI_API_KEY)

pn.extension()

context = [{'role':'system', 'content':""" Your prompt goes here
"""}] #TODO add your prompt to it

async def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
    context.append({'role': 'user', 'content': contents})
    
    response = await aclient.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=context,
        stream=True,
    )

    message = ""
    async for chunk in response:
        part = chunk.choices[0].delta.content
        if part is not None:
            message += part
            yield message

def main():
    chat_interface = pn.chat.ChatInterface(
        callback=callback,
        callback_user="BotName",  #TODO add your callback
        help_text="Some help text",  #TODO add your help text
    )
    
    template = pn.template.FastListTemplate(
        title="Awesome bot", #TODO add your tittle
        header_background="#212121",
        main=[chat_interface]
    )

    template.servable()
    pn.serve(chat_interface, show=True)


if __name__ == "__main__":
    main()

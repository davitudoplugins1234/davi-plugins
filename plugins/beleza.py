import asyncio
import os
import random
import requests
import wget
from cowpy import cow

from kannax import Message, kannax

@kannax.on_cmd("beleza", about={"header": "Quanto bonito eu sou?"})
async def beleza_(message: Message):
    reply_ = message.reply_to_message
    if not reply_:
        beleza = f" Eu sou{random.choice(range(0,100))}% bonito!"
        await message.edit(beleza)
        return
    user_ = await kannax.get_users(reply_.from_user.id)
    msg_ = f" {user_.mention} é {random.choice(range(0,100))}% bonito!"
    await message.edit(msg_)

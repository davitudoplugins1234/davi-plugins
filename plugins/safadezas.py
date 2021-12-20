""" safadezas enjoy """

import asyncio
import os
import random
import requests
import wget
from cowpy import cow

from kannax import Message, kannax

@kannax.on_cmd("hor", about={"header": "Estou com tesão!?"})
async def hor_(message: Message):
    reply_ = message.reply_to_message
    if not reply_:
        hor = f"🔥 Estou com  {random.choice(range(0,100))}% tesão!"
        await message.edit(hor)
        return
    user_ = await kannax.get_users(reply_.from_user.id)
    msg_ = f" 🔥{user_.mention} tá com {random.choice(range(0,100))}% tesão!"
    await message.edit(msg_)


@kannax.on_cmd("pau", about={"header": " Tamanho do meu pau é!?"})
async def pau_(message: Message):
    reply_ = message.reply_to_message
    if not reply_:
        pau = f"🍆 O tamanho do meu pau é {random.choice(range(700,10000))}cm!"
        await message.edit(pau)
        return
    user_ = await kannax.get_users(reply_.from_user.id)
    msg_ = f" 🍆{user_.mention} o tamanho do pau é {random.choice(range(0,100))}cm!"
    await message.edit(msg_)

@kannax.on_cmd("cute", about={"header": "Quanto fofo eu sou?"})
async def cut_(message: Message):
    reply_ = message.reply_to_message
    if not reply_:
        cut = f"🍑 Eu sou {random.choice(range(0,100))}% fofo!"
        await message.edit(cut)
        return
    user_ = await kannax.get_users(reply_.from_user.id)
    msg_ = f" 🍑 O {user_.mention} é {random.choice(range(0,100))}% fofo!"
    await message.edit(msg_)

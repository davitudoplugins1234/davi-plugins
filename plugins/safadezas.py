""" safadezas enjoy """

import asyncio
import os
import random
import requests
import wget
from cowpy import cow

from kannax import Message, kannax

@kannax.on_cmd("horny", about={"header": "i am  horny!?"})
async def hor_(message: Message):
    reply_ = message.reply_to_message
    if not reply_:
        iam = f"🔥 I am {random.choice(range(0,100))}% horny!"
        await message.edit(hor)
        return
    user_ = await kannax.get_users(reply_.from_user.id)
    msg_ = f" 🔥{user_.mention} é {random.choice(range(0,100))}% horny!"
    await message.edit(msg_)


@kannax.on_cmd("clock", about={"header": "My clock size is!?"})
async def clo_(message: Message):
    reply_ = message.reply_to_message
    if not reply_:
        iam = f"🍆 My clock size is {random.choice(range(0,100))}cm!"
        await message.edit(clo)
        return
    user_ = await kannax.get_users(reply_.from_user.id)
    msg_ = f" 🍆{user_.mention} My clock size is {random.choice(range(0,100))}cm!"
    await message.edit(msg_)

@kannax.on_cmd("cute", about={"header": "i am  cute!"})
async def cu_(message: Message):
    reply_ = message.reply_to_message
    if not reply_:
        iam = f"🍑 I am {random.choice(range(0,100))}% cute!"
        await message.edit(cu)
        return
    user_ = await kannax.get_users(reply_.from_user.id)
    msg_ = f" 🍑 I am {user_.mention}  {random.choice(range(0,100))}% cute!"
    await message.edit(msg_)

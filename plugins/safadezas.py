""" safadezas enjoy """

import asyncio
import os
import random
import requests
import wget
from cowpy import cow

from kannax import Message, kannax

@kannax.on_cmd("hor", about={"header": "i am  horny!?"})
async def hor_(message: Message):
    reply_ = message.reply_to_message
    if not reply_:
        iam = f"🔥 I am {random.choice(range(0,100))}% horny!"
        await message.edit(hor_)
        return
    user_ = await kannax.get_users(reply_.from_user.id)
    msg_ = f" 🔥{user_.mention} é {random.choice(range(0,100))}% horny!"
    await message.edit(msg_)


@kannax.on_cmd("clock", about={"header": "My clock size is!?"})
async def clock_(message: Message):
    reply_ = message.reply_to_message
    if not reply_:
        iam = f"🍆 My clock size is {random.choice(range(0,100))}cm!"
        await message.edit(clock_)
        return
    user_ = await kannax.get_users(reply_.from_user.id)
    msg_ = f" 🍆{user_.mention} My clock size is {random.choice(range(0,100))}cm!"
    await message.edit(msg_)

@kannax.on_cmd("cute", about={"header": "i am  cute!"})
async def cute_(message: Message):
    reply_ = message.reply_to_message
    if not reply_:
        iam = f"🍑 I am {random.choice(range(0,100))}% cute!"
        await message.edit(cute_)
        return
    user_ = await kannax.get_users(reply_.from_user.id)
    msg_ = f" 🍑 I am {user_.mention}  {random.choice(range(0,100))}% cute!"
    await message.edit(msg_

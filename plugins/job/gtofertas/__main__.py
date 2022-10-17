import asyncio
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from userge import userge, Message

@userge.on_cmd("gtofertas", about={"header": "Enviar ofertas"}, allow_via_bot=False)
async def gtofertas_(message: Message):
    id, time = message.filtered_input_str.split(maxsplit=1)
    message_reply = int(id)
    message_count = 0
    while True:
        try:
            i = await userge.forward_messages(-1001115033767, -1001197236241, message_reply)
            message_reply += 1
            if i:
                 message_count += 1
                 await message.edit(f"<b>Ofertas Enviadas</b>: <i>{message_count}</i>\n\n<b>Time sleep</b>: <i>{time}</i>\n<b>ID</b>: <code>{message_reply}</code>")
                 await asyncio.sleep(int(time))
        except MessageIdInvalid:
            message_reply += 1
            continue


@userge.on_cmd("gtimport", about={"header": "Enviar ofertas"}, allow_via_bot=False)
async def gtofertas_import(message: Message):
    id, time = message.filtered_input_str.split(maxsplit=1)
    message_reply = int(id)
    message_count = 0
    while True:
        try:
            i = await userge.forward_messages(-1001115033767, -1001389672812, message_reply)
            message_reply += 1
            if i:
                 message_count += 1
                 await message.edit(f"<b>Ofertas Enviadas</b>: <i>{message_count}</i>\n\n<b>Time sleep</b>: <i>{time}</i>\n<b>ID</b>: <code>{message_reply}</code>")
                 await asyncio.sleep(int(time))
        except MessageIdInvalid:
            message_reply += 1
            continue

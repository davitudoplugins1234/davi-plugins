# by DaviTudo

from pyrogram.errors import YouBlockedUser

from userge import Message, userge

@userge.on_cmd("k|K", about={"header": "risada curta"}, allow_via_bot=False)
async def k_(message: Message):
    out_str =f"KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
    await message.edit(out_str)

@userge.on_cmd("kkk|KKK", about={"header": "risada  longa"}, allow_via_bot=False)
async def kkk_(message: Message):
    out_str = f"KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
    await message.edit(out_str)

@userge.on_cmd(
    "clima",
    about={
        "header": "Weather of the city",
        "description": "Busque o clima para uma cidade",
        "usage": "{tr}clima [text]",
    },
)
async def clima_ln(message: Message):
    city_ = message.input_str
    bot_ = "@WhiterKangBOT"
    async with userge.conversation(bot_, timeout=1000) as conv:
        try:
            await conv.send_message(f"!clima {city_}")
        except YouBlockedUser:
            await message.reply("Por Favor desbloqueie a @WhiterKangBOT")
            return
        response = await conv.get_response(mark_read=True)
        await message.edit(response.text)

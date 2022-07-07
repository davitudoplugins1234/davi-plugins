from pyrogram.errors import YouBlockedUser
from userge import Message, userge


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
    if not city_:
        return await message.edit("<b>Uso:</b> <code>/clima localização ou cidade</code> <i>- Obtém informações sobre o clima na localização ou cidade.</i>")
    bot_ = "@WhiterKangBOT"
    async with userge.conversation(bot_, timeout=1000) as conv:
        try:
            await conv.send_message(f"!clima {city_}")
        except YouBlockedUser:
            await message.edit("Por Favor desbloqueie a @WhiterKangBOT")
            return
        response = await conv.get_response(mark_read=True)
        await message.edit(response.text)

# by joaoppierri

from pyrogram.errors import BadRequest

from kannax import Message, kannax
from kannax.utils import get_file_id

@kannax.on_cmd("perg", about={"header": "ask telegram"}, allow_via_bot=False)
async def perg_(message: Message):
    out_str f"https://telegra.ph/Como-fazer-perguntas-no-Telegram-07-21"
    await message.edit(out_str)

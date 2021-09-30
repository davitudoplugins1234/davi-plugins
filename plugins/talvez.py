# by joaoppierri

from pyrogram.errors import BadRequest

from kannax import Message, kannax
from kannax.utils import get_file_id

@kannax.on_cmd("t", about={"header": "talvez 🤔"})
async def t_(message: Message):
    out_str = f"talvez 🤔"
    await message.edit(out_str)
    

# by joaoppierri

from pyrogram.errors import BadRequest

from kannax import Message, kannax
from kannax.utils import get_file_id

@kannax.on_cmd("a", about={"header": "ata"})
async def a_(message: Message):
    out_str = f"ata"
    await message.edit(out_str)

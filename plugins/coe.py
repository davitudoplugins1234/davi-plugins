# by joaoppierri

from pyrogram.errors import BadRequest

from kannax import Message, kannax
from kannax.utils import get_file_id

@kannax.on_cmd("c", about={"header": "coe"})
async def c_(message: Message):
    out_str = f"coee"
    await message.edit(out_str)

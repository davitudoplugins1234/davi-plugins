# by joaoppierri

from pyrogram.errors import BadRequest

from kannax import Message, kannax
from kannax.utils import get_file_id

@kannax.on_cmd("n", about={"header": "não"}
async def n_(message: Message):
    out_str = f"não"
    await message.edit(out_str)
    

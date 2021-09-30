# by joaoppierri

from pyrogram.errors import BadRequest

from kannax import Message, kannax
from kannax.utils import get_file_id

@kannax.on_cmd("se", about={"header": "sei lá"}
async def se_(message: Message):
    out_str = f"sei lá"
    await message.edit(out_str)
    

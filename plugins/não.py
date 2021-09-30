# by joaoppierri

from pyrogram.errors import BadRequest

from kannax import Message, kannax
from kannax.utils import get_file_id

@kannax.on_cmd("n", about={"header": "não"}, trigger="", allow_via_bot=False)
async def n_(message: Message):
    out_str = f"não"
    await message.edit(out_str)
    

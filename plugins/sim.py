# by joaoppierri

from pyrogram.errors import BadRequest

from kannax import Message, kannax
from kannax.utils import get_file_id

@kannax.on_cmd("s", about={"header": "sim"}, trigger="", allow_via_bot=False)
async def s_(message: Message):
    out_str = f"simm"
    await message.edit(out_str)
    

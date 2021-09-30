# by joaoppierri

from pyrogram.errors import BadRequest

from kannax import Message, kannax
from kannax.utils import get_file_id

@kannax.on_cmd("w", about={"header": "wtf"}, trigger="", allow_via_bot=False)
async def w_(message: Message):
    out_str = f"wtff"
    await message.edit(out_str)
    

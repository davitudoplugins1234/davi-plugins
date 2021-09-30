# by joaoppierri

from pyrogram.errors import BadRequest

from kannax import Message, kannax
from kannax.utils import get_file_id

@kannax.on_cmd("td", about={"header": "tudo bom?"}, trigger="", allow_via_bot=False)
async def td_(message: Message):
    out_str = f"tudo bom?
    await message.edit(out_str)

# by joaoppierri

from pyrogram.errors import BadRequest

from kannax import Message, kannax
from kannax.utils import get_file_id

@kannax.on_cmd("repo", about={"header": "customrepo"}, allow_via_bot=False)
async def repo_(message: Message):
    out_str = f"https://github.com/JoaoPedroPierri/joao-plugins"
    await message.edit(out_str)

# by joaoppierri

from pyrogram.errors import BadRequest

from kannax import Message, kannax
from kannax.utils import get_file_id

@kannax.on_cmd("joao", about={"header": "customrepo"}, allow_via_bot=False)
async def joao_(message: Message):
    out_str = f"https://github.com/Giovanyeeeh/Giovany-Plugins"
    await message.edit(out_str)

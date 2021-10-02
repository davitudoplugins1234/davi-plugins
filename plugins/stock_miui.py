from pyrogram.errors import BadRequest

from kannax import Message, kannax
from kannax.utils import get_message_id


@kannax.on_cmd(
    "msu",
    about={
        "titulo": "Pesquisa a StockRom do seu Xiaomi",
        "como usar": ".stock #codename",
    },
)
async def app_sistema(message: Message):
    """Módulo para facilitar encontrar suas stockroms xiaomi"""
    aplicativo = message.input_str
    if not aplicativo:
        await message.err("Tente usar o codenome.", del_in=10)
        return
    search = await message.edit("𝙿𝚎𝚜𝚚𝚞𝚒𝚜𝚊𝚗𝚍𝚘 𝚙𝚘𝚛: {}".format())
    chat_id = message.chat.id
    f_id = ""
    try:
        async for msg in kannax.search_messages(
            "MIUI Download by xiaomiui", query=aplicativo, limit=1, filter="message"
        ):
            f_id = get_file_id(msg)
    except BadRequest:
        await search.edit(
            "Obrigatório participar do deste [canal](https://t.me/miui_download)."
        )
        return
    if not f_id:
        await search.edit("Falha na Matrix: Não encontrei foi nada...", del_in=5)
        return
    await kannax.send_message(chat_id, f_id)
    await search.delete()

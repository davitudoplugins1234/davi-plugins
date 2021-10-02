""" Plugin para baixar APK da Modded Central / @joaoppierri """

from pyrogram.errors import BadRequest

from kannax import Message, kannax
from kannax.utils import get_file_id


@kannax.on_cmd(
    "msu",
    about={
        "titulo": "Pesquisa um aplicativo direto do Modded Central Channel",
        "como usar": ".msu Launcher",
    },
)
async def app_sistema(message: Message):
    """Módulo para pesquisar e enviar rapidamente apps crackeados"""
    aplicativo = message.input_str
    if not aplicativo:
        await message.err("Tente usar o nome de um app.", del_in=10)
        return
    search = await message.edit("𝙿𝚎𝚜𝚚𝚞𝚒𝚜𝚊𝚗𝚍𝚘 𝚙𝚘𝚛: {}".format(aplicativo))
    chat_id = message.chat.id
    f_id = ""
    try:
        async for msg in kannax.search_messages(
            "Modded Central Channel", query=aplicativo, limit=1, filter="document"
        ):
            f_id = get_file_id(msg)
    except BadRequest:
        await search.edit(
            "Obrigatório participar do deste [canal](https://t.me/ModdedCentral)."
        )
        return
    if not f_id:
        await search.edit("Falha na Matrix: Não encontrei foi nada...", del_in=5)
        return
    await kannax.send_document(chat_id, f_id)
    await search.delete()

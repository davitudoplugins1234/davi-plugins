# tiktok downloader

import os
from wget import download

from kannax import Message, kannax, Config
from kannax.utils import get_response

API = "https://hadi-api.herokuapp.com/api/tiktok";


@kannax.on_cmd(
    "tiktok",
    about={
        "header": "Tiktok Downloader",
        "description": "baixa videos do tiktok com link",
        "usage": "{tr}tiktok link",
    },
)
async def ttdown_(message: Message):
    link = message.input_or_reply_str
    await message.edit("`Aguarde ...`")
    if not "tiktok.co" in link:
        return await message.edit("`Isso não é um link tiktok`")
    params = {
            "url": link,
        };
    try:
        response = await get_response.json(link=API, params=params)
    except ValueError:
        return await message.err("API Inativa", del_in=5)
    if not response["status"] == 200:
        return await message.err("Ocorreu um erro ao consultar os dados do video, verifique se você inseriu o link corretamente.", del_in=10)
    await message.edit("`Processando o video  ...`")
    link_v = response["result"]["video"]["original"]
    vid = download(link_v, Config.DOWN_PATH)
    os.rename(vid, f"{Config.DOWN_PATH}video.mp4")
    
    await message.client.send_video(message.chat.id, f"{Config.DOWN_PATH}video.mp4")
    await message.delete()
    os.remove(f"{Config.DOWN_PATH}video.mp4")
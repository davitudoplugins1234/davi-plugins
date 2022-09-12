# by DaviTudo
import io
import os
import re
import shutil
import asyncio
import tempfile
import datetime
import httpx

from yt_dlp import YoutubeDL
from typing import Tuple, Callable
from functools import wraps, partial

from pyrogram import filters, enums
from userge import Message, userge

def aiowrap(func: Callable) -> Callable:
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)

    return run

@aiowrap
def extract_info(instance: YoutubeDL, url: str, download=True):
    return instance.extract_info(url, download)

YOUTUBE_REGEX = re.compile(
    r"(?m)http(?:s?):\/\/(?:www\.)?(?:music\.)?youtu(?:be\.com\/(watch\?v=|shorts/|embed/)|\.be\/|)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?"
)

http = httpx.AsyncClient()

TIME_REGEX = re.compile(r"[?&]t=([0-9]+)")
MAX_FILESIZE = 4000000000

@userge.on_cmd("k", about={"header": "risada curta"}, allow_via_bot=False)
async def k_(message: Message):
    out_str = f"KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
    await message.edit(out_str)

@userge.on_cmd("kkk", about={"header": "risada  longa"}, allow_via_bot=False)
async def kkk_(message: Message):
    out_str = f"KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
    await message.edit(out_str)

@userge.on_cmd("lol", about={"header": "lol command"}, allow_via_bot=False)
async def lol(message: Message):
    out_str = f"""
┏━┓┈┈╭━━━━╮┏━┓┈┈
┃╱┃┈┈┃╱╭╮╱┃┃╱┃┈┈
┃╱┗━┓┃╱┃┃╱┃┃╱┗━┓
┃╱╱╱┃┃╱╰╯╱┃┃╱╱╱┃
┗━━━┛╰━━━━╯┗━━━┛
    """
    await message.edit(out_str)


@userge.on_cmd(
    "ytsong", 
    about={'header': "Advanced YT_DLP song",
        'usage': "{tr}ytsong URL or Query"}
)
async def songyt(m: Message):
    if m.reply_to_message and m.reply_to_message.text:
        url = m.reply_to_message.text
    elif m.input_str:
        url = m.input_str
    else:
        await m.edit_text("Give me args")
        return

    ydl = YoutubeDL({"noplaylist": True})

    rege = YOUTUBE_REGEX.match(url)

    t = TIME_REGEX.search(url)
    temp = t.group(1) if t else 0

    if not rege:
        yt = await extract_info(ydl, f"ytsearch:{url}", download=False)
        try:
            yt = yt["entries"][0]
        except IndexError:
            return
    else:
        yt = await extract_info(ydl, rege.group(), download=False)

    for f in yt["formats"]:
        if f["format_id"] == "140":
            afsize = f["filesize"] or 0
        if f["ext"] == "mp4" and f["filesize"] is not None:
            vfsize = f["filesize"] or 0
            vformat = f["format_id"]
    if " - " in yt["title"]:
        performer, title = yt["title"].rsplit(" - ", 1)
    else:
        performer = yt.get("creator") or yt.get("uploader")
        title = yt["title"]
    if int(afsize) > MAX_FILESIZE:
        return await m.edit("Sorry, Telegram doesn't allow me to upload videos larger than 4GB")
    await m.edit("Downloading...")
    with tempfile.TemporaryDirectory() as tempdir:
        path = os.path.join(tempdir, "ytdlp")
        
    ttemp = f"⏰ {datetime.timedelta(seconds=int(temp))} | " if int(temp) else ""
    
    id = yt["id"]
    url = f"https://www.youtube.com/watch?v={id}"

    ydl = YoutubeDL(
        {
            "outtmpl": f"{path}/%(title)s-%(id)s.%(ext)s",
            "format": "bestaudio[ext=m4a]",
            "max_filesize": MAX_FILESIZE,
            "noplaylist": True,
        }
    )
    try:
        yt = await extract_info(ydl, url, download=True)
    except BaseException as e:
        await m.edit("<b>Error:</b> <i>{}</i>".format(e))
        return
    await m.edit("Sending...")
    filename = ydl.prepare_filename(yt)
    thumb = io.BytesIO((await http.get(yt["thumbnail"])).content)
    thumb.name = "thumbnail.png"
    views = 0
    likes = 0
    if yt.get("view_count"):
        views += yt["view_count"]
    if yt.get("like_count"):
        likes += yt["like_count"]
    await m.delete()
    await m.client.send_audio(
        m.chat.id,
        audio=filename,
        title=title,
        caption="<b>[{}]({})</b>\n\n<b>• Duration</b>: <i>{}</i>\n<b>• Channel</b>: <i>{}</i>\n<b>• Views</b>: <i>{}</i>\n<b>• Likes</b>: <i>{}</i>".format(ttemp + title, url, datetime.timedelta(seconds=yt["duration"]), yt["channel"] or None, views, likes or 0),
        performer=performer,
        duration=yt["duration"],
        thumb=thumb,
        reply_to_message_id=int(m.id),
    )
    
    
@userge.on_cmd(
    "ytvideo", 
    about={'header': "Advanced YT_DLP video",
        'usage': "{tr}ytsong URL or Query"}
)
async def songyt(m: Message):
    if m.reply_to_message and m.reply_to_message.text:
        url = m.reply_to_message.text
    elif m.input_str:
        url = m.input_str
    else:
        await m.edit_text("Give me args")
        return

    ydl = YoutubeDL({"noplaylist": True})

    rege = YOUTUBE_REGEX.match(url)

    t = TIME_REGEX.search(url)
    temp = t.group(1) if t else 0

    if not rege:
        yt = await extract_info(ydl, f"ytsearch:{url}", download=False)
        try:
            yt = yt["entries"][0]
        except IndexError:
            return
    else:
        yt = await extract_info(ydl, rege.group(), download=False)

    for f in yt["formats"]:
        if f["format_id"] == "140":
            afsize = f["filesize"] or 0
        if f["ext"] == "mp4" and f["filesize"] is not None:
            vfsize = f["filesize"] or 0
            vformat = f["format_id"]
    if " - " in yt["title"]:
        performer, title = yt["title"].rsplit(" - ", 1)
    else:
        performer = yt.get("creator") or yt.get("uploader")
        title = yt["title"]
    if int(vfsize) > MAX_FILESIZE:
        return await m.edit("Sorry, Telegram doesn't allow me to upload videos larger than 4GB")
    await m.edit("Downloading...")
    with tempfile.TemporaryDirectory() as tempdir:
        path = os.path.join(tempdir, "ytdlp")
        
    ttemp = f"⏰ {datetime.timedelta(seconds=int(temp))} | " if int(temp) else ""
    
    id = yt["id"]
    url = f"https://www.youtube.com/watch?v={id}"

     ydl = YoutubeDL(
         {
            "outtmpl": f"{path}/%(title)s-%(id)s.%(ext)s",
            "format": f"{vformat}+140",
            "max_filesize": MAX_FILESIZE,
            "noplaylist": True,
         }
    )
    try:
        yt = await extract_info(ydl, url, download=True)
    except BaseException as e:
        await m.edit("<b>Error:</b> <i>{}</i>".format(e))
        return
    await m.edit("Sending...")
    filename = ydl.prepare_filename(yt)
    thumb = io.BytesIO((await http.get(yt["thumbnail"])).content)
    thumb.name = "thumbnail.png"
    views = 0
    likes = 0
    if yt.get("view_count"):
        views += yt["view_count"]
    if yt.get("like_count"):
        likes += yt["like_count"]
    await m.delete()
    await m.client.send_video(
        m.chat.id,
        video=filename,
        width=1920,
        height=1080,
        caption="<b>[{}]({})</b>\n\n<b>• Duration</b>: <i>{}</i>\n<b>• Channel</b>: <i>{}</i>\n<b>• Views</b>: <i>{}</i>\n<b>• Likes</b>: <i>{}</i>".format(ttemp + title, url, datetime.timedelta(seconds=yt["duration"]), yt["channel"] or None, views, likes or 0),
        duration=yt["duration"],
        thumb=thumb,
        reply_to_message_id=int(m.id),
    )

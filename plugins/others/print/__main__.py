import httpx
import uuid

from httpx import HTTPError
from userge import Message, userge

http = httpx.AsyncClient()


@userge.on_cmd(
    "print",
    about={
        "header": "print command",
        "description": "take a print through a link",
        "usage": "{tr}print [link]",
    },
)
async def print_(message: Message):
    the_url = message.input_str.split()
    wrong = False
    
    if len(the_url) == 1:
        if message.reply_to_message:
            the_url = message_reply_to_message.text
            if len(the_url) == 1:
                wrong = True
            else:
                the_url = the_url[1]
        else:
            wrong = True
    else:
        the_url = the_url[1]
    
    if wrong:
        return await message.edit("Please give me a link so I can print")

    try:
        await message.edit("<i>Taking screenshot...</i>")
        res_json = await cssworker_url(target_url=the_url)
    except BaseException as e:
        await message.edit(f"Failed due to {e}")
     
    if res_json:
        image_url = res_json["url"]
        if image_url:
            try:
                await message.reply_photo(image_url)
                await message.delete()
            except BaseException:
                return
        else:
            await message.edit("Couldn't get url value, most probably API not accessible")
    else:
        await message.edit("Failed Because API not responding, try again later")
          
          
async def cssworker_url(target_url: str):
    url = "https://htmlcsstoimage.com/demo_run"
    my_headers = {
       "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv: 95.0) Gecko/201000101 Firefox/95.0",
    }
     
    data = {
        "url": target_url,
        # Sending a random CSS to make the API to generate a new screenshot.
        "css": f"random-tag {uuid.uuid4()}",
        "render_when_ready": False,
        "viewport_width": 1280,
        "viewport_height": 720,
        "device_scale": 1,
    }

    try:
        resp = await http.post(url, headers=my_headers, json=data)
        return resp.json()
    except HTTPError:
        return None

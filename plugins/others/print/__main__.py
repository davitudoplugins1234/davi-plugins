import httpx

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
    the_url = message.input_str
    wrong = False
    
    if len(the_url) == 1:
        if message.reply_to_message:
            the_url = message_reply_to_message.text
            if len(the_url) == 1
                wrong = True
            else:
                the_url = the_url[1]
        else:
            wrong = True
    else:
        the_url = the_url[1]
    
    if wrong:
        return await message.reply("Please give me a link so I can print")

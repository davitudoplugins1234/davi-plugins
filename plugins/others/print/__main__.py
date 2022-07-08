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
    msg = message.input_str
    wrong = False

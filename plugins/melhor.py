
import asyncio

from kannax import Message, kannax


@kannax.on_cmd("melhor", about={"header": "Melhor"})
async def sii_(message: Message):
    out_str =   f"""texto = test
texto2 = test1

await message.edit(texto)
asyncio.sleep(2)
await message.edit(texto2)"""

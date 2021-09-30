from random import randint, choice

from kannax import Message, kannax

@kannax.on_cmd('sor' , about={"header": 'estou com sorte?'})
async def sort_(message: Message):
    sort = f"Número da sorte: {random.choice(range(0, 10))}"
    await message.edit(sort)

# by DaviTudo


from userge import Message, userge

@userge.on_cmd("k", about={"header": "risada curta"}, allow_via_bot=False)
async def k_(message: Message):
    out_str =f"KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
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

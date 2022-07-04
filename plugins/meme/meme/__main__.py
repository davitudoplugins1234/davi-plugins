# by joaoppierri

from userge import Message, userge

@userge.on_cmd("k|K", about={"header": "risada curta"}, allow_via_bot=False)
async def k_(message: Message):
    out_str =f"KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
    await message.edit(out_str)

@userge.on_cmd("kkk|KKK", about={"header": "risada  longa"}, allow_via_bot=False)
async def kkk_(message: Message):
    out_str = f"KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
    await message.edit(out_str)

@userge.on_cmd("rt", about={"header": "rt message"},  allow_via_bot=False)
async def rt_(message: Message):
    """rt mensagem"""
    retweet = message.reply_to_message
    try:
        rt_msg = retweet.text
        user_ = retweet.from_user.first_name
        user_me = await message.client.get_user_dict(message.from_user.id)
        usr_me = user_me["fname"]
        mensg = f"🔃 {usr_me} retweetou:\n\n👤 {user_}: {rt_msg}"
        await message.edit(mensg)
    except:
        pass

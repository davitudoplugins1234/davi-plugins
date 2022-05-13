import dicioinformal

@kannax.on_message(filters.command("dicio"))
async def dicio(c: Smudge, m: Message):
    txt = m.text.split(" ", 1)[1]
    a = dicioinformal.definicao(txt)["results"]
    if a:
        frase = f'<b>{a[0]["title"]}:</b>\n{a[0]["tit"]}\n\n<i>{a[0]["desc"]}</i>'
    else:
        frase = "sem resultado"
    await m.reply(frase)

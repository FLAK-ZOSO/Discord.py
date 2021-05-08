import discord
from discord.ext import commands
from discord import client

print("BOT Lillo, parte di on_message, censura.py")
token = "ODM3OTY3Mjk3MzE0NDIyODU0.YI0P3A.c_JhTZCpy-nm1-bTVJN3s1uv3YU"
Bot = commands.Bot(command_prefix = "£")

@Bot.event
async def on_ready():
    print(Bot.user, " è ora online ", "ID: ", Bot.user.id)
    game = discord.Game("Fare la limonata | £Aiuto | Limoncello")
    await Bot.change_presence(status = discord.Status.idle, activity = game)

@Bot.event
async def on_message(messaggio):
    Bestemmie = ["Porcodio", "PORCODIO", "Madonna Puttana", "DIOPORCO", "PORCAMADONNA", "porcamadonna", "Porca Madonna", "porcodio", "Porco dio", "Porco Dio", "porco dio", "diocane", "Diocane", "dio porco", "Dio porco", "Dioporco", "dioporco", "Dio Porco","madonna troia", "Madonna troia", "Mannaggia a dio", "Madonna zoccola", "Madonna Puttana", "Gesù bastardo", "Dio Merda"]
    Parolacce = ["Cazzo", "cazzo", "Coglioni", "coglioni"]
    Offese = ["Zoccola", "zoccola", "Troia", "troia", "puttana", "Puttana", "Coglione", "coglione", "Cogliona", "cogliona"]
    link_proibiti = ["https://discord.gg/"]
                
    #Controllo Bestemmie
    if messaggio.author != Bot.user:
        for i in Bestemmie:
            if i in messaggio.content:
                print(f'{messaggio.author} ha scritto {i} in {messaggio.channel}')
                await messaggio.reply(f'''Hai detto ||{i}||, quindi il tuo messaggio è stato censurato in quanto offensivo.
I moderatori potranno segnalarti con `£Avvertimento {messaggio.author.mention} regola-il-linguaggio`
''')
                await messaggio.reply(f"""{messaggio.author.mention}, il tuo messaggio è stato cancellato, ma rimarrà consultabile dal mio host finché sarò online.
I moderatori potranno richiedere una copia del tuo messaggio rivolgendosi all'host.""")
                await messaggio.delete()
                await messaggio.author.send(f'Non dire mai più "{i}" nel server dei limoni!')
                
    #Controllo menzioni
    if 'Limoncello' in messaggio.content or 'LIMONCELLO' in messaggio.content or 'limoncello' in messaggio.content or 'Limoncello#1127' in messaggio.content or '@Limoncello#1127' in messaggio.content:
            sono_stato_menzionato = str(f'''{messaggio.author.mention}, perché mi hai menzionato? Non vedo limonate in giro!
Trovi la mia lista comandi con `£Aiuto.`''')
            await messaggio.reply(sono_stato_menzionato)
            print(f'{messaggio.author} MI HA MENZIONATO in {messaggio.channel}!')
    if ("Dio" in messaggio.content or "dio" in messaggio.content or "Buddha" in messaggio.content or "Allah" in messaggio.content or "buddha" in messaggio.content or "allah" in messaggio.content or "madonna" in messaggio.content or "Madonna" in messaggio.content) and messaggio.author != Bot.user:
        print(f'{messaggio.author} ha nominato un personaggio religioso in {messaggio.channel}')

    #Controllo link
    for i in link_proibiti:
        if i in messaggio.content:
            author = messaggio.author
            if 'Diodesperado' in author.roles:
                return
            if messaggio.channel != '〘🥂〙𝘊𝘰𝘭𝘭𝘢𝘣𝘰𝘳𝘢𝘻𝘪𝘰𝘯𝘪.':
              await messaggio.author.ban(reason = 'Spamming di link sospetto, non invintare nessuno a tuoi server personali.')
              await messaggio.delete()
              await messaggio.channel.send(f"{messaggio.author.mention} ha provato a inviare un link di discord. Ho bannato la sua utenza dal server")
              await messaggio.author.send(f'{messaggio.author.mention}, puoi richiedere a @FLAK_FLAK#3241 un nuovo invito al server dei Limoni, non provare più a inviare inviti a server esterni fuori dal canale #〘🥂〙𝘊𝘰𝘭𝘭𝘢𝘣𝘰𝘳𝘢𝘻𝘪𝘰𝘯𝘪.')
              print(f'Ho kickato {messaggio.author}')
            return
                
Bot.run(token)

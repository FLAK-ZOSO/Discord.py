import discord
from discord.ext import commands
from discord import client
from asyncio import sleep

messaggi = []

print("BOT Lillo, parte di on_message, spam.py")
token = "ODM3OTY3Mjk3MzE0NDIyODU0.YI0P3A.c_JhTZCpy-nm1-bTVJN3s1uv3YU"
Bot = commands.Bot(command_prefix = "£")

@Bot.event
async def on_ready():
    print(Bot.user, " è ora online ", "ID: ", Bot.user.id)

@Bot.event
async def on_message(messaggio):
    global messaggi
    author = messaggio.author
    if author != Bot.user:
        messaggi.append(messaggio.content)
        for i in messaggi:
            if i == messaggio.content:
                if len(messaggi) > 2:
                    lunghezza = len(messaggi)
                    if messaggi[lunghezza-1] == messaggi[lunghezza-2] == messaggi[lunghezza-3]:
                        if messaggi[lunghezza-1] == messaggi[lunghezza-2] == messaggi[lunghezza-3] == messaggi[lunghezza-4]:
                            if messaggi[lunghezza-1] == messaggi[lunghezza-2] == messaggi[lunghezza-3] == messaggi[lunghezza-4] == messaggi[lunghezza-5]:
                                try:
                                    await author.kick(reason = 'spam')
                                    print(f"{author} stava spammando un messaggio in {messaggio.channel}, quindi l'ho espulso.")
                                    await messaggio.reply(f"{author.mention} stava spammando questo messaggio, quindi l'ho espulso.")
                                    print(messaggi)
                                    messaggi = []
                                    return
                                except discord.errors.Forbidden:
                                    await messaggio.reply(f"{author.mention} stava spammando questo messaggio, quindi ho provato ad espellerlo. Purtroppo non ho l'autorizzazione necessaria per farlo.")
                                    print(messaggi)
                                    messaggi = []
                                    return
                            else:
                                await messaggio.reply(f'{author.mention}, questo è il tuo ultimo avvertimento!')
                                return
                        else:
                            await messaggio.reply(f'{author.mention}, smettila di scrivere lo stesso messaggio. Se lo farai altre due volte sarai espulso dal server!')
                            return messaggi
                    else:
                        return messaggi
    else:
        return
            
Bot.run(token)

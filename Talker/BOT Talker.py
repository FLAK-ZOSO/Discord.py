import random
import string
import discord
from discord.ext import commands
from discord import client
import time
import webbrowser

print("Eseguendo il programma...")
token = "ODIzMTg5MTc0NDI4NzYyMTMz.YFdMqQ.Jvh7wZcrmkDm2hBP2P4bojxHZN0"
client = commands.Bot(command_prefix = "£")

@client.event

async def on_ready():
    print(client.user, " è ora online ", "ID: ", client.user.id)

@client.event

async def on_mention(ctx):
    print(client.user, client.user.id, " può risponderti col comando £Aiuto")

@client.command()

async def Aiuto(ctx):
    Aiuto = str('''I comandi utilizzabili sono i seguenti:
    £Aiuto :joy:
    £Benvenuto :wave:
    £Casuale
    £itwikipedia nome_della_pagina :mag:
    £Wikipedia nome_della_pagina :mag: :wikipedia:
    £Nonciclopedia nome_della_pagina :mag_right:
    £Cancella N :recycle:
    £Scrivi Parole-del-messaggio :pencil:
    £Ripeti Parole-del-messaggio :parrot:
    £Comando Comando (non funzionante):cross:
    £Espelli @Utente (non funzionante):cross:
    £Emoji Nome_dell'emoji :sushi:
    £Auguri Festività :partying_face:
    £Maiuscolo Parole-da-ridurre
    £Minuscolo Parole-da-aumentare
    £Spam_15 Parole-da-spammare :printer:
    £Spam_5 Parole-da-spammare
    £Spam_link Link-da-spammare 
    £Spam_menzione @Ruolo/Utente-da-menzionare :loudspeaker:
    ''')
    await ctx.send(Aiuto)
    
@client.command()
@commands.has_role('Autorizzato a Talker')
async def Benvenuto(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send("Benvenuto nel server")

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Casuale(ctx):
    nonciclopedia = "https://nonciclopedia.org/wiki/Speciale:PaginaCasuale/"
    wikipedia = "https://it.wikipedia.org/wiki/Speciale:PaginaCasuale/"
    numero = random.randint(0, 30000)
    if numero < 15000:
        numero = str(numero)
        Pagina_Casuale = str(nonciclopedia + numero)
    elif numero > 14999:
        numero = str(numero)
        Pagina_Casuale = str(wikipedia + numero)
    await ctx.channel.purge(limit = 1)
    await ctx.send(Pagina_Casuale)

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Nonciclopedia(ctx, ricerca):
    ricerca = str(ricerca)
    link = "https://nonciclopedia.org/wiki/"
    Pagina = str(link + ricerca)
    await ctx.send(Pagina)

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Wikipedia(ctx, ricerca):
    ricerca = str(ricerca)
    link = "https://wikipedia.org/wiki/"
    Pagina = str(link + ricerca)
    await ctx.send(Pagina)

@client.command()
@commands.has_role('Autorizzato a Talker')
async def itwikipedia(ctx, ricerca):
    ricerca = str(ricerca)
    link = "https://it.wikipedia.org/wiki/"
    Pagina = str(link + ricerca)
    await ctx.send(Pagina)

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Cancella(ctx, amount = 1000):
    await ctx.channel.purge(limit = amount)

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Scrivi(ctx, parola):
    await ctx.channel.purge(limit = 1)
    parola = parola.replace("-", " ", 100)
    await ctx.send(parola)

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Ripeti(ctx, parola):
    parola = parola.replace("-", " ", 100)
    await ctx.send(parola)

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Emoji(ctx, emoji):
    await ctx.channel.purge(limit = 1)
    emoji = (':' + emoji + ':')
    await ctx.send(emoji)

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Auguri(ctx, festività):
    await ctx.channel.purge(limit = 1)
    if festività == "Pasqua":
        await ctx.send('Buona Pasqua :egg:')
    elif festività == "Compleanno":
        await ctx.send(':partying_face: Buon Compleanno! :birthday:')
    elif festività == "Natale":
        await ctx.send('Buon Natale! :santa:')
    else:
        await ctx.send('Auguri per la festa ' + festività)

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Maiuscolo(ctx, messaggio):
    await ctx.channel.purge(limit = 1)
    messaggio = str(messaggio)
    messaggio = messaggio.replace("-", " ", 100)
    messaggio = messaggio.upper()
    await ctx.send(messaggio)    

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Minuscolo(ctx, messaggio):
    await ctx.channel.purge(limit = 1)
    messaggio = str(messaggio)
    messaggio = messaggio.replace("-", " ", 100)
    messaggio = messaggio.lower()
    await ctx.send(messaggio)    

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Spam_5(ctx, parola):
    await ctx.channel.purge(limit = 1)
    parola = parola.replace('-',' ', 100)
    parola = str(parola)
    for i in range(5):
        await ctx.send(parola)

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Spam_15(ctx, parola):
    await ctx.channel.purge(limit = 1)
    parola = parola.replace('-',' ', 100)
    parola = str(parola)
    for i in range(15):
        await ctx.send(parola)

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Spam_link(ctx, link):
    await ctx.channel.purge(limit = 1)
    link = str(link)
    for i in range(5):
        await ctx.send(link)

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Spam_menzione(ctx, menzione):
    await ctx.channel.purge(limit = 1)
    parola = str(menzione)
    for i in range(5):
        await ctx.send(menzione)
        await ctx.channel.purge(limit = 1)

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Avviso(ctx):
    await webbrowser.open('it.wikipedia.org')

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Aggiungi_Ruolo(ctx, user: discord.Member, role: discord.Role):
    await ctx.channel.purge(limit = 1)
    await user.add_roles(role)
    await ctx.send(f"Ho aggiunto il ruolo {role.mention} all'utente {user.mention}.")

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Togli_Ruolo(ctx, user: discord.Member, role: discord.Role):
    await ctx.channel.purge(limit = 1)
    await user.remove_roles(role)
    await ctx.send(f"Ho rimosso il ruolo {role.mention} all'utente {user.mention}.")

client.run(token)

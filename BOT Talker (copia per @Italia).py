import random
import string
import discord
from discord.ext import commands
from discord import client
import time
import webbrowser

print("Eseguendo il programma...")
token = "ODI4MDA3ODc5MDY3MTcyODg1.YGjUbg.WXC9LRX1SZLvB16GFUuHmImfjY4"
client = commands.Bot(command_prefix = "$")

@client.event

async def on_ready():
    print(client.user, " è ora online ", "ID: ", client.user.id)

@client.event

async def on_mention(ctx):
    await ctx.send(client.user, client.user.id, " può risponderti col comando $Aiuto")

@client.command()

async def Aiuto(ctx):
    Aiuto = str('''I comandi utilizzabili sono i seguenti:
    $Aiuto :joy:
    $Benvenuto :wave:
    $Benvenuto_regione :flag_it:
    $Casuale
    $itwikipedia nome_della_pagina :mag:
    $Wikipedia nome_della_pagina :mag: :wikipedia:
    $Nonciclopedia nome_della_pagina :mag_right:
    $Cancella N :recycle:
    $Scrivi Parole-del-messaggio :pencil:
    $Ripeti Parole-del-messaggio :parrot:
    $Comando Comando (non funzionante):cross:
    $Espelli @Utente (non funzionante) :cross:
    $Espulsione @Utente (non funzionante):cross:
    $Anonimo @Utente messaggio-da-mandare :email:
    $Avvertimento @Utente avvertimento-da-mandare :warning:
    $Emoji Nome_dell'emoji :sushi:
    $Auguri Festività :partying_face:
    $Maiuscolo Parole-da-ridurre
    $Minuscolo Parole-da-aumentare
    $Spam_15 Parole-da-spammare :printer:
    $Spam_5 Parole-da-spammare
    $Spam_link Link-da-spammare 
    $Spam_menzione @Ruolo/Utente-da-menzionare :loudspeaker:
    ''')
    await ctx.send(Aiuto)
    

@client.command()

async def Benvenuto(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send("Benvenuto in Italia :flag_it:")

@client.command()

async def Benvenuto_regione(ctx, regione):
    await ctx.channel.purge(limit = 1)
    regione = str(regione)
    await ctx.send(f'Benvenuto in {regione}')

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Espelli(ctx, username: discord.User):
    await client.kick(username)

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
async def Tasse(ctx, reddito):
    reddito = int(reddito)
    if reddito <= 1250:
        tasse = round(reddito*0.23)
        tasse_txt = str(tasse)
        tasse = str('Devi pagare ' + tasse_txt + ' euro di tasse :coin:')
        await ctx.send(tasse)
    if reddito > 1250:
        tasse = round(1250*0.23)
        reddito_residuo = round(reddito-1250)
        if reddito  <= 2333:
            tasse = round(tasse + reddito_residuo*0.27)
            tasse_txt = str(tasse)
            tasse = str('Devi pagare ' + tasse_txt + ' euro di tasse :coin:')
            await ctx.send(tasse)
        if reddito > 2333:
            tasse = round(tasse + 1083*0.27)
            reddito_residuo = round(reddito_residuo - 1083)
            if reddito  <= 4583:
                tasse = round(tasse + reddito_residuo*0.38)
                tasse_txt = str(tasse)
                tasse = str('Devi pagare ' + tasse_txt + ' euro di tasse :coin:')
                await ctx.send(tasse)
            if reddito > 4583:
                tasse = round(tasse + 2250*0.38)
                reddito_residuo = round(reddito_residuo - 2250)
                if reddito  <= 6250:
                    tasse = round(tasse + reddito_residuo*0.41)
                    tasse_txt = str(tasse)
                    tasse = str('Devi pagare ' + tasse_txt + ' euro di tasse :coin:')
                    await ctx.send(tasse)
                if reddito > 6250:
                    tasse = round(tasse + 1667*0.41)
                    reddito_residuo = round(reddito_residuo - 1667)
                    tasse = round(reddito_residuo*0.43)
                    tasse_txt = str(tasse)
                    tasse = str('Devi pagare ' + tasse_txt + ' euro di tasse :coin:')
                    await ctx.send(tasse)
                    
@client.command()
@commands.has_role('Autorizzato a Talker')
async def itwikipedia(ctx, ricerca):
    ricerca = str(ricerca)
    link = "https://it.wikipedia.org/wiki/"
    Pagina = str(link + ricerca)
    await ctx.send(Pagina)

@client.command()

async def Cancella(ctx, amount = 10000):
    await ctx.channel.purge(limit = amount)
    amount = str(amount)
    await ctx.send('Sono stati eliminati ' + amount + " messaggi!")

@client.command()

async def Scrivi(ctx, parola):
    await ctx.channel.purge(limit = 1)
    parola = parola.replace("-", " ", 100)
    await ctx.send(parola)

@client.command()

async def Ripeti(ctx, parola):
    parola = parola.replace("-", " ", 100)
    await ctx.send(parola)

@client.command()
@commands.has_role('Autorizzato a Talker')
async def Comando(ctx, comando):
    await ctx.channel.purge(limit = 1)
    await ctx.send(comando)
    eval(comando)

@client.command()

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
async def Pornhub(ctx):
    await webbrowser.open('it.wikipedia.org')

@client.command(description="Avverte in privato un cittadino")
@commands.has_role('Autorizzato a Talker')
async def Avvertimento(ctx, member:discord.User = None, reason = None):
    if reason == None:
        await ctx.send('E per cosa lo staresti avvertendo?! Prova con £Avvertimento {member} parole-del-tuo-avvertimento')
    else:
        reason = reason.replace('-', ' ', 100)
        author = ctx.message.author
        await member.send(f"{member}, la tua utenza è stata avvertita da {author}! Motivo: {reason}")
        await ctx.channel.send(f"Avvertimento inviato a {member}")

@client.command(description="Scrive in privato ad un cittadino")
@commands.has_role('Autorizzato a Talker')
async def Anonimo(ctx, member:discord.User = None, messaggio = None):
    await ctx.channel.purge(limit = 1)
    if messaggio == None:
        await ctx.send(f"E che messaggio staresti mandando?! Prova con *£Anonimo {member} parole-del-tuo-messaggio*")
    else:
        messaggio = messaggio.replace('-', ' ', 100)
        author = ctx.message.author
        await member.send(f"{member}, ti recapito un messaggio in anonimo!")
        await member.send(f"{messaggio}")
        await author.send(f"Messaggio inviato a {member}, :white_check_mark: ")
        await author.send(f"Messaggio: {messaggio}")

@client.command(description="Comando di espulsione, solo per gli amministratori")
@commands.has_role('Autorizzato a Talker')
@commands.has_permissions(administrator=True)
async def Espulsione(ctx, member:discord.User=None, reason =None):
    try:
        if (reason == None):
            await ctx.channel.send("Come mai vuoi espellerlo?!")
            return
        if (member == ctx.message.author or member == None):
            await ctx.send("Non puoi espellerti da solo!")
        else:
            message = f"Sei stato espulso da {ctx.guild.name} col seguente motivo: {reason}"
            await member.send(message)
            motivo = reason.replace('-',' ', 100)
            await client.kick(member, reason=motivo)
            await ctx.channel.send(f"{member} è stato espulso! Motivo: {reason}")
    except:
        await ctx.send(f"Errore, hai provato ad espellere {member}, **non puoi espellere il proprietario o un bot!**")

client.run(token)

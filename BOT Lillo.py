from random import choice, randint
from asyncio import sleep
import discord
from discord.ext import commands
from discord import client

print("BOT Lillo.py")
token = "ODM3OTY3Mjk3MzE0NDIyODU0.YI0P3A.c_JhTZCpy-nm1-bTVJN3s1uv3YU"
Bot = commands.Bot(command_prefix = "£", description = "Ciao, sono Limoncello-Bot, mi occupo di gestione del server dei Limoni. Trovi la mia documentazione con £Documentazione")
gioco = discord.Game("£Aiuto | Limoncello | @Limoncello#1127")

@Bot.event
async def on_ready():
    print(Bot.user, " è ora online ", "ID: ", Bot.user.id)
    await Bot.change_presence(status = discord.Status.idle, activity = gioco)

lillo = ["https://tenor.com/view/gif-21466850", "https://tenor.com/view/gif-21466496", "https://tenor.com/view/gif-21466816", "https://tenor.com/view/gif-21466850", "https://tenor.com/view/gif-21466498", "https://tenor.com/view/gif-21466501", "https://tenor.com/view/gif-21466509", "https://tenor.com/view/gif-21466512", "https://tenor.com/view/lillo-lillodance-ballo-balletto-dance-gif-21194918", "https://tenor.com/view/sono-lillo-lillo-gif-21191597", "https://tenor.com/view/lillo-sono-lillo-so-lillo-amazon-amazonprime-gif-21194920", "https://tenor.com/view/lillo-mago-magic-lol-lol-italia-gif-21194915", "https://tenor.com/view/lillo-sono-lillo-so-lillo-amazon-amazonprime-gif-21194920", "https://tenor.com/view/elio-lol-gif-21134579", "https://tenor.com/view/elio-lol-chi-ride%c3%a8fuori-lol-elio-gif-21111371", "https://tenor.com/view/elio-cazzimiei-lol-gif-21110573", "https://tenor.com/view/elio-hey-ehi-gif-21216346", "https://tenor.com/view/kalo9603-lillo-lol-lol-chi-ride%c3%a8fuori-cos-gif-21175216", "https://tenor.com/view/pintus-haicagato-lolitalia-gif-21064228", "https://tenor.com/view/elio-tip-tap-lol-elio-ele-storie-tese-chi-ride%c3%a8fuori-gif-21144052", "https://tenor.com/view/lol-chi-ride-fuori-ciro-caterina-guzzanti-bottiglia-gif-21081670", "https://tenor.com/view/ciro-capriello-lol-chi-ride%c3%a8fuori-ciro-priello-the-jackal-ciro-gif-21300834", "https://tenor.com/view/lol-lolchiride%c3%a8fuori-fru-thejackal-mannaggia-gif-21136564", "https://tenor.com/view/frank-matano-lol-chi-ride%c3%a8fuori-lol-frank-matano-gif-arrabbiato-gif-21301241", "https://tenor.com/view/lolitalia-lol-frankmatano-thejackal-fru-gif-21085835"," https://tenor.com/view/lolchirideefuori-elio-lol-gif-21091310", "https://tenor.com/view/matano-lol-pintus-cazzo-buona-gif-21085489", "https://tenor.com/view/stefano-belisari-lol-chi-ride%c3%a8fuori-elio-elio-lol-lol-gif-21300886", "https://tenor.com/view/lol-chi-ride-efuori-caterina-guzzanti-wtf-gif-21028898", "https://tenor.com/view/lol-chi-ride-efuori-katia-follesa-shock-gif-21028894", "https://tenor.com/view/katia-follesa-junior-bake-off-eh-head-shaking-swaying-gif-15804462", "https://tenor.com/view/ciro-capriello-ciro-priello-risata-ridere-ciro-gif-21300942", "https://tenor.com/view/lol-lillo-chi-ride-fuori-gif-21190341"]

@Bot.command()
async def Documentazione(ctx):
    await ctx.send(f'{ctx.message.author.mention}, eccoti la mia documentazione!')
    await ctx.send("")#Qui dovrò mettere il link di GitHub dove metterò il file
    await ctx.send(f"""Il mio codice sorgente è scritto in `Python 3.9.1`, e utilizza i seguenti comandi da moduli a libera licenza:

Da `random.py`:
`random.choice()`
`random.randint()`

Da `asyncio.py`:
`asyncio.sleep()`

Da `discord.py`:
`discord.client`
`discord.commands`
`discord.errors`
""")

@Bot.command()
@commands.has_role('Diodesperado')
async def Cambia_stato(ctx, tempo, nuovo_stato):
    nuovo_stato = discord.Game(str(nuovo_stato))
    await Bot.change_presence(status = discord.Status.idle, activity = nuovo_stato)
    tempo = float(tempo)
    await sleep(tempo)
    await Bot.change_presence(status = discord.Status.idle, activity = gioco)

@Bot.command()
@commands.has_role('Diodesperado')
async def Ripristina_stato(ctx):
    await Bot.change_presence(status = discord.Status.idle, activity = gioco)

@Bot.command()
async def Lillo(ctx):
    global lillo
    link = choice(lillo)
    await ctx.channel.send(link)

@Bot.command()
@commands.has_role('Diodesperado')
async def LILLO(ctx, ripetizioni):
    ripetizioni = int(ripetizioni)
    for i in range(ripetizioni):
        global lillo
        link = choice(lillo)
        await ctx.channel.send(link)

@Bot.command()
@commands.has_role('Diodesperado')
async def Aggiungi_link(ctx, link):
    global lillo
    lillo.append(link)
    print(f'{link} è stato aggiunto alla lista lillo dei link.')
    return

@Bot.command()
async def Casuale(ctx):
    nonciclopedia = "https://nonciclopedia.org/wiki/Speciale:PaginaCasuale/"
    wikipedia = "https://it.wikipedia.org/wiki/Speciale:PaginaCasuale/"
    numero = randint(0, 30000)
    if numero < 15000:
        numero = str(numero)
        Pagina_Casuale = str(nonciclopedia + numero)
    elif numero > 14999:
        numero = str(numero)
        Pagina_Casuale = str(wikipedia + numero)
    await ctx.channel.purge(limit = 1)
    await ctx.send(Pagina_Casuale)

@Bot.command()
@commands.has_role('Diodesperado')
async def Scrivi(ctx, parola):
    await ctx.channel.purge(limit = 1)
    parola = parola.replace("-", " ", 100)
    await ctx.send(parola)

@Bot.command()
@commands.has_role('Diodesperado')
async def Espulsione(ctx, member:discord.user = None, motivo = None):
    if member == None:
        await ctx.message.reply(f'E chi vorresti espellere? (ripeti il comando senza omettere il membro da espellere)')
        return
    if motivo == None:
        await ctx.message.reply(f'E perché vorresti espellere {member.mention}?')
        return
    else:
        await member.kick()
        await ctx.send(f'Ho espulso {member.mention} su ordine di {ctx.message.author.mention}')
        print(f'Ho espulso {member.mention} su ordine di {ctx.message.author.mention}')
        await member.send(f'{member.mention}, sei stato espulso per il seguente motivo: {motivo}')
        return
    
@Bot.command()
@commands.has_role('Diodesperado')
async def Ostracizzazione(ctx, member:discord.user = None, motivo = None):
    if member == None:
        await ctx.message.reply(f'E chi vorresti ostracizzare? (ripeti il comando senza omettere il membro da bannare)')
        return
    if motivo == None:
        await ctx.message.reply(f'E perché vorresti espellere {member.mention}?')
        return
    else:
        await member.ban()
        await ctx.send(f'Ho espulso e bannato {member.mention} su ordine di {ctx.message.author.mention}')
        print(f'Ho bannato {member.mention} su ordine di {ctx.message.author.mention}')
        await member.send(f'{member.mention}, sei stato bannato per il seguente motivo: {motivo}')
        return
    
@Bot.command()
@commands.has_role('Diodesperado')
async def Avvertimento(ctx, member:discord.User = None, reason = None):
    if reason == None:
        await ctx.send('E per cosa lo staresti avvertendo?! Prova con £Avvertimento {member} parole-del-tuo-avvertimento')
    else:
        reason = reason.replace('-', ' ', 100)
        author = ctx.message.author
        await member.send(f"{member.mention}, la tua utenza è stata avvertita da {author}! Motivo: {reason}")
        await ctx.channel.send(f"Avvertimento inviato a {member}")

@Bot.command()
@commands.has_role('Diodesperado')
async def Cancella(ctx, quantità):
    quantità = int(quantità)
    await ctx.channel.purge(limit = quantità)
    await ctx.send(f'Ho cancellato {quantità} messaggi su ordine di {ctx.message.author.mention}')
    await ctx.message.author.send(f'{ctx.message.author.mention}, ho cancellato come richiesto i tuoi {quantità} messaggi nel canale {ctx.channel}')
    print(f'Ho cancellato {quantità} messaggi in {ctx.channel} su ordine di {ctx.message.author}.')
    return

@Bot.command()
async def Anonimo(ctx, member:discord.User = None, messaggio = None):
    await ctx.channel.purge(limit = 1)
    if messaggio == None:
        await ctx.send(f"E che messaggio staresti mandando?! Prova con *$Anonimo {member} parole-del-tuo-messaggio*")
    else:
        messaggio = messaggio.replace('-', ' ', 100)
        author = ctx.message.author
        await member.send(f"{member}, ti recapito un messaggio in anonimo!")
        await member.send(f"{messaggio}")
        await author.send(f"Messaggio inviato a {member}, :white_check_mark: ")
        await author.send(f"Messaggio: {messaggio}")

@Bot.command()
@commands.has_role('Diodesperado')
async def Aggiungi_Ruolo(ctx, user: discord.Member, role: discord.Role):
    await ctx.message.delete()
    await user.add_roles(role)
    await ctx.send(f"Ho aggiunto il ruolo {role.mention} all'utente {user.mention}.")
    print(f"Ho aggiunto il ruolo {role.mention} all'utente {user.mention}.")
    return

@Bot.command()
@commands.has_role('Diodesperado')
async def Togli_Ruolo(ctx, user: discord.Member, role: discord.Role):
    await ctx.message.delete()
    await user.remove_roles(role)
    await ctx.send(f"Ho rimosso il ruolo {role.mention} all'utente {user.mention}.")
    print(f"Ho rimosso il ruolo {role.mention} all'utente {user.mention}.")
    return

@Bot.command()
@commands.has_role('Diodesperado')
async def Spam(ctx, contatore, frase):
    try:
        contatore = int(contatore)
    except TypeError:
        await ctx.send(f'{ctx.message.author.mention}, inserisci un numero intero di ripetizioni')
    frase = frase.replace('-', ' ', 10000)
    await ctx.channel.purge(limit = 1)
    for i in range(contatore):
        await ctx.send(frase)
    await ctx.send(f'(**Spam** di {contatore} messaggi eseguita per conto di {ctx.message.author.mention})')

offese = [" ce l'hai corto",  " tua madre si sta ancora pentendo del mancato aborto", " sei così brutto che se mai avrai una ragazza dovrà essere così miope da poterti scambiare per un rettile", " parli come un'aspirante Barbara d'Urso"]
@Bot.command()
@commands.has_role('Diodesperado')
async def Offendi(ctx, utente):
    await ctx.channel.purge(limit = 1)
    await ctx.send(f'{utente},' + choice(offese))

@Bot.command()
@commands.has_role('Diodesperado')
async def Aggiungi_offesa(ctx, offesa):
    global offese
    offesa = offesa.replace("-", " ", 100)
    offese.append(offesa)
    print(f'{offesa} è stata aggiunta alla lista offese')
    await ctx.send(offesa)

@Bot.command()
async def Aiuto(ctx):
    Aiuto = str(f"""I comandi utilizzabili da tutti sono:
`£Aiuto` :joy:

`£Lillo` :thumbsup:

`£Anonimo @Destinatario parole-del-messaggio`

`£Casuale`

Usa `£Aiuto_Diodesperado` per la lista dei comandi limitati agli amministratori

QUESTO MESSAGGIO DI AIUTO VA COMPLETATO""")
    await ctx.message.reply(Aiuto)
    await ctx.send(f'Elenco dei comandi richiesto da {ctx.message.author.mention}')
    print(f'Elenco dei comandi richiesto da {ctx.message.author.mention}')
    return

@Bot.command()
async def Aiuto_Diodesperado(ctx):
    Comandi_elìte = (f"""I comandi disponibili solo per gli amministratori sono i seguenti:

`£LILLO quantità`

`£Aggiungi_link https://LINK`

`£Scrivi parole-del-messaggio`

`£Cancella quantità`

`£Spam quantità parole-da-spammare`

`£Offendi @Membro`

`£Aggiungi_offesa parole-dell'offesa`

`£Avvertimento @Destinatario parole-dell'avvertimento` :warning:

`£Espulsione @Membro ragione-dell'espulsione`

`£Ostracizzazione @Membro ragione-del-ban`

`£Aggiungi_Ruolo @Membro @Ruolo`

`£Togli_Ruolo @Membro @Ruolo`

`£Cambia_stato tempo(secondi) parole-del-nuovo-stato`

`£Ripristina stato`
""")
    await ctx.message.reply(Comandi_elìte)
    await ctx.send(f'Elenco dei comandi richiesto da {ctx.message.author.mention}')
    print(f'Elenco dei comandi richiesto da {ctx.message.author.mention}')

Bot.run(token)

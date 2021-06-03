from random import choice, randint
from asyncio import sleep
import discord
from discord.ext.commands.errors import MissingRole
from discord.ext.commands.errors import MissingPermissions
from discord.ext import commands
from discord import client

print("Papocchio.py")
token = ""
intents = discord.Intents().all()
Bot = commands.Bot(command_prefix = ")", description = "Ciao, sono Papocchio-Bot, mi occupo di gestione nel server di Nonciclopedia. Trovi la mia documentazione con )Documentazione", intents = intents)

#Comandi cazzoni e abbastanza inutili

@Bot.command()
@commands.has_role('nonciclopediano verificato')
async def Casuale(ctx):
    nonciclopedia = "https://nonciclopedia.org/wiki/Speciale:PaginaCasuale/"
    numero = randint(0, 15000)
    numero = str(numero)
    Pagina_Casuale = str(nonciclopedia + numero)
    await ctx.message.reply(Pagina_Casuale)

@Bot.command()
@commands.has_role('nonciclopediano verificato')
async def Nonciclopedia(ctx, pagina):
    nonciclopedia = "https://nonciclopedia.org/wiki/"
    await ctx.message.reply(nonciclopedia + pagina)

@Bot.command(description = "Comando per modificare il mio stato per un determinato arco di tempo.")
@commands.has_role('nonciclopediano rullatore')
async def Cambia_stato(ctx, secondi, nuovo_stato):
    try:
        nuovo_stato = nuovo_stato.replace('-', ' ', 1000)
        nuovo_stato = discord.Game(str(nuovo_stato))
        await Bot.change_presence(status = discord.Status.idle, activity = nuovo_stato)
        await ctx.message.reply(f"{ctx.message.author.mention} ha cambiato il mio stato per il tempo di {secondi} secondi")
        tempo = float(secondi)
        await sleep(tempo)
        await Bot.change_presence(status = discord.Status.idle, activity = gioco)
    except discord.errors.MissingRole:
        await ctx.message.reply(f"{ctx.message.author.mention}, mi dispiace, ma per eseguire questo comando è necessario il ruolo di nonciclopediano rullatore")

@Bot.command()
@commands.has_role('nonciclopediano verificato')
async def Anonimo(ctx, member:discord.User = None, messaggio = None):
    await ctx.message.delete()
    messaggio = messaggio.replace('-', ' ', 100)
    author = ctx.message.author
    await member.send(f"{member}, ti recapito un messaggio in anonimo!")
    await member.send(f"{messaggio}")
    await author.send(f"Messaggio inviato a {member}, :white_check_mark: ")
    await author.send(f"Messaggio: {messaggio}")

global offese
offese = [" ce l'hai corto",  " tua madre si sta ancora pentendo del mancato aborto", " sei così brutto che se mai avrai una ragazza dovrà essere così miope da poterti scambiare per un rettile", " parli come un'aspirante Barbara d'Urso"]
@Bot.command()
@commands.has_role('nonciclopediano verificato')
async def Offendi(ctx, utente:discord.User):
    try:
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'{utente.mention},' + choice(offese))
    except discord.ext.commands.errors.MissingRole:
        await ctx.message.reply(f"{ctx.message.author.mention}, mi dispiace, ma per eseguire questo comando è necessario il ruolo Diodesperado")

@Bot.command()
@commands.has_role('nonciclopediano verificato')
async def Aggiungi_offesa(ctx, *args):
    for parola in args:
        offesa += parola
    try:
        offesa = offesa.replace("-", " ", 100)
        offese.append(offesa)
        print(f'({offesa}) è stata aggiunta alla lista offese')
        await ctx.send((f"(***{offesa}***) è stata aggiunta alla lista offese"))
    except discord.errors.MissingRole:
        await ctx.message.reply(f"{ctx.message.author.mention}, mi dispiace, ma per eseguire questo comando è necessario il ruolo di nonciclopediano verificato")

@Bot.command()
async def Scrivi(ctx, *parole):
    await ctx.message.delete()
    frase = str('')
    for parola in parole:
        parola += ' '
        frase += parola
    await ctx.send(frase)

@Bot.command()
async def Cancella(ctx, quantità:int):
    await ctx.channel.purge(limit = quantità)
    await ctx.send("Sono stati eliminati {quantità} messaggi per conto di {ctx.message.author.mention}!")

@Bot.command()
@commands.has_role('nonciclopediano verificato')
async def Spam(ctx, ripetizioni:int, *parole):
    await ctx.message.delete()
    frase = str('')
    for parola in parole:
        parola += ' '
        frase += parola
    for i in range(ripetizioni):
        await ctx.send(frase)
    await ctx.send(f"Spam di {ripetizioni} messaggi effettuata per conto di {ctx.message.author.mention}")

@Bot.command(description = "Decidi quante notifiche mandare per rompere il cazzo allo sfortunato di turno. Se non specificherai un numero allora sarò costretto a deciderlo io...")
@commands.has_role('nonciclopediano picciotto')
async def Importuna(ctx, utonto:discord.Member, ripetizioni = None, messaggio_privato = None):
    await ctx.message.delete()
    if (ripetizioni == None):
        for i in range(randint(1, 10)):
            await ctx.send(f"{utonto.mention}")
        if (messaggio_privato == None):
            return
        else:
            messaggio = messaggio_privato.replace('-', ' ', 10000)
            await utonto.send(f"{utonto.mention}, {ctx.author} vuole che tu torni online, per cui ti ha lasciato questo messaggio: ")
            await utonto.send(f"> *{messaggio}*")
            return
    ripetizioni = int(ripetizioni)
    for i in range(ripetizioni):
        await ctx.send(f"{utonto.mention}")
    if (messaggio_privato == None):
        return
    else:
        messaggio = messaggio = messaggio_privato.replace('-', ' ', 10000)
        await utonto.send(f"{utonto.mention}, {ctx.author} vuole che tu torni online, per cui ti ha lasciato questo messaggio: ")
        await utonto.send(f"> *{messaggio}*")
        return

#Comandi tattici per la gestione dei nonciclopediani

@Bot.command()
@commands.has_role('nonciclopediano rullatore')
async def Avvertimento(ctx, utente:discord.User, motivo = None):
    try:
        if motivo == None:
            await ctx.send('E per cosa lo staresti avvertendo?! Prova con `)Avvertimento {utente.mention} parole-del-tuo-avvertimento`')
        else:
            reason = motivo.replace('-', ' ', 100)
            author = ctx.message.author
            await utente.send(f"{utente.mention}, la tua utenza è stata avvertita da {author}! Motivo: {reason}")
            await ctx.channel.send(f"Avvertimento inviato a {utente.mention}")
    except discord.errors.Forbidden:
        await ctx.message.reply(f'{ctx.message.author.mention}, non ho il potere di farlo')

@Bot.command()
@commands.has_role('nonciclopediano amministratore')
async def Calciorotazione(ctx, utente:discord.User, motivo = None):
    if (motivo != None):
        motivo = str(motivo.replace('-', ' ', 1000))
        await ctx.message.reply(f"Ho provato ad espellere quel caprone di {utente.mention}!")
        try:
            await utente.kick(reason = motivo)
            await ctx.send(f"E ce l'ho fatta! Quel dispotico di {ctx.message.author.mention} è stato accontentato.")
        except discord.error.Forbidden:
            await ctx.send(f"Purtroppo però non ci sono riuscito...")
        await utente.send(f"Sei stato espulso da parte di {ctx.message.author.nick} per il seguente motivo:")
        await utente.send(motivo)
    if (motivo == None):
        await utente.send(f"Sei stato espulso dal server perché così sbatteva a {ctx.message.author.nick}")

@Bot.command(description = "Per dare un po' di tempo al ciccione di turno per lamentarsi dell'espulsione in avvicinamento. Inserire un tempo minimo di 15 secondi.")
@commands.has_role('nonciclopediano amministratore')
async def Calciorotazione_con_countdown(ctx, utente:discord.Member, motivo = None, offesa = None, secondi = None, countdown = None):
    if (secondi == None):
        await Calciorotazione(ctx, utente)
        return
    secondi = float(secondi)
    countdown = bool(countdown)
    if (secondi != None and countdown):
        if (secondi < 15):
            await ctx.message.reply(f"Scrivi `)help Calciorotazione_con_countdown`, forse capisci come mai ~~sei ritardato~~ il comando non ha funzionato.")
            return
        await ctx.send(f"{utente.mention}, ti rimangono {str(secondi)} secondi da trascorrere in questo server.")
        await sleep(secondi-10)
        await ctx.send(f"{utente.mention}, ti rimangono 10 secondi da trascorrere in questo server.")
        for i in range(10):
            await sleep(1)
            await ctx.send(str(10-i))
        if (offesa == None):
            await ctx.message.reply(f"Ho provato ad espellere quel caprone di {utente.mention}!")
        else:
            await ctx.message.reply(f"Ho provato ad espellere quel {offesa} di {utente.mention}!")
        try:
            await utente.kick(reason = motivo)
            await ctx.send(f"E ce l'ho fatta! Quel dispotico di {ctx.message.author.mention} è stato accontentato.")
        except discord.errors.Forbidden:
            await ctx.send(f"Purtroppo però non ci sono riuscito...")
        return

#Comandi sulla gestione del Bot

@Bot.command()
@commands.has_role('nonciclopediano amministratore')
async def FERMO(ctx):
    await ctx.send('Hai usato il comando )FERMO, il mio programma in file `.exe` si arresterà in automatico, per riattivarmi contatta @FLAK_FLAK)3241')
    await quit()

#Comandi sulle informazioni

@Bot.command(aliases = ["info", "Info", "informazioni"], description = "Le informazioni fondamentali del Bot.")
async def Informazioni(ctx):
    numero_server = len(Bot.guilds)
    quantità_utenti = len(ctx.guild.members)
    await ctx.send(f"Sono in {numero_server} server.")
    await ctx.send(f"Trovi la lista dei miei server con `)Lista_server`.")
    await ctx.send(f"Posso vedere {quantità_utenti} utenti.")
    await ctx.send(f"Trovi la lista dei miei server con `)Lista_utenti`. Purtroppo quest'ultimo comando non funziona.")

@Bot.command(description = "Lista dei server dei quali faccio parte.")
async def Lista_server(ctx):
    numero_server = len(Bot.guilds)
    await ctx.send(f"Eccoti la lista dei {numero_server} server dei quali faccio parte:")
    Lista = ""
    for guild in Bot.guilds:
        Lista += f"""{guild.name}
"""
    await ctx.send(Lista)

Bot.run(token)

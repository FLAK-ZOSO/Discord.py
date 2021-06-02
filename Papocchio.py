from random import choice, randint
from asyncio import sleep
import discord
from discord.ext.commands.errors import MissingRole
from discord.ext.commands.errors import MissingPermissions
from discord.ext import commands
from discord import client

print("Papocchio.py")
token = "ODQ5Njg5ODI0MjgxMTAwMzU4.YLe1UA.Wg29Lyl1yG_URtKScOU1vk7irXc"
#intents = discord.Intents().all()
#, intents = intents
Bot = commands.Bot(command_prefix = "#", description = "Ciao, sono Papocchio-Bot, mi occupo di gestione nel server di Nonciclopedia. Trovi la mia documentazione con #Documentazione")
gioco = discord.Game("#Aiuto | Papocchio | @Papocchio#9166")

@Bot.event
async def on_ready():
    print(Bot.user, " è ora online ", "ID: ", Bot.user.id)
    await Bot.change_presence(status = discord.Status.idle, activity = gioco)

#Comandi cazzoni e abbastanza inutili

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
    await ctx.message.delete()
    await ctx.send(Pagina_Casuale)

@Bot.command()
async def Nonciclopedia(ctx):
    nonciclopedia = "https://nonciclopedia.org/wiki/Speciale:PaginaCasuale/"
    numero = randint(0, 15000)
    numero = str(numero)
    Pagina_Casuale = str(nonciclopedia + numero)
    await ctx.message.reply(Pagina_Casuale)

@Bot.command(description = "Comando per modificare il mio stato per un determinato arco di tempo.")
@commands.has_role('Autorizzato a Talker')
async def Cambia_stato(ctx, secondi, nuovo_stato):
    try:
        nuovo_stato = nuovo_stato.replace('-', ' ', 1000)
        nuovo_stato = discord.Game(str(nuovo_stato))
        await Bot.change_presence(status = discord.Status.idle, activity = nuovo_stato)
        await ctx.message.reply(f"{ctx.message.author.mention} ha cambiato il mio stato per il tempo di {secondi} secondi")
        tempo = float(secondi)
        await sleep(tempo)
        await Bot.change_presence(status = discord.Status.idle, activity = gioco)
    except discord.ext.commands.errors.MissingRole:
        await ctx.message.reply(f"{ctx.message.author.mention}, mi dispiace, ma per eseguire questo comando è necessario il ruolo Autorizzato a Talker")

@Bot.command()
async def Anonimo(ctx, member:discord.User = None, messaggio = None):
    await ctx.message.delete()
    messaggio = messaggio.replace('-', ' ', 100)
    author = ctx.message.author
    await member.send(f"{member}, ti recapito un messaggio in anonimo!")
    await member.send(f"{messaggio}")
    await author.send(f"Messaggio inviato a {member}, :white_check_mark: ")
    await author.send(f"Messaggio: {messaggio}")

@Bot.command()
async def Scrivi(ctx, *args):
    await ctx.message.delete()
    frase = str('')
    for parola in args:
        parola += ' '
        frase += parola
    await ctx.send(frase)

#Comandi tattici per la gestione dei nonciclopediani

@Bot.command()
@commands.has_role('Diodesperado')
async def Avvertimento(ctx, member:discord.User, reason = None):
    try:
        if reason == None:
            await ctx.send('E per cosa lo staresti avvertendo?! Prova con `£Avvertimento {member} parole-del-tuo-avvertimento`')
        else:
            reason = reason.replace('-', ' ', 100)
            author = ctx.message.author
            await member.send(f"{member.mention}, la tua utenza è stata avvertita da {author}! Motivo: {reason}")
            await ctx.channel.send(f"Avvertimento inviato a {member}")
    except discord.errors.Forbidden:
        await ctx.message.reply(f'{ctx.message.author.mention}, non ho il potere di farlo')

@Bot.command()
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
async def Calciorotazione_con_countdown(ctx, utente:discord.User, motivo = None, secondi = None, countdown = None):
    if (secondi == None):
        await Calciorotazione(ctx, utente)
        return
    secondi = float(secondi)
    countdown = bool(countdown)
    if (secondi != None and countdown):
        if (secondi < 15):
            await ctx.message.reply(f"Scrivi `a`#help Calciorotazione_con_countdown`, forse capisci come mai ~~sei ritardato~~ il comando non ha funzionato.")
        await ctx.send(f"{utente.mention}, ti rimangono {str(secondi)} secondi da trascorrere in questo server.")
        await sleep(secondi-10)
        await ctx.send(f"{utente.mention}, ti rimangono 10 secondi da trascorrere in questo server.")
        for i in range(10):
            await sleep(1)
            await ctx.send(str(10-i))
        await ctx.message.reply(f"Ho provato ad espellere quel caprone di {utente.mention}!")
        try:
            await utente.kick(reason = motivo)
            await ctx.send(f"E ce l'ho fatta! Quel dispotico di {ctx.message.author.mention} è stato accontentato.")
        except discord.error.Forbidden:
            await ctx.send(f"Purtroppo però non ci sono riuscito...")
        return

#Comandi sulle informazioni

@Bot.command(aliases = ["info", "Info", "informazioni"], description = "Le informazioni fondamentali del Bot.")
async def Informazioni(ctx):
    numero_server = len(Bot.guilds)
    quantità_utenti = len(ctx.guild.members)
    await ctx.send(f"Sono in {numero_server} server.")
    await ctx.send(f"Trovi la lista dei miei server con `#Lista_server`.")
    await ctx.send(f"Posso vedere {quantità_utenti} utenti.")
    await ctx.send(f"Trovi la lista dei miei server con `#Lista_utenti`. Purtroppo quest'ultimo comando non funziona.")

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

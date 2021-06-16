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
prefixes = (")", "()")
Bot = commands.Bot(command_prefix = prefixes, description = "Ciao, sono Papocchio-Bot, mi occupo di gestione nel server di Nonciclopedia. Trovi la mia documentazione con )Documentazione", intents = intents)
gioco = discord.Game(""")Aiuto | Papocchio | @Papocchio#9166""")

#Comandi cazzoni e abbastanza inutili

@Bot.command()
@commands.has_role('nonciclopediano verificato')
async def Casuale(ctx):
    await ctx.message.delete()
    nonciclopedia = "https://nonciclopedia.org/wiki/Speciale:PaginaCasuale/"
    numero = randint(0, 15000)
    numero = str(numero)
    Pagina_Casuale = str(nonciclopedia + numero)
    embed = discord.Embed()
    embed.color = discord.Color.random()
    embed.description = f"{ctx.message.author.mention} mi ha chiesto una pagina casuale di nonciclopedia, eccovela:"
    await ctx.send(embed=embed)
    await ctx.send(Pagina_Casuale)

@Bot.command()
@commands.has_role('nonciclopediano verificato')
async def Nonciclopedia(ctx, pagina):
    nonciclopedia = "https://nonciclopedia.org/wiki/"
    await ctx.message.reply(nonciclopedia + pagina)

@Bot.command()
@commands.has_role('nonciclopediano verificato')
async def Wikipedia(ctx, pagina):
    nonciclopedia = "https://it.wikipedia.org/wiki/"
    await ctx.message.reply(nonciclopedia + pagina)

@Bot.command(description = "Comando per modificare il mio stato per un determinato arco di tempo.")
@commands.has_role('nonciclopediano verificato')
async def Cambia_stato(ctx, secondi, *nuovo_stato):
    stato = str('')
    for parola in nuovo_stato:
        parola += " "
        stato += parola
    nuovo_stato = discord.Game(str(stato))
    await Bot.change_presence(status = discord.Status.idle, activity = nuovo_stato)
    embed = discord.Embed(description = f"""{ctx.message.author.mention} ha cambiato il mio stato per il tempo di {secondi} secondi.
Ecco la stronzata che mi ha rifilato come stato:""", color = discord.Color.red())
    await ctx.message.reply(embed = embed)
    await ctx.message.delete()
    embed = discord.Embed(description = f"{nuovo_stato}", color = discord.Color.red())
    await ctx.send(embed = embed)
    tempo = float(secondi)
    await sleep(tempo)
    await Bot.change_presence(status = discord.Status.idle, activity = gioco)

@Bot.command(description = "Un messaggio in anonimo per rompere il cazzo al deficiente di turno.")
@commands.has_role('nonciclopediano verificato')
async def Anonimo(ctx, utonto:discord.Member, *Messaggio):
    await ctx.message.delete()
    messaggio = str('')
    for parola in Messaggio:
        parola += ' '
        messaggio += parola
    messaggio = messaggio[:(len(messaggio)-1)]
    author = ctx.message.author
    await utonto.send(embed = discord.Embed(description = f"{utonto.mention}, ti recapito un messaggio in anonimo:"))
    await utonto.send(f"*{messaggio}*")
    await author.send(embed = discord.Embed(description = f"Messaggio inviato a {utonto}, :white_check_mark: "))
    await author.send(f"Messaggio: *{messaggio}*")

global offese
offese = [" vorrei trombarmi tua cugina (perché non c'è cosa più divina), vuoi farti da parte?", " sei così orripilante che in confronto <:jumboface:845028213910798346> è sexy", " tua sorella è così zoccola che Berlusconi le ha dato un posto al senato", " ce l'hai corto",  " tua madre si sta ancora pentendo del mancato aborto", " sei così brutto che se mai avrai una ragazza dovrà essere così miope da poterti scambiare per un rettile", " parli come un'aspirante Barbara d'Urso"]
@Bot.command(aliases = ["offendi"])
@commands.has_role('nonciclopediano verificato')
async def Offendi(ctx, utente:discord.User):
    try:
        await ctx.message.delete()
        await ctx.send(embed = discord.Embed(description = f'{utente.mention},' + choice(offese), color = discord.Color.random()))
    except discord.ext.commands.errors.MissingRole:
        await ctx.message.reply(f"{ctx.message.author.mention}, mi dispiace, ma per eseguire questo comando è necessario il ruolo nonciclopediano verificato")

@Bot.command()
@commands.has_role('nonciclopediano verificato')
async def Aggiungi_offesa(ctx, *Offesa):
    await ctx.message.delete()
    offesa = str(' ')
    for parola in Offesa:
        parola += ' '
        offesa += parola
    offesa = offesa[:(len(offesa)-1)]
    try:
        offesa = offesa.replace("-", " ", 100)
        offese.append(offesa)
        print(f'({offesa}) è stata aggiunta alla lista offese')
        colore = discord.Color.random()
        await ctx.send(embed = discord.Embed(description = f"{ctx.message.author.mention} mi ha chiesto di aggiungere alla lista offese la seguente:", color = colore))
        await ctx.send(embed = discord.Embed(description = f"***{offesa}***", color = colore))
    except discord.errors.MissingRole:
        await ctx.message.reply(f"{ctx.message.author.mention}, mi dispiace, ma per eseguire questo comando è necessario il ruolo di nonciclopediano verificato")

@Bot.command(aliases = ["scrivi"])
async def Scrivi(ctx, *parole):
    await ctx.message.delete()
    frase = str('')
    for parola in parole:
        parola += ' '
        frase += parola
    await ctx.send(frase)

@Bot.command(aliases = ["cancella"])
async def Cancella(ctx, quantità:int):
    await ctx.channel.purge(limit = quantità)
    await ctx.send(embed = discord.Embed(description = f"Sono stati eliminati {quantità} messaggi per conto di {ctx.message.author.mention}!", color = discord.Color.blurple()))

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
    await ctx.send(embed = discord.Embed(description = f"Spam di {ripetizioni} messaggi effettuata per conto di {ctx.message.author.mention}"))

@Bot.command(description = "Decidi quante notifiche mandare per rompere il cazzo allo sfortunato di turno. Se non specificherai un numero allora sarò costretto a deciderlo io...")
@commands.has_role('nonciclopediano verificato')
async def Importuna(ctx, utonto:discord.Member, ripetizioni = None, *messaggio_privato):
    await ctx.message.delete()
    if (ripetizioni == None):
        for i in range(randint(1, 10)):
            await ctx.send(f"{utonto.mention}")
        if (messaggio_privato == None):
            return
        else:
            messaggio = str('')
            for i in messaggio_privato:
                i += ' '
                messaggio += i
            messaggio = messaggio[:(len(messaggio)-1)]
            await utonto.send(embed = discord.Embed(description = f"""{ctx.author.mention} **__pretende__** che tu torni online, per cui ti ha lasciato un messaggio:
> *{messaggio}*""", color = discord.Color.red()))
            return
    ripetizioni = int(ripetizioni)
    for i in range(ripetizioni):
        await ctx.send(f"{utonto.mention}")
    if (messaggio_privato == None):
        return
    else:
        messaggio = str('')
        for i in messaggio_privato:
            i += ' '
            messaggio += i
        messaggio = messaggio[:(len(messaggio)-1)]
        await utonto.send(embed = discord.Embed(description = f"""{ctx.author.mention} **__pretende__** che tu torni online, per cui ti ha lasciato un messaggio:
> *{messaggio}*""", color = discord.Color.red()))
        return

#Comandi tattici per la gestione dei nonciclopediani

@Bot.command()
@commands.has_role('nonciclopediano rullatore')
async def Avvertimento(ctx, utente:discord.User, motivo = None):
    try:
        if motivo == None:
            await ctx.message.reply(embed = discord.Embed(description = f'E per cosa lo staresti avvertendo?! Prova con `)Avvertimento {utente.mention} parole-del-tuo-avvertimento`', color = discord.Color.dark_red()))
        else:
            reason = motivo.replace('-', ' ', 100)
            author = ctx.message.author
            await utente.send(embed = discord.Embed(description = f"{utente.mention}, la tua utenza è stata avvertita da {author}! Motivo: {reason}", title = "AVVERTIMENTO", color = discord.Color.dark_red()))
            await ctx.channel.send(embed = discord.Embed(description = f"Avvertimento inviato a {utente.mention} :white_check_mark:", color = discord.Color.dark_red()))
    except discord.errors.Forbidden:
        await ctx.message.reply(f'{ctx.message.author.mention}, non ho il potere di farlo')

@Bot.command()
@commands.has_role('nonciclopediano amministratore')
async def Calciorotazione(ctx, utente:discord.Member, *Motivo):
    await ctx.message.delete()
    if (Motivo != None):
        motivo = str('')
        for parola in Motivo:
            parola += ' '
            motivo += parola
        motivo = motivo[:(len(motivo)-1)]
        await ctx.send(embed = discord.Embed(description = f"Ho provato ad espellere quel caprone di {utente.mention}", color = discord.Color.dark_orange()))
        try:
            await utente.kick(reason = motivo)
            await ctx.send(embed = discord.Embed(description = f"""E ce l'ho fatta! Quel dispotico di {ctx.message.author.mention} è stato accontentato""", color = discord.Color.dark_orange()))
        except discord.errors.Forbidden:
            await ctx.send(f"Purtroppo però non ci sono riuscito...")
        await utente.send(embed = discord.Embed(description = f"""Sei stato espulso da parte di {ctx.message.author.nick} per il seguente motivo:
{motivo}""", color = discord.Color.dark_orange(), title = "CALCIOROTAZIONE"))
    if (Motivo == None):
        await utente.send(embed = discord.Embed(description = f"Sei stato espulso dal server perché così sbatteva a {ctx.message.author.mention}", color = discord.Color.dark_orange()))

@Bot.command(description = "Per dare un po' di tempo al ciccione di turno per lamentarsi dell'espulsione in avvicinamento. Inserire un tempo minimo di 15 secondi.", aliases = ["CCC"])
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

@Bot.command(aliases = ["AR", "aggiungi_ruolo", "Aggiungi_ruolo"])
async def Aggiungi_Ruolo(ctx, ruolo:discord.Role, utente:discord.Member):
    await ctx.message.delete()
    try:
        await utente.add_roles(ruolo)
    except discord.errors.Forbidden:
        await ctx.send(embed = discord.Embed(description = f"{ctx.message.author.mention}, non ho i poteri per assegnare quel ruolo. Per farlo dev'essere un ruolo inferiore al più alto dei miei.", color = discord.Color.random()))
        return
    finally:
        await ctx.send(embed = discord.Embed(description = f"Ho aggiunto il ruolo {ruolo.mention} a {utente.mention} su richesta di {ctx.message.author.mention}", color = discord.Color.random()))

@Bot.command(aliases = ["RR", "rimuovi_ruolo", "Rimuovi_ruolo"])
async def Rimouvi_Ruolo(ctx, ruolo:discord.Role, utente:discord.Member):
    await ctx.message.delete()
    try:
        await utente.remove_roles(ruolo)
    except discord.errors.Forbidden:
        await ctx.send(embed = discord.Embed(description = f"{ctx.message.author.mention}, non ho i poteri per rimuovere quel ruolo. Per farlo dev'essere un ruolo inferiore al più alto dei miei.", color = discord.Color.random()))
        return
    finally:
        await ctx.send(embed = discord.Embed(description = f"Ho tolto il ruolo {ruolo.mention} a {utente.mention} su richesta di {ctx.message.author.mention}", color = discord.Color.random()))

@Bot.command(description = "Con questo comando puoi fare una gentile concessione al nonciclopediano di turno, regalandogli per un numero di secondi limitato un ruolo a tua scelta, di modo da capire fino a che punto possa esserne immeritevole")
@commands.has_role('nonciclopediano amministratore')
async def Concessione(ctx, ruolo:discord.Role, utente:discord.Member, secondi:float):
    try:
        await utente.add_roles(ruolo)
    except discord.errors.Forbidden:
        await ctx.send(embed = discord.Embed(description = f"""{ctx.message.author.mention}, non sono riuscito a dare il ruolo {ruolo.mention} a {utente.mention} perché il ruolo richiesto non è inferiore al mio.
                       Peggio per quel deficiente di {utente.mention}, si è perso {secondi} secondi di divertimento!""", color = discord.Color.dark_green()))
        return
    await ctx.send(embed = discord.Embed(description = f"""{utente.mention}, eccoti in regalo da {ctx.message.author.mention} il ruolo {ruolo.mention}.
Goditelo, perché tra {secondi} secondi non sarà più tuo.""", color = discord.Color.dark_green()))
    await sleep(secondi)
    await ctx.send(f"{utente.mention}, spero che tu ti sia divertito finché sei stato {ruolo.mention}, perché i {secondi} secondi gentilmente concessi da {ctx.message.author.mention} sono scaduti, e mo' t'attacchi al cazzo.")
    await utente.remove_roles(ruolo)

#Comandi sulla gestione del Bot

@Bot.command()
@commands.has_role('nonciclopediano amministratore')
async def FERMO(ctx):
    await ctx.send('Hai usato il comando `)FERMO`, il mio programma in file `.exe` si arresterà in automatico, per riattivarmi contatta `@FLAK_FLAK#3241`')
    await quit()

#Comandi sulle informazioni

@Bot.command(aliases = ["info", "Info", "informazioni"], description = "Le informazioni fondamentali del Bot.")
async def Informazioni(ctx):
    numero_server = len(Bot.guilds)
    quantità_utenti = len(ctx.guild.members)
    #lista_server = str('')
    #for membro in ctx.guild.members:
    #   server = membro.guilds
    #   lista_server += membro
    #   lista_server += server
    await ctx.send(f"Sono in {numero_server} server.")
    await ctx.send(f"Trovi la lista dei miei server con `)Lista_server`.")
    await ctx.send(f"Posso vedere {quantità_utenti} utenti.")
    await ctx.send(f"Trovi la lista dei miei server con `)Lista_utenti`.")
    #await ctx.send(f"In tutto i componenti di questo server fanno parte di {len(lista_server)} server.")
    #await ctx.send(f"Trovi la lista dei server degli utenti con `)Lista_server_utenti`")

@Bot.command(description = "Lista dei server dei quali faccio parte.")
async def Lista_server(ctx):
    numero_server = len(Bot.guilds)
    await ctx.send(f"Eccoti la lista dei {numero_server} server dei quali faccio parte:")
    Lista = ""
    for guild in Bot.guilds:
        Lista += f"""{guild.name}
"""
    await ctx.send(Lista)

@Bot.command(description = "Lista degli utenti di questo server.")
async def Lista_utenti(ctx):
    numero_utenti = len(ctx.guild.members)
    await ctx.send(f"Eccoti la lista dei {numero_utenti} utenti che vedo:")
    Lista = ""
    for member in ctx.guild.members:
        if (member.nick != None):
            Lista += f"""{member.nick}   ({member})
"""
        if (member.nick == None):
            Lista += f"""{member}    ({member})
"""
    await ctx.send(Lista)

@Bot.command(description = "Lista dei vari utenti del server con i relativi server. Non esiste l'attributo `member.guilds`, per cui non può restituire informazioni. Il comando andrà eliminato.")
@commands.has_role('nonciclopediano verificato')
async def Lista_server_utenti(ctx):
    lista_server = str('')
    for membro in ctx.guild.members:
        server = membro.guilds
        lista_server += str(f"""{membro}
{server}
""")
    await ctx.send(f"lista_server")

Bot.run(token)

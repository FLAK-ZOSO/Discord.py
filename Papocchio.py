from random import choice, randint
from asyncio import sleep
from discord import Status, Game, Intents, Member, User, Role, Embed, Color, File
from discord.ext.commands.errors import MissingRole, MissingPermissions
from discord.errors import Forbidden
from discord.ext import commands
from discord import client

print("Papocchio.py")
token = "Don't rob me"
intents = Intents().all()
prefixes = (")", "()", "<:Papocchio:849018580426555473> ", "<:Papocchio:849018580426555473>", ")(", "@Papocchio#9166", "@Papocchio")
Bot = commands.Bot(command_prefix = prefixes, description = "Ciao, sono Papocchio-Bot, mi occupo di gestione nel server di Nonciclopedia. Trovi la mia documentazione con )Documentazione", intents = intents)
gioco = Game(""")Aiuto | Papocchio | @Papocchio#9166""")

@Bot.event
async def on_ready():
    print(Bot.user, " è ora online ", "ID: ", Bot.user.id)
    await Bot.change_presence(status = Status.online, activity = gioco)

#Comandi cazzoni e abbastanza inutili

@Bot.command()
@commands.has_role('nonciclopediano verificato')
async def Casuale(ctx):
    await ctx.message.delete()
    nonciclopedia = "https://nonciclopedia.org/wiki/Speciale:PaginaCasuale/"
    numero = randint(0, 15000)
    numero = str(numero)
    Pagina_Casuale = str(nonciclopedia + numero)
    embed = Embed()
    embed.color = Color.random()
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
    nuovo_stato = Game(str(stato))
    await Bot.change_presence(status = Status.online, activity = nuovo_stato)
    embed = Embed(description = f"""{ctx.message.author.mention} ha cambiato il mio stato per il tempo di {secondi} secondi.
Ecco la stronzata che mi ha rifilato come stato:""", color = Color.red())
    await ctx.message.reply(embed = embed)
    await ctx.message.delete()
    embed = Embed(description = f"{nuovo_stato}", color = Color.red())
    await ctx.send(embed = embed)
    tempo = float(secondi)
    await sleep(tempo)
    await Bot.change_presence(status = Status.online, activity = gioco)

@Bot.command(description = "Un messaggio in anonimo per rompere il cazzo al deficiente di turno.")
@commands.has_role('nonciclopediano verificato')
async def Anonimo(ctx, utonto:Member, *Messaggio):
    await ctx.message.delete()
    messaggio = str('')
    for parola in Messaggio:
        parola += ' '
        messaggio += parola
    messaggio = messaggio[:(len(messaggio)-1)]
    author = ctx.message.author
    await utonto.send(embed = Embed(description = f"{utonto.mention}, ti recapito un messaggio in anonimo:"))
    await utonto.send(f"*{messaggio}*")
    await author.send(embed = Embed(description = f"Messaggio inviato a {utonto}, :white_check_mark: "))
    await author.send(f"Messaggio: *{messaggio}*")

global offese
offese = ["vorrei trombarmi tua cugina (perché non c'è cosa più divina), vuoi farti da parte?", "sei così orripilante che in confronto <:jumboface:845028213910798346> è sexy", "tua sorella è così zoccola che Berlusconi le ha dato un posto al senato", "ce l'hai corto",  "tua madre si sta ancora pentendo del mancato aborto", "sei così brutto che se mai avrai una ragazza dovrà essere così miope da poterti scambiare per un rettile", "parli come un'aspirante Barbara d'Urso"]
@Bot.command(aliases = ["offendi"])
@commands.has_role('nonciclopediano verificato')
async def Offendi(ctx, utente:User):
    try:
        await ctx.message.delete()
        await ctx.send(embed = Embed(description = f'{utente.mention}, ' + choice(offese), color = Color.random()))
    except MissingRole:
        await ctx.message.reply(f"{ctx.message.author.mention}, mi dispiace, ma per eseguire questo comando è necessario il ruolo nonciclopediano verificato")

@Bot.command()
@commands.has_role('nonciclopediano verificato')
async def Aggiungi_offesa(ctx, *Offesa):
    await ctx.message.delete()
    offesa = str('')
    for parola in Offesa:
        parola += ' '
        offesa += parola
    offesa = offesa[:(len(offesa)-1)]
    try:
        offesa = offesa.replace("-", " ", 100)
        offese.append(offesa)
        print(f'({offesa}) è stata aggiunta alla lista offese')
        colore = Color.random()
        await ctx.send(embed = Embed(description = f"{ctx.message.author.mention} mi ha chiesto di aggiungere alla lista offese la seguente:", color = colore))
        await ctx.send(embed = Embed(description = f"***{offesa}***", color = colore))
    except MissingRole:
        await ctx.message.reply(f"{ctx.message.author.mention}, mi dispiace, ma per eseguire questo comando è necessario il ruolo di nonciclopediano verificato")

@Bot.command()
@commands.has_role('nonciclopediano verificato')
async def Lista_offese(ctx):
    await ctx.message.delete()
    colore = Color.random()
    await ctx.send(embed = Embed(description = f"{ctx.message.author.mention} ha richiesto la corrente lista delle offese.", title = "LISTA OFFESE", color = colore))
    await ctx.send(embed = Embed(description = f"*{offese}*", color = colore))
    await ctx.message.author.send(embed = Embed(description = "Hai richiesto la lista delle offese", title = "LISTA OFFESE", color = colore))
    await ctx.message.author.send(embed = Embed(description = f"*{offese}*", color = colore))

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
    await ctx.send(embed = Embed(description = f"Sono stati eliminati {quantità} messaggi per conto di {ctx.message.author.mention}!", color = Color.blurple()))

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
    await ctx.send(embed = Embed(description = f"Spam di {ripetizioni} messaggi effettuata per conto di {ctx.message.author.mention}"))

@Bot.command(aliases = ["Embed"], description = "Invia un embed per conto di un nonciclopediano. Il colore va codificato in RGB. L'immagine va scritta come link. Il file dev'essere presente nel dispositivo dell'host..")
@commands.has_role('nonciclopediano verificato')
async def EMBED(ctx, titolo:str, descrizione:str, colore = None, immagine = None, file = None, nome_file = None):
    await ctx.message.delete()
    titolo = titolo.replace('-', ' ')
    descrizione = descrizione.replace('-', ' ')
    embed = Embed(title = titolo, description = descrizione, color = Color.default())
    if (colore != None):
        colore = Color.from_rgb(int(colore[:2]), int(colore[2:4]), int(colore[4:]))
        embed = Embed(title = titolo, description = descrizione, color = colore)
    if (immagine != None):
        embed.set_image(url = immagine)
    if (file != None):
        file = File(fp = file)
        if (nome_file != None):
            file = File(fp = file, filename = nome_file)
    await ctx.send(embed = embed)
    await ctx.message.author.send(embed = Embed(title = "EMBED", description =f"{ctx.message.author.mention}, ho inviato nel canale {ctx.channel} il tuo embed"))

@Bot.command()
async def HelloWorld(ctx, linguaggio):
    await ctx.message.delete()
    linguaggio = str(linguaggio)
    
    if (linguaggio == "python" or linguaggio == "py" or linguaggio == "Python"):
        script = "print('Hello World')"
    if (linguaggio == "ruby" or linguaggio == "Ruby" or "ruby" in linguaggio or "Ruby" in linguaggio):
        script = "puts 'Hello World'"
    if (linguaggio == "c++" or linguaggio == "C++" or "C++" in linguaggio or "c++" in linguaggio):
        script = """cout << "Hello World";"""
    if (linguaggio == "javascript" or linguaggio == "js" or linguaggio == "JavaScript"):
        script = "document.Get_Element_By_Id('your ass').innerHTML = 'Hello World';"
    else:
        script = """'Hello World'"""
        
    script = f"""```{linguaggio}
{script}```"""
    embed = Embed(title = f"{linguaggio}", description = script)
    await ctx.send(embed = embed)

@Bot.command()
async def Attacca(ctx, ID:int):
    await ctx.message.delete()
    messaggio = await ctx.fetch_message(ID)
    await messaggio.pin()
    embed = Embed(title = "MESSAGGIO ATTACCATO", description = f"Ho attaccato il seguente messaggio su ordine di {ctx.message.author.mention}.", color = Color.blue())
    await ctx.send(embed = embed)
    informazioni_messaggio = Informazioni_messaggio_offline(messaggio)
    embed = Embed(title = "MESSAGGIO:", description = informazioni_messaggio, color = Color.blue())
    await ctx.send(embed = embed)

def Informazioni_messaggio_offline(messaggio):
    informazioni = f""" **ID**: {messaggio.id}
** Link**: {messaggio.jump_url}
 
 **Autore**: {messaggio.author.mention} ({messaggio.author})
 **Orario**: {messaggio.created_at}
 **Canale**: {messaggio.guild}
"""

    if (messaggio.pinned):
        informazioni += f"\n **Messaggio attaccato**: Sì"
    if not(messaggio.pinned):
        informazioni += f"\n **Messaggio attaccato**: No"
    
    if (messaggio.reference != None):
        informazioni += f"\n **Messaggio risposto**: {messaggio.reference.message_id}"
    if (messaggio.reference == None):
        informazioni += f"\n **Messaggio risposto**: nessuno"
    
    informazioni += f"\n **Contenuto**: {messaggio.content}"
    
    if (messaggio.raw_mentions != []):
        informazioni += f"\n **Menzioni**: {messaggio.raw_mentions}"
    if (messaggio.raw_role_mentions != []):
        informazioni += f"\n **Ruoli menzionati**: {messaggio.raw_role_mentions}"
    if (messaggio.raw_channel_mentions != []):
        informazioni += f"\n **Canali menzionati**: {messaggio.raw_channel_mentions}"
    if (messaggio.reactions != []):
        emoji = ""
        for i in messaggio.reactions:
            emoji += f"{i} "
        informazioni += f"\n **Reazioni**: {emoji}"
    
    return informazioni

@Bot.command()
async def Informazioni_messaggio(ctx, ID:int):
    await ctx.message.delete()
    embed = Embed(title = "INFORMAZIONI MESSAGGIO:", description = Informazioni_messaggio_offline(await ctx.fetch_message(ID)), color = Color.blue())
    await ctx.send(embed = embed)

@Bot.command()
async def Digita(ctx, secondi:float):
    await ctx.message.delete()
    async with ctx.typing():
        await sleep(secondi)

#Comandi tattici per la gestione dei nonciclopediani
    
@Bot.command(description = "Decidi quante notifiche mandare per rompere il cazzo allo sfortunato di turno. Se non specificherai un numero allora sarò costretto a deciderlo io...")
@commands.has_role('nonciclopediano verificato')
async def Importuna(ctx, utonto:Member, ripetizioni = None, *messaggio_privato):
    await ctx.message.delete()
    if (ripetizioni == None):
        for i in range(randint(1, 10)):
            if (utonto.status == Status.online):
                await ctx.send(embed = Embed(description = f"{utonto.mention} è già online, arriverà a momenti.", color = Color.green()))
                break
            await ctx.send(f"{utonto.mention}")
        if (messaggio_privato == None):
            return
        else:
            messaggio = str('')
            for i in messaggio_privato:
                i += ' '
                messaggio += i
            messaggio = messaggio[:(len(messaggio)-1)]
            await utonto.send(embed = Embed(description = f"""{ctx.author.mention} **__pretende__** che tu torni online, per cui ti ha lasciato un messaggio:
> *{messaggio}*""", color = Color.red()))
            return
    ripetizioni = int(ripetizioni)
    for i in range(ripetizioni):
        if (utonto.status == Status.online):
            await ctx.send(embed = Embed(description = f"{utonto.mention} è già online, arriverà a momenti.", color = Color.green()))
            break
        await ctx.send(f"{utonto.mention}")
    if (messaggio_privato == None):
        return
    else:
        messaggio = str('')
        for i in messaggio_privato:
            i += ' '
            messaggio += i
        messaggio = messaggio[:(len(messaggio)-1)]
        await utonto.send(embed = Embed(description = f"""{ctx.author.mention} **__pretende__** che tu torni online, per cui ti ha lasciato un messaggio:
> *{messaggio}*""", color = Color.red()))
        return

@Bot.command()
@commands.has_role('nonciclopediano rullatore')
async def Avvertimento(ctx, utente:User, motivo = None):
    try:
        if motivo == None:
            await ctx.message.reply(embed = Embed(description = f'E per cosa lo staresti avvertendo?! Prova con `)Avvertimento {utente.mention} parole-del-tuo-avvertimento`', color = Color.dark_red()))
        else:
            reason = motivo.replace('-', ' ', 100)
            author = ctx.message.author
            await utente.send(embed = Embed(description = f"{utente.mention}, la tua utenza è stata avvertita da {author}! Motivo: {reason}", title = "AVVERTIMENTO", color = Color.dark_red()))
            await ctx.channel.send(embed = Embed(description = f"Avvertimento inviato a {utente.mention} :white_check_mark:", color = Color.dark_red()))
    except Forbidden:
        await ctx.message.reply(f'{ctx.message.author.mention}, non ho il potere di farlo')

@Bot.command()
@commands.has_role('nonciclopediano amministratore')
async def Calciorotazione(ctx, utente:Member, *Motivo):
    await ctx.message.delete()
    if (Motivo != None):
        motivo = str('')
        for parola in Motivo:
            parola += ' '
            motivo += parola
        motivo = motivo[:(len(motivo)-1)]
        await ctx.send(embed = Embed(description = f"Ho provato ad espellere quel caprone di {utente.mention}", color = Color.dark_orange()))
        try:
            await utente.kick(reason = motivo)
            await ctx.send(embed = Embed(description = f"""E ce l'ho fatta! Quel dispotico di {ctx.message.author.mention} è stato accontentato""", color = Color.dark_orange()))
        except Forbidden:
            await ctx.send(f"Purtroppo però non ci sono riuscito...")
        await utente.send(embed = Embed(description = f"""Sei stato espulso da parte di {ctx.message.author.nick} per il seguente motivo:
{motivo}""", color = Color.dark_orange(), title = "CALCIOROTAZIONE"))
    if (Motivo == None):
        await utente.send(embed = Embed(description = f"Sei stato espulso dal server perché così sbatteva a {ctx.message.author.mention}", color = Color.dark_orange()))

@Bot.command(description = "Per dare un po' di tempo al ciccione di turno per lamentarsi dell'espulsione in avvicinamento. Inserire un tempo minimo di 15 secondi.", aliases = ["CCC"])
@commands.has_role('nonciclopediano amministratore')
async def Calciorotazione_con_countdown(ctx, utente:Member, secondi:float, motivo = None, offesa = None):
    await ctx.message.delete()
    if (secondi != None):
        if (secondi < 15):
            await ctx.send(embed = Embed(description = f"Scrivi `)help Calciorotazione_con_countdown`, forse capisci come mai ~~sei ritardato~~ il comando non ha funzionato.", color = Color.red(), title = f"{ctx.message.author.nick}, UN COGLIONE"))
            return
        if (round(secondi) == secondi):
            await ctx.send(embed = Embed(description = f"{utente.mention}, ti rimangono {str(int(secondi))} secondi da trascorrere in questo server.", color = Color.red()))
        else:
            await ctx.send(embed = Embed(description = f"{utente.mention}, ti rimangono {str(secondi)} secondi da trascorrere in questo server.", color = Color.red()))
        await sleep(secondi-10)
        await ctx.send(embed = Embed(description = f"{utente.mention}, ti rimangono 10 secondi da trascorrere in questo server.", color = Color.red()))
        for i in range(10):
            await sleep(1)
            await ctx.send(embed = Embed(description = f"{str(10-i)}", color = Color.red()))
        if (offesa == None):
            await ctx.send(embed = Embed(description = f"Ho provato ad espellere quel caprone di {utente.mention}!", color = Color.red()))
        else:
            await ctx.send(embed = Embed(description = f"Ho provato ad espellere quel {offesa} di {utente.mention}!", color = Color.red()))
        try:
            await utente.kick(reason = motivo)
            await ctx.send(embed = Embed(description = f"E ce l'ho fatta! Quel dispotico di {ctx.message.author.mention} è stato accontentato.", color = Color.red()))
        except Forbidden:
            await ctx.send(embed = Embed(description = f"Purtroppo però non ci sono riuscito...", color = Color.red()))
        return

@Bot.command(aliases = ["AR", "aggiungi_ruolo", "Aggiungi_ruolo"])
async def Aggiungi_Ruolo(ctx, ruolo:Role, utente:Member):
    await ctx.message.delete()
    try:
        await utente.add_roles(ruolo)
    except Forbidden:
        await ctx.send(embed = Embed(description = f"{ctx.message.author.mention}, non ho i poteri per assegnare quel ruolo. Per farlo dev'essere un ruolo inferiore al più alto dei miei.", color = Color.random()))
        return
    await ctx.send(embed = Embed(description = f"Ho aggiunto il ruolo {ruolo.mention} a {utente.mention} su richesta di {ctx.message.author.mention}", color = Color.random()))

@Bot.command(aliases = ["RR", "rimuovi_ruolo", "Rimuovi_ruolo"])
async def Rimouvi_Ruolo(ctx, ruolo:Role, utente:Member):
    await ctx.message.delete()
    try:
        await utente.remove_roles(ruolo)
    except Forbidden:
        await ctx.send(embed = Embed(description = f"{ctx.message.author.mention}, non ho i poteri per rimuovere quel ruolo. Per farlo dev'essere un ruolo inferiore al più alto dei miei.", color = Color.random()))
        return
    await ctx.send(embed = Embed(description = f"Ho tolto il ruolo {ruolo.mention} a {utente.mention} su richesta di {ctx.message.author.mention}", color = Color.random()))

@Bot.command(description = "Con questo comando puoi fare una gentile concessione al nonciclopediano di turno, regalandogli per un numero di secondi limitato un ruolo a tua scelta, di modo da capire fino a che punto possa esserne immeritevole")
@commands.has_role('nonciclopediano amministratore')
async def Concessione(ctx, ruolo:Role, utente:Member, secondi:float):
    await ctx.message.delete()
    try:
        await utente.add_roles(ruolo)
    except Forbidden:
        await ctx.send(embed = Embed(description = f"""{ctx.message.author.mention}, non sono riuscito a dare il ruolo {ruolo.mention} a {utente.mention} perché il ruolo richiesto non è inferiore al mio.
                       Peggio per quel deficiente di {utente.mention}, si è perso {secondi} secondi di divertimento!""", color = Color.dark_green()))
        return
    await ctx.send(embed = Embed(description = f"""{utente.mention}, eccoti in regalo da {ctx.message.author.mention} il ruolo {ruolo.mention}.
Goditelo, perché tra {secondi} secondi non sarà più tuo.""", color = Color.dark_green()))
    await sleep(secondi)
    await ctx.send(embed = Embed(description = f"{utente.mention}, spero che tu ti sia divertito finché sei stato {ruolo.mention}, perché i {secondi} secondi gentilmente concessi da {ctx.message.author.mention} sono scaduti, e mo' t'attacchi al cazzo.", color = Color.dark_green()))
    await utente.remove_roles(ruolo)

#Comandi sulla gestione del Bot

@Bot.command()
@commands.has_role('nonciclopediano amministratore')
async def FERMO(ctx):
    await ctx.message.delete()
    await ctx.send(embed = Embed(description = f'Hai usato il comando `)FERMO`, il mio programma in file `.exe` si arresterà in automatico, per riattivarmi contatta `@FLAK_FLAK#3241`', color = Color.default(), title = f"{ctx.message.author.nick} MI HA FERMATO"))
    await quit()

#Comandi sulle informazioni

@Bot.command(aliases = ["info", "Info", "informazioni"], description = "Le informazioni fondamentali del Bot.")
async def Informazioni(ctx):
    await ctx.message.delete()
    numero_server = len(Bot.guilds)
    quantità_utenti = len(ctx.guild.members)
    #lista_server = str('')
    #for membro in ctx.guild.members:
    #   server = membro.guilds
    #   lista_server += membro
    #   lista_server += server
    color = Color.random()
    await ctx.send(embed = Embed(description = f"{ctx.message.author.mention}, ha richiesto le informazioni di cui dispongo:", color = color))
    description = f"""
Sono in {numero_server} server
Posso vedere {quantità_utenti} utenti
"""
    title = f"INFORMAZIONI"
    embed = Embed(description = description, title = title, color = color)
    await ctx.send(embed = embed)
    description = f"""
Trovi la lista dei miei server con `)Lista_server`
Trovi la lista degli utenti con `)Lista_utenti`"""
    title = f"ALTRO"
    embed = Embed(description = description, title = title, color = color)
    await ctx.send(embed = embed)
    #await ctx.send(f"In tutto i componenti di questo server fanno parte di {len(lista_server)} server.")
    #await ctx.send(f"Trovi la lista dei server degli utenti con `)Lista_server_utenti`")

@Bot.command(description = "Lista dei server dei quali faccio parte.")
async def Lista_server(ctx):
    numero_server = len(Bot.guilds)
    color = Color.random()
    await ctx.send(embed = Embed(description = f"{ctx.message.author.mention}, eccoti la lista dei {numero_server} server dei quali faccio parte:", color = color))
    Lista = ""
    for guild in Bot.guilds:
        Lista += f"""{guild.name}
"""
    await ctx.send(embed = Embed(description = Lista, color = color, title = "LISTA SERVER"))

@Bot.command(description = "Lista degli utenti di questo server.")
async def Lista_utenti(ctx):
    numero_utenti = len(ctx.guild.members)
    color = Color.random()
    await ctx.send(embed = Embed(description = f"{ctx.message.author.mention}, eccoti la lista dei {numero_utenti} utenti che vedo:", color = color))
    Lista = ""
    for member in ctx.guild.members:
        if (member.nick != None):
            Lista += f"""{member.nick}   ({member})
"""
        if (member.nick == None):
            Lista += f"""{member}    ({member})
"""
    await ctx.send(embed = Embed(description = Lista, color = color, title = "LISTA UTENTI"))

@Bot.command(description = "Lista dei vari utenti del server con i relativi server. Non esiste l'attributo `member.guilds`, per cui non può restituire informazioni. Il comando andrà eliminato.") #Tanto non funziona, non so perchéccazzo lo tengo qui
@commands.has_role('nonciclopediano verificato')
async def Lista_server_utenti(ctx):
    lista_server = str('')
    for membro in ctx.guild.members:
        server = membro.guilds
        lista_server += str(f"""{membro}
{server}
""")
    await ctx.send(f"lista_server")

@Bot.command()
async def Documentazione(ctx):
    await ctx.message.delete()
    messaggio = f"""{ctx.message.author.mention} ha richiesto il mio codice sorgente:
https://github.com/FLAK-ZOSO/Discord.py/blob/Papocchio/Papocchio.py"""
    await ctx.send(embed = Embed(title = "DOCUMENTAZIONE", description = messaggio, color = Color.lighter_gray()))
    await ctx.message.author.send(embed = Embed(title = "DOCUMENTAZIONE", description = "Hai richiesto il mio file sorgente, te lo invio qui sotto.", color = Color.lighter_gray()))
    await ctx.message.author.send(file = File(r"C:\Users\mattia\papocchio.py"))
    print(f"{ctx.message.author} ha richiesto la mia documentazione")
    await sleep(15)
    embed = Embed(title = "ATTENZIONE", description = "Se fai stronzate col mio token lo verrò a sapere, il Papocchio ti osserva:", color = Color.red())
    embed.set_image(url = "https://static.miraheze.org/nonciclopediawiki/c/cd/Papocchio_2000x2000.png")
    await ctx.message.author.send(embed = embed)

Bot.run(token)

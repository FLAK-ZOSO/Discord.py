from random import choice, randint
from asyncio import sleep
from discord import Status, Game, Intents, Member, User, Role, Embed, Color, File
from discord.utils import get
from discord.ext.commands.errors import MissingRole, MissingPermissions, CommandInvokeError
from discord.errors import Forbidden, NotFound, HTTPException
from discord.ext import commands
from discord import client

print("Papocchio.py")
token = "Sapessih"
intents = Intents().all()
prefixes = (")", "()", "<:Papocchio:849018580426555473> ", "<:Papocchio:849018580426555473>", ")(", "@Papocchio#9166", "@Papocchio")
ids = ["797844636281995274"]
Bot = commands.Bot(command_prefix = prefixes, owner_ids = ids, description = "Ciao, sono Papocchio-Bot, mi occupo di gestione nel server di Nonciclopedia. Trovi la mia documentazione con )Documentazione", intents = intents)
gioco = Game(""")Aiuto | Papocchio | @Papocchio#9166""")

@Bot.event
async def on_ready():
    print(Bot.user, " è ora online ", "ID: ", Bot.user.id)
    await Bot.change_presence(status = Status.online, activity = gioco)
    for i in Bot.get_all_channels():
        if i.category == "cazzeggio" and i.name == "generale":
            i.send("Sono tornato!")

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

@Bot.command(description = "Comando per modificare la mia attività per un determinato arco di tempo.")
@commands.has_role('nonciclopediano verificato')
async def Cambia_attività(ctx, secondi, *nuova_attività):
    stato = str('')
    for parola in nuova_attività:
        parola += " "
        stato += parola
    nuovo_stato = Game(str(stato))
    await Bot.change_presence(status = Status.online, activity = nuovo_stato)
    embed = Embed(description = f"""{ctx.message.author.mention} ha cambiato il mio stato per il tempo di {secondi} secondi.
Ecco la stronzata che mi ha rifilato come stato:""", color = Color.green())
    await ctx.send(embed = embed)
    await ctx.message.delete()
    embed = Embed(description = f"{nuovo_stato}", color = Color.green())
    await ctx.send(embed = embed)
    tempo = float(secondi)
    await sleep(tempo)
    await Bot.change_presence(status = Status.online, activity = gioco)

@Bot.command(description = "Comando per modificare il mio stato per un determinato arco di tempo.")
async def Cambia_stato(ctx, secondi:float, stato):
    await ctx.message.delete()
    try:
        await Bot.change_presence(status = stato_da_nome(stato))
    except ValueError:
        await ctx.send(embed = Embed(title = "ERRORE", description = f"""{ctx.message.author.mention}, il valore che hai inserito per il parametro stato non è convertibile in uno stato, riprova con un valore più plausibile di "{stato}", grazie"""))
    await ctx.send(embed = Embed(title = stato.upper(), description = f"Ho impostato lo stato {stato} per {round(secondi)} secondi. \n Non chiedetemi perché, qui è {ctx.message.author.mention} che comanda...", color = colore_da_stato(stato)))
    await sleep(secondi)
    await Bot.change_presence(status = Status.online, activity = gioco)
    await ctx.send(embed = Embed(title = "BACK IN GREEN", description = "Dopo aver cambiato stato per {} secondi, sono tornato".format(round(secondi)), color = Color.green()))

def stato_da_nome(stato):
    if (stato == "online" or stato == "Online" or stato == "on" or stato == "On" or stato == "ON"):
        return Status.online
    if (stato == "idle" or stato == "Idle" or stato == "inattivo" or stato == "Inattivo"):
        return Status.idle
    if (stato == "offline" or stato == "Offline" or stato == "off" or stato == "Off" or stato == "OFF"):
        return Status.offline
    if (stato == "non disturbare" or stato == "Non disturbare" or stato == "do not disturb" or stato == "DND" or stato == "dnd"):
        return Status.dnd
    if (stato == "invisible" or stato == "Invisible" or stato == "invisibile" or stato == "Invisibile"):
        return Status.invisible
    else:
        raise ValueError(f"Il valore {stato} non è utilizzabile per il parametro stato")

def colore_da_stato(stato):
    stato = stato_da_nome(stato)
    if (stato == Status.online):
        return Color.green()
    if (stato == Status.idle):
        return Color.orange()
    if (stato == Status.offline):
        return Color.magenta()
    if (stato == Status.dnd):
        return Color.red()
    if (stato == Status.invisible):
        return Color.light_gray()
    else:
        raise ValueError(f"Il valore {stato} non è utilizzabile per il parametro stato")

@Bot.command()
async def Stealth(ctx, secondi:float):
    await ctx.message.delete()
    await ctx.send(embed = Embed(title = "STEALTH", description = f"Su ordine di {ctx.message.author.mention} mi fingerò offline per {round(secondi)} secondi", color = Color.default()))
    await Bot.change_presence(status = Status.invisible, afk = True)
    await sleep(secondi)
    await ctx.send(embed = Embed(title = "BACK IN GREEN", description = "Dopo essermi nascosto per {} secondi, sono tornato".format(round(secondi)), color = Color.green()))
    await Bot.change_presence(status = Status.online, activity = gioco, afk = False)
    
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

@Bot.command()
async def Scrivi_con_attesa(ctx, secondi:float, *parole):
    await ctx.message.delete()
    frase = str('')
    for parola in parole:
        parola += ' '
        frase += parola
    async with ctx.typing():
        await sleep(secondi)
    await ctx.send(frase)

@Bot.command()
async def Scrivi_a_velocità(ctx, caratteri_al_secondo:int, *parole):
    pass

@Bot.command()
async def Scrivi_come_utente(ctx, *parole):
    await ctx.message.delete()
    frase = str('')
    for parola in parole:
        parola += ' '
        frase += parola
    secondi = (frase.count(' ')+1)
    async with ctx.typing():
        await sleep(secondi)
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
    async with ctx.typing():
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
    try:
        embed = Embed(title = "INFORMAZIONI MESSAGGIO:", description = Informazioni_messaggio_offline(await ctx.fetch_message(ID)), color = Color.blue())
    except CommandInvokeError:
        await ctx.send(embed = Embed(title = "MESSAGGIO NON TROVATO", description = f"Il messaggio con ID {ID} non esiste, oppure è già stato cancellato", color = Color.red()))
        return
    except NotFound:
        await ctx.send(embed = Embed(title = "MESSAGGIO NON TROVATO", description = f"Il messaggio con ID {ID} non esiste, oppure è già stato cancellato", color = Color.red()))
        return
    except HTTPException:
        await ctx.send(embed = Embed(title = "MESSAGGIO NON TROVATO", description = f"Il messaggio con ID {ID} non esiste, oppure è già stato cancellato", color = Color.red()))
        return
    await ctx.send(embed = embed)

@Bot.command()
async def Digita(ctx, secondi:float):
    await ctx.message.delete()
    async with ctx.typing():
        await sleep(secondi)

@Bot.command()
async def LegalizeDrugsAndMurder(ctx):
    await ctx.message.delete()
    embed = Embed(title = "LEGALIZE DRUGS AND MURDER")
    embed.set_image(url = choice(['https://www.ticketone.it/obj/media/IT-eventim/galery/222x222/e/electric-wizard-biglietti.jpg', 'http://4.bp.blogspot.com/-qrCRffBfn9U/UYRFym1TPpI/AAAAAAAAAns/pcB-uzVmw9w/s1600/ewblackmass.jpg', 'https://metalitalia.com/wp-content/uploads/2014/07/electric-wizard-band-2014.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdaursX4QPwoD5dauWtbQ-eoZQ-nmmcXR-GA&usqp=CAU', 'https://metalitalia.com/wp-content/uploads/2018/08/electric-wizard-band-2018.jpeg', 'https://www.ocanerarock.com/sally/wp-content/uploads/2018/11/Electric-Wizard.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwC_APEw7jKsLMevW8oBzUCxN2jHh4RPJG2Q&usqp=CAU', 'https://www.lascimmiapensa.com/wp-content/uploads/2017/11/electricwizardband2017_638.jpg', 'https://media.resources.festicket.com/www/artists/ElectricWizard.jpg', 'http://3.bp.blogspot.com/-C_bW7rSHa8o/TYIpgM_qFXI/AAAAAAAAI_c/aAlVGlsEAIU/s1600/Electric%2BWizard.jpg', 'https://media.stubcloudstatic.com/stubhub-catalog/d_defaultLogo.jpg/t_f-fs-0fv,q_auto:low,f_auto,c_fill,$w_750_mul_3,$h_416_mul_3/performer/700245/r1k5aeangqrftshro5hp', 'https://cdn.wegow.com/media/artists/electric-wizard/electric-wizard-1492555854.33.2560x1440.jpg', 'https://lastfm.freetls.fastly.net/i/u/avatar170s/9f0e22d9f6064320bedfde9b8112ad59', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwyrIxYbr3-8_tvv8coHpfXbnHQ-bb6Pezzg&usqp=CAU', 'https://static.wikia.nocookie.net/metal/images/0/03/ElectricWizard2013.jpg/revision/latest/scale-to-width-down/250?cb=20140310105648', 'https://note-store.com/upload/resize_cache/iblock/605/325_380_2/Electric-Wizard.png', 'https://upload.wikimedia.org/wikipedia/commons/d/d6/Electricwizard_LizBuckingham.jpg', 'https://www.metal.it/image.ashx?id=358&size=400&folder=group&suffix=photo&filters=square', 'https://lh3.googleusercontent.com/proxy/JAu3GMnf2yD_a7H-pSA_P1BEh9lXpfzhDupBUgLbT2OvuKFPn37ynIdIBUtT2SrrAYNfAKv9DTmWuUSrg9LOwzvIriP5lQVzFIO3re44EJg']))
    await ctx.send(embed = embed)

@Bot.command()
async def RobertaSammarelli(ctx):
    await ctx.message.delete()
    embed = Embed(title = "ROBERTA SAM(M)ARELLI")
    embed.set_image(url = choice(['https://rockitecn.nohup.it/fotouser/102895/verdena-roberta-sammarelli.jpg', 'https://images2-bergamo.corriereobjects.it/methode_image/2015/08/27/Bergamo/Foto%20Bergamo%20-%20Trattate/verdena-kTt-U43110492147391zcE-1224x916@Corriere-Web-Bergamo-593x443.jpg?v=20150827161913', 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/b3069b23-a844-4f45-8589-f32f580706ba/d11c0k7-006f5360-3b88-4f3e-9298-7986167e422f.jpg/v1/fill/w_600,h_801,q_75,strp/roberta_sammarelli_by_veergilicious_d11c0k7-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9ODAxIiwicGF0aCI6IlwvZlwvYjMwNjliMjMtYTg0NC00ZjQ1LTg1ODktZjMyZjU4MDcwNmJhXC9kMTFjMGs3LTAwNmY1MzYwLTNiODgtNGYzZS05Mjk4LTc5ODYxNjdlNDIyZi5qcGciLCJ3aWR0aCI6Ijw9NjAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.EcugiTErOSgl4HH41BB5EAhKBw9TC14jwzEO_koxxpU', 'https://live.staticflickr.com/6073/6086307279_6812bdf2cd_b.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMaIcXR2gcYnENaBcYgZfvhdxSxQfecLtG4Q&usqp=CAU', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs4tYJmoLnvGx6bacbc4XMEw80cIg7lJL3og&usqp=CAU', 'https://upload.wikimedia.org/wikipedia/commons/8/80/Roberta_Sammarelli_-_Modena_19-09-2007.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnhU5tMTkOEF8KlOi3L5dmf26ZyM3sDsXE6Q&usqp=CAU', 'https://rockitecn.nohup.it/fotouser/102918/verdena-roberta-sammarelli.jpg?v=843', 'http://2.bp.blogspot.com/-PLn-AtMJB5k/Vd8Oh4noIYI/AAAAAAAA3V4/vnjWHI28ofc/s1600/foto.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2NZQKsmu7yNLbVZsyWcQIDq-qqmPQCgedow&usqp=CAU']))
    await ctx.send(embed = embed)

@Bot.command()
async def Caparezza(ctx):
    await ctx.message.delete()
    embed = Embed(title = "CAPAREZZA ||tutt'altro che una carezza||")
    embed.set_image(url = choice(['https://cdn.discordapp.com/attachments/851839196742287380/869931327334518784/caparezza.png', 'https://cdn.discordapp.com/attachments/851839196742287380/869930713049354240/caparezza.png', 'https://cdn.discordapp.com/attachments/851839196742287380/869930601128546314/hqdefault.png', 'https://media.discordapp.net/attachments/851839196742287380/869929953314095114/image.png?width=320&height=320', 'https://notiziemusica.it/wp-content/uploads/2018/02/CS_CAPAREZZA.jpg.webp', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Caparezza_Italia_Wave.jpg/220px-Caparezza_Italia_Wave.jpg', 'https://www.alguer.it/img/Caparezza-3.jpg', 'https://sites.google.com/site/patagarruconiriccioli/_/rsrc/1461764265458/il-nuovo-caparezza/capa2.jpg', 'https://www.studionord.news/wp-content/uploads/2018/03/Caparezza.jpg']))
    await ctx.send(embed = embed)

#Comandi tattici per la gestione dei nonciclopediani

@Bot.command()
async def Permessi(ctx, utente:Member):
    await ctx.message.delete()
    p = utente.guild_permissions
    descrizione = ''
    descrizione += "Aggiungere reazioni: {}\n".format(p.add_reactions)
    descrizione += "Amministrare i canali: {}\n".format(p.manage_channels)
    descrizione += "Amministrare le emoji: {}\n".format(p.manage_emojis)
    descrizione += "Amministrare il server: {}\n".format(p.manage_guild)
    descrizione += "Amministrare i messaggi: {}\n".format(p.manage_messages)
    descrizione += "Amministrare i nickname: {}\n".format(p.manage_nicknames)
    descrizione += "Amministrare i permessi: {}\n".format(p.manage_permissions)
    descrizione += "Amministrare i ruoli: {}\n".format(p.manage_roles)
    descrizione += "Amministratore: {}\n".format(p.administrator)
    descrizione += "Allegare file: {}\n".format(p.attach_files)
    descrizione += "Bannare membri: {}\n".format(p.ban_members)
    descrizione += "Cambiare nickname: {}\n".format(p.change_nickname)
    descrizione += "Creare invito: {}\n".format(p.create_instant_invite)
    descrizione += "Espellere membri: {}\n".format(p.kick_members)
    descrizione += "Inviare link: {}\n".format(p.embed_links)
    descrizione += "Inviare messaggi: {}\n".format(p.send_messages)
    descrizione += "Leggere i messaggi: {}\n".format(p.read_messages)
    descrizione += "Leggere la cronologia: {}\n".format(p.read_message_history)
    descrizione += "Menzionare @everyone: {}\n".format(p.mention_everyone)
    descrizione = descrizione.replace('True', ':green_circle:')
    descrizione = descrizione.replace('False', ':red_circle:')
    embed = Embed(title = f"Permessi di {utente}", description = descrizione, color = Color.blue())
    await ctx.send(embed = Embed(description = f"{ctx.message.author.mention} ha richiesto i permessi di {utente.mention}", color = Color.blue()))
    await ctx.send(embed = embed)

#Aggiungere qui un comando riguardo le informazioni di un singolo utente

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
        await ctx.send(embed = Embed(description = f"{ctx.message.author.mention}, non ho i poteri per assegnare quel ruolo. Per farlo dev'essere un ruolo inferiore al più alto dei miei.", color = Color.green()))
        return
    await ctx.send(embed = Embed(description = f"Ho aggiunto il ruolo {ruolo.mention} a {utente.mention} su richesta di {ctx.message.author.mention}", color = Color.green()))

@Bot.command(aliases = ["RR", "rimuovi_ruolo", "Rimuovi_ruolo"])
async def Rimouvi_Ruolo(ctx, ruolo:Role, utente:Member):
    await ctx.message.delete()
    try:
        await utente.remove_roles(ruolo)
    except Forbidden:
        await ctx.send(embed = Embed(description = f"{ctx.message.author.mention}, non ho i poteri per rimuovere quel ruolo. Per farlo dev'essere un ruolo inferiore al più alto dei miei.", color = Color.red()))
        return
    await ctx.send(embed = Embed(description = f"Ho tolto il ruolo {ruolo.mention} a {utente.mention} su richesta di {ctx.message.author.mention}", color = Color.red()))

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

@Bot.command(aliases = ["KillYourself", "Suicide"])
@commands.has_permissions(administrator = True)
async def FERMO(ctx):
    await ctx.message.delete()
    await ctx.send(embed = Embed(description = f'Hai usato il comando `)FERMO`, il mio programma in file `.exe` si arresterà in automatico, per riattivarmi contatta `@FLAK_FLAK#3241`', color = Color.default(), title = f"{ctx.message.author.nick} MI HA FERMATO"))
    await quit()

@Bot.command()
@commands.has_role('nonciclopediano verificato')
async def SPENTO(ctx, secondi:float):
    await ctx.message.delete()
    embed = Embed(title = "SPENTO", description = f"{ctx.message.author.mention} mi ha spento per {round(secondi)} secondi", color = Color.red())
    await ctx.send(embed = embed)
    await Bot.close()
    await sleep(secondi)
    await Bot.login(token)
    embed = Embed(title = "ACCESO", description = f"Sono tornato dal letargo di {round(secondi)} impostomi da {ctx.message.author.mention}", color = Color.green())
    await ctx.send(embed = embed)
    
#Comandi sulle informazioni

@Bot.command()
async def Prefissi(ctx): #Da incorporare in un comando )Informazioni_Bot
    await ctx.message.delete()
    await ctx.send(embed = Embed(title = "PREFISSI", description = f"{ctx.message.author.mention}, eccoti i miei prefissi:"))
    await ctx.send(embed = Embed(description = prefixes))

@Bot.command(aliases = ["info", "Info", "informazioni"], description = "Le informazioni fondamentali del Bot.")
async def Informazioni(ctx): #Andrà ampliato con informazioni sul bot stesso
    await ctx.message.delete()
    numero_server = len(Bot.guilds)
    quantità_utenti = len(ctx.guild.members)
    quantità_ruoli = len(ctx.guild.roles)
    color = Color.random()
    await ctx.send(embed = Embed(description = f"{ctx.message.author.mention}, ha richiesto le informazioni di cui dispongo:", color = color))
    description = f"""
Sono in {numero_server} server
Posso vedere {quantità_utenti} utenti
Conosco {quantità_ruoli} ruoli
"""
    title = f"INFORMAZIONI"
    embed = Embed(description = description, title = title, color = color)
    await ctx.send(embed = embed)
    description = f"""
Trovi la lista dei miei server con `)Lista_server`
Trovi la lista degli utenti con `)Lista_utenti`
Trovi la lista dei ruoli con `)Lista_ruoli`"""
    title = f"ALTRO"
    embed = Embed(description = description, title = title, color = color)
    await ctx.send(embed = embed)

@Bot.command(description = "Lista dei server dei quali faccio parte.")
async def Lista_server(ctx):
    await ctx.message.delete()
    numero_server = len(Bot.guilds)
    color = Color.purple()
    await ctx.send(embed = Embed(description = f"{ctx.message.author.mention}, eccoti la lista dei {numero_server} server dei quali faccio parte:", color = color))
    Lista = ""
    for guild in Bot.guilds:
        Lista += f"""{guild.name}
"""
    await ctx.send(embed = Embed(description = Lista, color = color, title = "LISTA SERVER"))

@Bot.command(description = "Lista degli utenti di questo server.")
async def Lista_utenti(ctx):
    await ctx.message.delete()
    numero_utenti = len(ctx.guild.members)
    color = Color.purple()
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

@Bot.command()
async def Lista_ruoli(ctx):
    await ctx.message.delete()
    color = Color.purple()
    await ctx.send(embed = Embed(title = "LISTA RUOLI", description = f"{ctx.message.author.mention}, eccoti la lista dei {len(ctx.guild.roles)} ruoli di questo server:", color = color))
    Lista = ''
    for role in ctx.guild.roles:
        Lista += f"{role.mention}\n"
    await ctx.send(embed = Embed(description = Lista, color = color))

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

import os, sys, json
from random import choice, randint
from asyncio import sleep
from nextcord import (
    Status, Game, Intents,
    Member, User, Role,
    Embed, Color, File,
    TextChannel, User,
    SlashOption, Interaction
)
from nextcord.ext.commands import Bot, command, has_permissions
from nextcord.message import Message, MessageReference
from nextcord.ext.commands.errors import MissingRole, CommandInvokeError
from nextcord.errors import Forbidden, NotFound, HTTPException


print("Papocchio.py")
token = open("token.txt", 'r').read()
intents = Intents().all()
prefixes = (
    ")", "()", 
    "<:Papocchio:849018580426555473> ",
    "<:Papocchio:849018580426555473>",
    ")(", "@Papocchio#9166", "@Papocchio"
)
owner_ids = [797844636281995274]
Papocchio = Bot(
    command_prefix = prefixes,
    owner_ids = set(owner_ids),
    description = "Ciao, sono Papocchio-Bot, mi occupo di gestione nel server di Nonciclopedia.\n Trovi la mia documentazione con )Documentazione",
    intents = intents
)
gioco = Game(")Help | Papocchio | @Papocchio#9166")

rispostacce: dict[int, dict[str, str]] = {}
@Papocchio.event
async def on_ready():
    print(Papocchio.user, " è ora online ", "ID: ", Papocchio.user.id)
    await Papocchio.change_presence(status = Status.online, activity = gioco)
    for directory in os.listdir("guilds"):
        for file in os.listdir(f"guilds/{directory}"):
            with open(f"guilds/{directory}/risposteMaleducate.json", "r") as f:
                rispostacce[int(directory)] = json.load(f)


#Comandi cazzoni e abbastanza inutili

@Papocchio.command()
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

@Papocchio.command()
async def Nonciclopedia(ctx, pagina):
    await ctx.message.delete()
    nonciclopedia = "https://nonciclopedia.org/wiki/"
    await ctx.send(nonciclopedia + pagina)

@Papocchio.command()
async def Wikipedia(ctx, pagina):
    await ctx.message.delete()
    nonciclopedia = "https://it.wikipedia.org/wiki/"
    await ctx.send(nonciclopedia + pagina)

@Papocchio.command(description = "Comando per modificare la mia attività per un determinato arco di tempo.")
@has_permissions(administrator=True)
async def Cambia_attività(ctx, secondi, *nuova_attività):
    await ctx.message.delete()
    stato = ' '.join(nuova_attività)
    nuovo_stato = Game(str(stato))
    await Papocchio.change_presence(status = Status.online, activity = nuovo_stato)
    embed = Embed(description = f"""{ctx.message.author.mention} ha cambiato il mio stato per il tempo di {secondi} secondi.
Ecco la stronzata che mi ha rifilato come stato:""", color = Color.green())
    await ctx.send(embed = embed)
    embed = Embed(description = f"{nuovo_stato}", color = Color.green())
    await ctx.send(embed = embed)
    tempo = float(secondi)
    await sleep(tempo)
    await Papocchio.change_presence(status = Status.online, activity = gioco)

@Papocchio.command(description = "Comando per modificare il mio stato per un determinato arco di tempo.")
@has_permissions(administrator=True)
async def Cambia_stato(ctx, secondi:float, stato):
    await ctx.message.delete()
    try:
        await Papocchio.change_presence(status = stato_da_nome(stato))
    except ValueError:
        await ctx.send(embed = Embed(title = "ERRORE", description = f"""{ctx.message.author.mention}, il valore che hai inserito per il parametro stato non è convertibile in uno stato, riprova con un valore più plausibile di "{stato}", grazie"""))
    await ctx.send(embed = Embed(title = stato.upper(), description = f"Ho impostato lo stato {stato} per {round(secondi)} secondi. \n Non chiedetemi perché, qui è {ctx.message.author.mention} che comanda...", color = colore_da_stato(stato)))
    await sleep(secondi)
    await Papocchio.change_presence(status = Status.online, activity = gioco)
    await ctx.send(embed = Embed(title = "BACK IN GREEN", description = "Dopo aver cambiato stato per {} secondi, sono tornato".format(round(secondi)), color = Color.green()))

def stato_da_nome(stato: str):
    if (stato.lower() in ["online", "on"]):
        return Status.online
    elif (stato.lower() in ["idle", "inattivo"]):
        return Status.idle
    elif (stato.lower() in ["offline", "off"]):
        return Status.offline
    elif (stato.lower() in  ["non disturbare", "do not disturb", "dnd"]):
        return Status.dnd
    elif (stato.lower() in ["invisible", "invisibile"]):
        return Status.invisible
    else:
        raise ValueError(f"Il valore {stato} non è utilizzabile per il parametro stato")

def colore_da_stato(stato):
    stato = stato_da_nome(stato)
    if (stato == Status.online):
        return Color.green()
    elif (stato == Status.idle):
        return Color.orange()
    elif (stato == Status.offline):
        return Color.magenta()
    elif (stato == Status.dnd):
        return Color.red()
    elif (stato == Status.invisible):
        return Color.light_gray()
    else:
        raise ValueError(f"Il valore {stato} non è utilizzabile per il parametro stato")

@Papocchio.command()
@has_permissions(send_messages= True)
async def Stealth(ctx, secondi:float):
    await ctx.message.delete()
    await ctx.send(embed = Embed(title = "STEALTH", description = f"Su ordine di {ctx.message.author.mention} mi fingerò offline per {round(secondi)} secondi", color = Color.default()))
    await Papocchio.change_presence(status = Status.invisible, afk=True)
    await sleep(secondi)
    await ctx.send(embed = Embed(title = "BACK IN GREEN", description = "Dopo essermi nascosto per {} secondi, sono tornato".format(round(secondi)), color = Color.green()))
    await Papocchio.change_presence(status = Status.online, activity = gioco, afk = False)
    
@Papocchio.command(description = "Un messaggio in anonimo per rompere il cazzo al deficiente di turno.")
@has_permissions(mention_everyone=True)
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
@Papocchio.command(aliases = ["offendi"])
@has_permissions(send_messages=True)
async def Offendi(ctx, utente: User):
    try:
        await ctx.message.delete()
        await ctx.send(embed = Embed(description = f'{utente.mention}, ' + choice(offese), color = Color.random()))
    except MissingRole:
        await ctx.message.reply(f"{ctx.message.author.mention}, mi dispiace, ma per eseguire questo comando è necessario il ruolo nonciclopediano verificato")

@Papocchio.command()
@has_permissions(send_messages=True)
async def Aggiungi_offesa(ctx, *Offesa):
    await ctx.message.delete()
    offesa = ' '.join(Offesa)
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

@Papocchio.command()
@has_permissions(send_messages=True)
async def Lista_offese(ctx):
    await ctx.message.delete()
    colore = Color.random()
    await ctx.send(embed = Embed(description = f"{ctx.message.author.mention} ha richiesto la corrente lista delle offese.", title = "LISTA OFFESE", color = colore))
    await ctx.send(embed = Embed(description = f"*{offese}*", color = colore))
    await ctx.message.author.send(embed = Embed(description = "Hai richiesto la lista delle offese", title = "LISTA OFFESE", color = colore))
    await ctx.message.author.send(embed = Embed(description = f"*{offese}*", color = colore))

@Papocchio.command(aliases = ["scrivi"])
@has_permissions(send_messages=True)
async def Scrivi(ctx, *parole):
    await ctx.message.delete()
    frase = str('')
    for parola in parole:
        parola += ' '
        frase += parola
    await ctx.send(frase)

@Papocchio.command()
@has_permissions(send_messages=True)
async def Scrivi_con_attesa(ctx, secondi:float, *parole):
    await ctx.message.delete()
    frase = ' '.join(parole)
    async with ctx.typing():
        await sleep(secondi)
    await ctx.send(frase)

@Papocchio.command()
@has_permissions(send_messages=True)
async def Scrivi_a_velocità(ctx, caratteri_al_secondo: int, *parole):
    parole = ' '.join(parole)
    await ctx.message.delete()
    with ctx.typing():
        for i in range(len(parole)):
            await sleep(1/caratteri_al_secondo)
    await ctx.send(parole)

@Papocchio.command()
@has_permissions(send_messages=True)
async def Scrivi_come_utente(ctx, *parole):
    await ctx.message.delete()
    frase = ' '.join(parole)
    secondi = (frase.count(' ')+1)
    async with ctx.typing():
        await sleep(secondi)
    await ctx.send(frase)

@Papocchio.command(aliases = ["cancella"])
@has_permissions(manage_messages=True)
async def Cancella(ctx, quantità: int):
    await ctx.channel.purge(limit = quantità)
    await ctx.send(embed = Embed(description = f"Sono stati eliminati {quantità} messaggi per conto di {ctx.message.author.mention}!", color = Color.blurple()))

@Papocchio.command()
@has_permissions(send_messages=True)
async def Spam(ctx, ripetizioni: int, *parole):
    await ctx.message.delete()
    frase = ' '.join(parole)
    async with ctx.typing():
        for i in range(ripetizioni):
            await ctx.send(frase)
    await ctx.send(embed = Embed(description = f"Spam di {ripetizioni} messaggi effettuata per conto di {ctx.message.author.mention}"))

@Papocchio.command(aliases = ["Embed"], description = "Invia un embed per conto di un nonciclopediano. Il colore va codificato in RGB. L'immagine va scritta come link. Il file dev'essere presente nel dispositivo dell'host..")
@has_permissions(send_messages=True)
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
    embed.set_footer(text = f"Embed inviato in data {datetime.now()}", icon_url = "https://static.miraheze.org/nonciclopediawiki/c/cd/Papocchio_2000x2000.png")
    embed.set_author(name = ctx.message.author.nick, icon_url = ctx.message.author.avatar_url)
    embed.set_thumbnail(url = ctx.message.author.avatar_url)
    await ctx.send(embed = embed)
    await ctx.message.author.send(embed = Embed(title = "EMBED", description =f"{ctx.message.author.mention}, ho inviato nel canale {ctx.channel} il tuo embed"))

@Papocchio.command()
async def HelloWorld(ctx, linguaggio: str):
    await ctx.message.delete()
    
    if ((linguaggio in ["Python", "python", "py"]) or ("py" in linguaggio)):
        script = "print('Hello World')"
    elif (linguaggio == "ruby" or linguaggio == "Ruby" or "ruby" in linguaggio or "Ruby" in linguaggio):
        script = "puts 'Hello World'"
    elif ((linguaggio in ["C++", "c++", "Cpp", "cpp"]) or "c++" in linguaggio):
        script = """cout << "Hello World";"""
    elif (linguaggio in ["JavaScript", "javascript", "js"]):
        script = "console.log('Hello World);"
    else:
        script = """'Hello World'"""
        
    script = f"""```{linguaggio}
{script}```"""
    embed = Embed(title = linguaggio, description = script)
    await ctx.send(embed = embed)

@Papocchio.command()
@has_permissions(send_messages=True)
async def Attacca(ctx, ID:int):
    await ctx.message.delete()
    messaggio = await ctx.fetch_message(ID)
    await messaggio.pin()
    embed = Embed(title = "MESSAGGIO ATTACCATO", description = f"Ho attaccato il seguente messaggio su ordine di {ctx.message.author.mention}.", color = Color.blue())
    await ctx.send(embed = embed)
    informazioni_messaggio = Informazioni_messaggio_offline(messaggio)
    embed = Embed(title = "MESSAGGIO:", description = informazioni_messaggio, color = Color.blue())
    await ctx.send(embed = embed)

def Informazioni_messaggio_offline(messaggio: Message):
    informazioni = f""" **ID**: {messaggio.id}
** Link**: {messaggio.jump_url}
 
 **Autore**: {messaggio.author.mention} ({messaggio.author})
 **Orario**: {messaggio.created_at}
 **Canale**: {messaggio.guild}
"""

    if (messaggio.pinned):
        informazioni += f"\n **Messaggio attaccato**: Sì"
    else:
        informazioni += f"\n **Messaggio attaccato**: No"
    
    if (messaggio.reference != None):
        informazioni += f"\n **Messaggio risposto**: {messaggio.reference.message_id}"
    else:
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

@Papocchio.command()
async def Informazioni_messaggio(ctx, ID: int) -> (bool | None):
    await ctx.message.delete()
    try:
        embed = Embed(title = "INFORMAZIONI MESSAGGIO:", description = Informazioni_messaggio_offline(await ctx.fetch_message(ID)), color = Color.blue())
    except CommandInvokeError:
        await ctx.send(embed = Embed(title = "MESSAGGIO NON TROVATO", description = f"Il messaggio con ID {ID} non esiste, oppure è già stato cancellato", color = Color.red()))
        return False
    except NotFound:
        await ctx.send(embed = Embed(title = "MESSAGGIO NON TROVATO", description = f"Il messaggio con ID {ID} non esiste, oppure è già stato cancellato", color = Color.red()))
        return False
    except HTTPException:
        await ctx.send(embed = Embed(title = "MESSAGGIO NON TROVATO", description = f"Il messaggio con ID {ID} non esiste, oppure è già stato cancellato", color = Color.red()))
        return False
    await ctx.send(embed=embed)

@Papocchio.command()
async def Digita(ctx, secondi: float):
    await ctx.message.delete()
    async with ctx.typing():
        await sleep(secondi)

@Papocchio.command()
async def LegalizeDrugsAndMurder(ctx):
    await ctx.message.delete()
    embed = Embed(title = "LEGALIZE DRUGS AND MURDER")
    embed.set_image(url = choice(['https://www.ticketone.it/obj/media/IT-eventim/galery/222x222/e/electric-wizard-biglietti.jpg', 'http://4.bp.blogspot.com/-qrCRffBfn9U/UYRFym1TPpI/AAAAAAAAAns/pcB-uzVmw9w/s1600/ewblackmass.jpg', 'https://metalitalia.com/wp-content/uploads/2014/07/electric-wizard-band-2014.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdaursX4QPwoD5dauWtbQ-eoZQ-nmmcXR-GA&usqp=CAU', 'https://metalitalia.com/wp-content/uploads/2018/08/electric-wizard-band-2018.jpeg', 'https://www.ocanerarock.com/sally/wp-content/uploads/2018/11/Electric-Wizard.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwC_APEw7jKsLMevW8oBzUCxN2jHh4RPJG2Q&usqp=CAU', 'https://www.lascimmiapensa.com/wp-content/uploads/2017/11/electricwizardband2017_638.jpg', 'https://media.resources.festicket.com/www/artists/ElectricWizard.jpg', 'http://3.bp.blogspot.com/-C_bW7rSHa8o/TYIpgM_qFXI/AAAAAAAAI_c/aAlVGlsEAIU/s1600/Electric%2BWizard.jpg', 'https://media.stubcloudstatic.com/stubhub-catalog/d_defaultLogo.jpg/t_f-fs-0fv,q_auto:low,f_auto,c_fill,$w_750_mul_3,$h_416_mul_3/performer/700245/r1k5aeangqrftshro5hp', 'https://cdn.wegow.com/media/artists/electric-wizard/electric-wizard-1492555854.33.2560x1440.jpg', 'https://lastfm.freetls.fastly.net/i/u/avatar170s/9f0e22d9f6064320bedfde9b8112ad59', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwyrIxYbr3-8_tvv8coHpfXbnHQ-bb6Pezzg&usqp=CAU', 'https://static.wikia.nocookie.net/metal/images/0/03/ElectricWizard2013.jpg/revision/latest/scale-to-width-down/250?cb=20140310105648', 'https://note-store.com/upload/resize_cache/iblock/605/325_380_2/Electric-Wizard.png', 'https://upload.wikimedia.org/wikipedia/commons/d/d6/Electricwizard_LizBuckingham.jpg', 'https://www.metal.it/image.ashx?id=358&size=400&folder=group&suffix=photo&filters=square', 'https://lh3.googleusercontent.com/proxy/JAu3GMnf2yD_a7H-pSA_P1BEh9lXpfzhDupBUgLbT2OvuKFPn37ynIdIBUtT2SrrAYNfAKv9DTmWuUSrg9LOwzvIriP5lQVzFIO3re44EJg']))
    await ctx.send(embed = embed)

global Roberta_Sammarelli
Roberta_Sammarelli = ['https://lightstorage.ecodibergamo.it/mediaon/cms.quotidiani/storage/site_media/media/photologue/2016/10/7/photos/cache/a-cena-con-roberta-sammarelli_51915_display.jpg', 'http://baraonda.radiondadurto.org/files/2013/04/1roberta.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/RobertaSammarelli.jpg/1200px-RobertaSammarelli.jpg', 'https://www.nikonclub.it/forum/uploads//201601/appBig_e9d2aa6828bf99cf6900693b4a720bb2.jpg', 'https://rockitecn.nohup.it/fotouser/102895/verdena-roberta-sammarelli.jpg', 'https://images2-bergamo.corriereobjects.it/methode_image/2015/08/27/Bergamo/Foto%20Bergamo%20-%20Trattate/verdena-kTt-U43110492147391zcE-1224x916@Corriere-Web-Bergamo-593x443.jpg?v=20150827161913', 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/b3069b23-a844-4f45-8589-f32f580706ba/d11c0k7-006f5360-3b88-4f3e-9298-7986167e422f.jpg/v1/fill/w_600,h_801,q_75,strp/roberta_sammarelli_by_veergilicious_d11c0k7-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9ODAxIiwicGF0aCI6IlwvZlwvYjMwNjliMjMtYTg0NC00ZjQ1LTg1ODktZjMyZjU4MDcwNmJhXC9kMTFjMGs3LTAwNmY1MzYwLTNiODgtNGYzZS05Mjk4LTc5ODYxNjdlNDIyZi5qcGciLCJ3aWR0aCI6Ijw9NjAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.EcugiTErOSgl4HH41BB5EAhKBw9TC14jwzEO_koxxpU', 'https://live.staticflickr.com/6073/6086307279_6812bdf2cd_b.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMaIcXR2gcYnENaBcYgZfvhdxSxQfecLtG4Q&usqp=CAU', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs4tYJmoLnvGx6bacbc4XMEw80cIg7lJL3og&usqp=CAU', 'https://upload.wikimedia.org/wikipedia/commons/8/80/Roberta_Sammarelli_-_Modena_19-09-2007.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnhU5tMTkOEF8KlOi3L5dmf26ZyM3sDsXE6Q&usqp=CAU', 'https://rockitecn.nohup.it/fotouser/102918/verdena-roberta-sammarelli.jpg?v=843', 'http://2.bp.blogspot.com/-PLn-AtMJB5k/Vd8Oh4noIYI/AAAAAAAA3V4/vnjWHI28ofc/s1600/foto.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2NZQKsmu7yNLbVZsyWcQIDq-qqmPQCgedow&usqp=CAU']
@Papocchio.slash_command(name="robertasammarelli", description="Roberta Sammarelli, pronta per l'invio.")
async def RobertaSammarelli(interaction: Interaction):
    embed = Embed(title = "ROBERTA SAM(M)ARELLI")
    global Roberta_Sammarelli
    url = choice(Roberta_Sammarelli)
    embed.set_image(url = url)
    embed.set_footer(text = f"Per {interaction.user.nick} con amore", icon_url = url)
    await interaction.channel.send(embed = embed)

@Papocchio.command()
async def Caparezza(ctx):
    await ctx.message.delete()
    embed = Embed(title = "CAPAREZZA ||tutt'altro che una carezza||")
    embed.set_image(url = choice(['https://cdn.discordapp.com/attachments/851839196742287380/869931327334518784/caparezza.png', 'https://cdn.discordapp.com/attachments/851839196742287380/869930713049354240/caparezza.png', 'https://cdn.discordapp.com/attachments/851839196742287380/869930601128546314/hqdefault.png', 'https://media.discordapp.net/attachments/851839196742287380/869929953314095114/image.png?width=320&height=320', 'https://notiziemusica.it/wp-content/uploads/2018/02/CS_CAPAREZZA.jpg.webp', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Caparezza_Italia_Wave.jpg/220px-Caparezza_Italia_Wave.jpg', 'https://www.alguer.it/img/Caparezza-3.jpg', 'https://sites.google.com/site/patagarruconiriccioli/_/rsrc/1461764265458/il-nuovo-caparezza/capa2.jpg', 'https://www.studionord.news/wp-content/uploads/2018/03/Caparezza.jpg']))
    await ctx.send(embed = embed)

@Papocchio.command()
@has_permissions(read_message_history=True)
async def Messaggi(ctx, utente: Member, canale: TextChannel, quantità: int):
    await ctx.message.delete()
    messaggio = await canale.send(embed = Embed(title = "LEGGENDO...", description = f"Sto leggendo {quantità} messaggi al posto di {ctx.message.author.mention}, che non ha voglia di farlo.", color = Color.green()))
    messaggi = ""
    with ctx.typing():
        async for i in canale.history(limit = quantità):
            if i.author == utente:
                messaggi += f"{i.id}\n"
    primo_id = messaggi[:messaggi.find('\n')]
    await messaggio.edit(embed = Embed(title = "FINITO", description = f"Ho letto {quantità} messaggi. :white_check_mark:"))
    await ctx.send(embed = Embed(title = f"MESSAGGI DI {utente.nick}", description = messaggi, color = Color.default()))
    await ctx.send(embed = Embed(description = f"{utente.mention}, puoi richiedere informazioni sui tuoi messaggi con `)InformazioniMessaggio ID`.\n Ad esempio con `)InformazioniMessaggio {primo_id}`"))

from asyncio import create_task, wait, FIRST_COMPLETED
from datetime import datetime
from typing import Iterable
@Papocchio.command(description = "Spiare un utente in ogni cosa che fa, dall'andare online fino al modificarsi il nickname, passando dal digitare sulla tastiera e dall'aprire spotify.")
@has_permissions(send_messages=True)
async def Spia(ctx, utente: Member):
    autore = ctx.message.author
    await ctx.message.delete()
    await autore.send(embed = Embed(title = "SPIONAGGIO", description = f"Ho iniziato a pedinare {utente.mention}.\n Riferirò se lascerà il server da te indicato.\n Riferirò se apparirà online o cambierà stato.\n Riferirò se digiterà un messaggio nel server, o se lo invierà.\n Riferirò se cambierà username, discriminatore, o avatar.", color = Color.default()))
    await autore.send(embed = Embed(description = f"Per terminare questo pedinamento, scrivi 'Smettila di spiarlo' dove posso leggerlo.\n Il messaggio verrà immediatamente eliminato e smetterai di ricevere notifiche.", color = Color.default()))

    async def wait_for_event(event, **options):
        args = await Papocchio.wait_for(event, **options)
        if not isinstance(args, Iterable):
            args = [args]
        return event, *args

    while True:
        tasks = [
            create_task(wait_for_event("member_update")),
            create_task(wait_for_event("user_update")),
            create_task(wait_for_event("message")),
            create_task(wait_for_event("typing"))
        ]

        done, pending = await wait(tasks, return_when=FIRST_COMPLETED)
        for t in pending:
            t.cancel()
        
        event, *args = list(done)[0].result()

        if event == "user_update":
            prima, dopo = args
            if prima.nick == utente.nick:
                Emb = Embed(title = f"{utente.name}#{utente.discriminator}", color = Color.default())
                Emb.add_field(name = "Prima", value = f"{prima.avatar}\n {prima.name}\n {prima.discriminator}")
                Emb.add_field(name = "Dopo", value = f"{dopo.avatar}\n {dopo.name}\n {dopo.discriminator}")
                Emb.set_footer(text = f"Orario: {datetime.now()}")
                Emb.set_author(name = "Papocchio", icon_url = "https://static.miraheze.org/nonciclopediawiki/c/cd/Papocchio_2000x2000.png")
                Emb.set_thumbnail(url = utente.avatar_url)
                await autore.send(embed = Emb)
        
        elif event == "member_update":
            prima, dopo = args
            if prima.nick == utente.nick:
                Emb = Embed(title = f"{utente.name}#{utente.discriminator}", color = Color.default())
                Emb.add_field(name = "Prima", value = f"{prima.status}\n {prima.activity}\n {prima.nick}", inline = False)
                Emb.add_field(name = "Dopo", value = f"{dopo.status}\n {dopo.activity}\n {dopo.nick}", inline = False)
                Emb.set_footer(text = f"Orario: {datetime.now()}")
                Emb.set_author(name = "Papocchio", icon_url = "https://static.miraheze.org/nonciclopediawiki/c/cd/Papocchio_2000x2000.png")
                Emb.set_thumbnail(url = utente.avatar_url)
                await autore.send(embed = Emb)

        elif event == "typing":
            canale, user, quando = args
            if user == utente:
                Emb = Embed(title = f"{utente.name}#{utente.discriminator}", description = f"Ho beccato {utente.mention} a digitare in {canale}.", color = Color.default())
                Emb.set_footer(text = f"Orario: {datetime.now()}")
                Emb.set_author(name = "Papocchio", icon_url = "https://static.miraheze.org/nonciclopediawiki/c/cd/Papocchio_2000x2000.png")
                Emb.set_thumbnail(url = utente.avatar_url)
                await autore.send(embed = Emb)

        elif event == "message":
            messaggio = args[0]
            if messaggio.author == utente:
                Emb = Embed(title = f"{utente.name}#{utente.discriminator}", description = f"{utente.mention} ha inviato un messaggio in {messaggio.channel}.", color = Color.default())
                Emb.set_footer(text = f"Orario: {datetime.now()}")
                Emb.set_author(name = "Papocchio", icon_url = "https://static.miraheze.org/nonciclopediawiki/c/cd/Papocchio_2000x2000.png")
                Emb.set_thumbnail(url = utente.avatar_url)
                await autore.send(embed = Emb)
            if messaggio.author == autore and messaggio.content == "Smettila di spiarlo":
                await messaggio.delete()
                Emb = Embed(title = "SPIONAGGIO", description = f"Ho smesso di spiare {utente.name}#{utente.discriminator}.")
                Emb.set_footer(text = f"Orario: {datetime.now()}")
                Emb.set_author(name = "Papocchio", icon_url = "https://static.miraheze.org/nonciclopediawiki/c/cd/Papocchio_2000x2000.png")
                Emb.set_thumbnail(url = utente.avatar_url)
                await autore.send(embed = Emb)
                return

#Comandi tattici per la gestione dei nonciclopediani

@Papocchio.command()
async def Permessi(ctx, utente: Member):
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

@Papocchio.command(description = "Decidi quante notifiche mandare per rompere il cazzo allo sfortunato di turno. Se non specificherai un numero allora sarò costretto a deciderlo io...")
@has_permissions(send_messages=True, mention_everyone=True)
async def Importuna(ctx, utonto: Member, ripetizioni = None, *messaggio_privato):
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

@Papocchio.command()
@has_permissions(send_messages=True, mention_everyone=True)
async def Avvertimento(ctx, utente: Member, motivo = None):
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

@Papocchio.command()
@has_permissions(administrator=True)
async def Calciorotazione(ctx, utente: Member, *Motivo):
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

@Papocchio.command(description = "Per dare un po' di tempo al ciccione di turno per lamentarsi dell'espulsione in avvicinamento. Inserire un tempo minimo di 15 secondi.", aliases = ["CCC"])
@has_permissions(send_messages=True)
async def Calciorotazione_con_countdown(ctx, utente: Member, secondi: float, motivo = None, offesa = None):
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

@Papocchio.command(aliases = ["AR", "aggiungi_ruolo", "Aggiungi_ruolo"])
@has_permissions(manage_roles=True)
async def Aggiungi_Ruolo(ctx, ruolo: Role, utente: Member):
    await ctx.message.delete()
    try:
        await utente.add_roles(ruolo)
    except Forbidden:
        await ctx.send(embed = Embed(description = f"{ctx.message.author.mention}, non ho i poteri per assegnare quel ruolo. Per farlo dev'essere un ruolo inferiore al più alto dei miei.", color = Color.green()))
        return
    await ctx.send(embed = Embed(description = f"Ho aggiunto il ruolo {ruolo.mention} a {utente.mention} su richesta di {ctx.message.author.mention}", color = Color.green()))

@Papocchio.command(aliases = ["RR", "rimuovi_ruolo", "Rimuovi_ruolo"])
@has_permissions(send_messages=True)
async def Rimouvi_Ruolo(ctx, ruolo: Role, utente: Member):
    await ctx.message.delete()
    try:
        await utente.remove_roles(ruolo)
    except Forbidden:
        await ctx.send(embed = Embed(description = f"{ctx.message.author.mention}, non ho i poteri per rimuovere quel ruolo. Per farlo dev'essere un ruolo inferiore al più alto dei miei.", color = Color.red()))
        return
    await ctx.send(embed = Embed(description = f"Ho tolto il ruolo {ruolo.mention} a {utente.mention} su richesta di {ctx.message.author.mention}", color = Color.red()))

@Papocchio.command(description = "Con questo comando puoi fare una gentile concessione al nonciclopediano di turno, regalandogli per un numero di secondi limitato un ruolo a tua scelta, di modo da capire fino a che punto possa esserne immeritevole")
@has_permissions(manage_roles=True)
async def Concessione(ctx, ruolo: Role, utente: Member, secondi: float):
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

@Papocchio.command(aliases = ["KillYourself", "Suicide"])
@has_permissions(administrator=True)
async def FERMO(ctx):
    await ctx.message.delete()
    await ctx.send(embed = Embed(description = f'Hai usato il comando `)FERMO`, il mio programma in file `.exe` si arresterà in automatico, per riattivarmi contatta `@FLAK_FLAK#3241`', color = Color.default(), title = f"{ctx.message.author.nick} MI HA FERMATO"))
    await quit()

@Papocchio.command()
@has_permissions(manage_guild=True)
async def SPENTO(ctx, secondi:float):
    await ctx.message.delete()
    embed = Embed(title = "SPENTO", description = f"{ctx.message.author.mention} mi ha spento per {round(secondi)} secondi", color = Color.red())
    await ctx.send(embed = embed)
    await Papocchio.close()
    await sleep(secondi)
    await Papocchio.login(token)
    embed = Embed(title = "ACCESO", description = f"Sono tornato dal letargo di {round(secondi)} impostomi da {ctx.message.author.mention}", color = Color.green())
    await ctx.send(embed = embed)
    
#Comandi sulle informazioni

@Papocchio.command()
@has_permissions(send_messages=True)
async def Prefissi(ctx): #Da incorporare in un comando )Informazioni_Bot
    await ctx.message.delete()
    await ctx.send(embed = Embed(title = "PREFISSI", description = f"{ctx.message.author.mention}, eccoti i miei prefissi:"))
    await ctx.send(embed = Embed(description = prefixes))

@Papocchio.command(aliases = ["info", "Info", "informazioni"], description = "Le informazioni fondamentali del Papocchio.")
@has_permissions(send_messages=True)
async def Informazioni(ctx): #Andrà ampliato con informazioni sul bot stesso
    await ctx.message.delete()
    numero_server = len(Papocchio.guilds)
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

@Papocchio.command(description = "Lista dei server dei quali faccio parte.")
@has_permissions(send_messages=True)
async def Lista_server(ctx):
    await ctx.message.delete()
    numero_server = len(Papocchio.guilds)
    color = Color.purple()
    await ctx.send(embed = Embed(description = f"{ctx.message.author.mention}, eccoti la lista dei {numero_server} server dei quali faccio parte:", color = color))
    Lista = ""
    for guild in Papocchio.guilds:
        Lista += f"""{guild.name}
"""
    await ctx.send(embed = Embed(description = Lista, color = color, title = "LISTA SERVER"))

@Papocchio.command(description = "Lista degli utenti di questo server.")
@has_permissions(send_messages=True)
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

@Papocchio.command()
@has_permissions(send_messages=True)
async def Lista_ruoli(ctx):
    await ctx.message.delete()
    color = Color.purple()
    await ctx.send(embed = Embed(title = "LISTA RUOLI", description = f"{ctx.message.author.mention}, eccoti la lista dei {len(ctx.guild.roles)} ruoli di questo server:", color = color))
    Lista = ''
    for role in ctx.guild.roles:
        Lista += f"{role.mention}\n"
    await ctx.send(embed = Embed(description = Lista, color = color))

@Papocchio.command()
@has_permissions(send_messages=True)
async def Documentazione(ctx):
    await ctx.message.delete()
    messaggio = f"""{ctx.message.author.mention} ha richiesto il mio codice sorgente:
https://github.com/FLAK-ZOSO/Discord.py/blob/Papocchio/Papocchio.py"""
    await ctx.send(embed = Embed(title = "DOCUMENTAZIONE", description = messaggio, color = Color.lighter_gray()))
    await ctx.message.author.send(embed = Embed(title = "DOCUMENTAZIONE", description = "Hai richiesto il mio file sorgente, te lo invio qui sotto.", color = Color.lighter_gray()))
    await ctx.message.author.send(file = File(r"Papocchio.py"))
    print(f"{ctx.message.author} ha richiesto la mia documentazione")
    await sleep(15)
    embed = Embed(title = "ATTENZIONE", description = "Se fai stronzate col mio token lo verrò a sapere, il Papocchio ti osserva:", color = Color.red())
    embed.set_image(url = "https://static.miraheze.org/nonciclopediawiki/c/cd/Papocchio_2000x2000.png")
    await ctx.message.author.send(embed = embed)


# Comando "STOCAZZO" e correlati
@Papocchio.slash_command(name="inizializza", description = "Inizializza una sezione di memoria per il server corrente volta all'uso comando /stocazzo e non solo")
async def inizializzaGuild(interaction: Interaction) -> None:
    try:
        os.makedirs(fr"guilds/{interaction.guild.id}")
    except OSError:
        interaction.response.send_message("Il server è già inizializzato per Papocchio", ephemeral=True)
    open(fr"guilds/{interaction.guild.id}/risposteMaleducate.json", "w").write("{}")
    await interaction.response.send_message("Inizializzazione completata", ephemeral=True)


@Papocchio.slash_command(name="maleduca", description = "Aggiunge una risposta maleducata alla memoria del server")
async def aggiungiRispostaMaleducata(interaction: Interaction, risposta: str, innesco: str) -> None:
    try:
        risposteMaleducate = json.load(open(fr"guilds/{interaction.guild.id}/risposteMaleducate.json"))
    except FileNotFoundError:
        await interaction.response.send_message("Il server non è inizializzato per Papocchio", ephemeral=True)
    risposteMaleducate[innesco.lower()] = risposta
    rispostacce[interaction.guild.id] = risposteMaleducate
    json.dump(risposteMaleducate, open(fr"guilds/{interaction.guild.id}/risposteMaleducate.json", "w"))
    await interaction.response.send_message("Risposta maleducata aggiunta", ephemeral=True)


@Papocchio.slash_command(name="rispondi", description = "Risponde (maleducatamente) a un messaggio")
async def rispondiMaleducatamente(interaction: Interaction, id_messaggio: str, risposta: str) -> None:
    # Get the message and answer to it
    messaggio = await interaction.channel.fetch_message(id_messaggio.split('-')[1])
    await messaggio.reply(risposta)
    await interaction.response.send_message("Risposta inviata", ephemeral=True)


@Papocchio.slash_command(name="stocazzo", description = "Risponde (maleducatamente) a un messaggio")
async def stocazzalo(interaction: Interaction, id_messaggio: str) -> None:
    messaggio = await interaction.channel.fetch_message(id_messaggio.split('-')[1])
    await messaggio.reply("**STOCAZZO!**")
    await interaction.response.send_message("stocazzo inviato", ephemeral=True)


@Papocchio.event
async def on_message(message: Message):
    regole = rispostacce[message.guild.id]
    if message.content.strip().lower() in regole.keys():
        await message.reply(regole[message.content.strip().lower()])


Papocchio.run(token)
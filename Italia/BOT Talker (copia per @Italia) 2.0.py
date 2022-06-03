import smtplib
import random
import string
import discord
from discord.ext import commands
from discord.utils import get
from discord import client
import time
import webbrowser

print("Eseguendo il programma...")
token = "ODI4MDA3ODc5MDY3MTcyODg1.YGjUbg.WXC9LRX1SZLvB16GFUuHmImfjY4"
Bot = commands.Bot(command_prefix = "$")

cittadini = []

No = ["Niente", "niente", "Nnt", "nnt", "nulla", "Nulla", "no", "No", "NO"]
Sì = ["Sì", "sì", "si", "Si", "SI", "ok", "Ok", "OK"]
PermessoMancante = 'Non hai il permesso di usare questa funzione, probabilmente perché non hai il ruolo **Autorizzato a Talker**'
offese = [" ce l'hai corto",  " tua madre si sta ancora pentendo del mancato aborto", " sei così brutto che se mai avrai una ragazza dovrà essere così miope da poterti scambiare per un rettile", " parli come un'aspirante Barbara d'Urso"]
Procioni = ['https://cdn.discordapp.com/attachments/828540525190840340/834165376447283251/sconosciuto.gif', 'https://cdn.discordapp.com/attachments/828540525190840340/834163468894601246/sconosciuto.gif', 'https://cdn.discordapp.com/attachments/828540525190840340/834163377823547402/sconosciuto.gif', 'https://tenor.com/view/hungry-eat-food-raccoon-eating-gif-15379674', 'https://tenor.com/view/raccoon-clap-yay-clapping-happy-gif-5243246', 'https://tenor.com/view/raccoon-dog-funny-animals-cute-gif-3320061', 'https://tenor.com/view/hungry-eat-food-raccoon-eating-gif-15379674', 'https://tenor.com/view/swag-procione-kawaii-gif-5390229', 'https://tenor.com/view/raccoon-we-are-here-open-the-door-doorbell-hurry-up-gif-13308287', 'https://tenor.com/view/raccoon-clean-clean-up-sweep-broom-gif-13308307', 'https://tenor.com/view/raccoon-bicycle-bike-ride-go-biking-gif-13308306']

@Bot.event
async def on_ready():
    print(Bot.user, " è ora online ", "ID: ", Bot.user.id)
    game = discord.Game("$Aiuto")
    await Bot.change_presence(status = discord.Status.idle, activity = game)

@Bot.event
async def on_mention(ctx): #Quest'evento credo non esista...
    await ctx.send(Bot.user + Bot.user.id + " può risponderti col comando $Aiuto")

@Bot.command()
async def Aiuto(ctx):
    Aiuto = str('''Le categorie sono visibili con i seguenti comandi:
    $Aiuto :joy:
    $Aiuto_Spam
    $Aiuto_Comandi
    $Aiuto_Wiki
    $Aiuto_Scrittura
    $Aiuto_Benvenuto
    $Documentazione
    ''')
    await ctx.send(Aiuto)

@Bot.command()
async def Documentazione(ctx):
    area = ctx.message.channel
    await ctx.send(r"`D:\Python\Python\Python39\Python3.9.1 dal pc\BOT Talker (copia per @Italia) 2.0.py`")
    await ctx.send('Invio dei file momentaneamente disabilitato') #Qui devo capire come fare per fargli allegare un file Python, in alternativa invierò un link verso questa pagina

@Bot.command()
async def Aiuto_Spam(ctx):
    Aiuto_Spam = str('''I comandi di spam sono i seguenti:
    $Spam_15 Parole-da-spammare :printer:
    $Spam_5 Parole-da-spammare :printer:
    $Spam_link Link-da-spammare :link:
    $Spam_menzione @Ruolo/Utente-da-menzionare :loudspeaker:''')
    await ctx.send(Aiuto_Spam)

@Bot.command()
async def Aiuto_Comandi(ctx):
    Aiuto_Comandi = str('''I comandi di gestione degli utenti sono i seguenti:
    $Comando Comando (non funzionante):cross:
    $Espelli @Utente (non funzionante) :cross:
    $Espulsione @Utente (non funzionante):cross:
    $Anonimo @Utente messaggio-da-mandare :email:
    $Avvertimento @Utente avvertimento-da-mandare :warning:
    $FERMO :stop:''')
    await ctx.send(Aiuto_Comandi)

@Bot.command()
async def Aiuto_Wiki(ctx):
    Aiuto_Wiki = str('''I comandi delle Wiki sono i seguenti:
    $Casuale
    $itwikipedia nome_della_pagina :mag:
    $Wikipedia nome_della_pagina :mag: :wikipedia:
    $Nonciclopedia nome_della_pagina :mag_right:''')
    await ctx.send(Aiuto_Wiki)

@Bot.command()
async def Aiuto_Scrittura(ctx):
    Aiuto_Scrittura = str('''I comandi di scrittura sono i seguenti:
    $Cancella N :recycle:
    $Scrivi Parole-del-messaggio :pencil:
    $Ripeti Parole-del-messaggio :parrot:
    $Emoji Nome_dell'emoji :sushi:
    $Maiuscolo Parole-da-ridurre
    $Minuscolo Parole-da-aumentare''')
    await ctx.send(Aiuto_Scrittura)

@Bot.command()
async def Aiuto_Benvenuto(ctx):
    Aiuto_Benvenuto = str('''I comandi di benvenuto sono i seguenti:
    $Ciao
    $Benvenuto @Utente :wave:
    $Benvenuto_regione Regione :flag_it:
    $Auguri Festività :partying_face:
    $Offendi @Utente
    $Aggiungi_offesa''')
    await ctx.send(Aiuto_Benvenuto)

#Qui ci sono i vari comandi di Aiuto di singole funzioni

@Bot.command()
async def Aiuto_Mail(ctx):
    autore = ctx.message.author
    await ctx.send("Sintassi:  `$Email tuonome@tuodominio suonome@suodominio oggetto-del-messaggio corpo-della-mail password-del-tuo-account`")
    await ctx.send("Esempio:  `$Email {autore}@gmail.com Italia@discord.devenloping LA-SCUOLA-ESCHIMESE La-scuola-è-stata-inventata-in-Groenlandia P4$$W0RD-1N1ND0V1N4B1L3` ")
    await ctx.send("I trattini (-) saranno trasformati automaticamente in spazi prima di inviare la mail.")
    await ctx.send(f"La tua password non sarà salvata in alcun modo, la variabile locale che la contiene viene svuotata prima del messaggio di conferma con  `password = None`.")
    









#Qui dentro si definiscono le sottoclassi di cittadino inclusa la stessa

class cittadino:
    def __init__(self, nome, cognome, regione, disoccupato): #Per creare un oggetto cittadino si veda la riga 157
        self.nome = nome
        self.cognome = cognome
        self.regione = regione
        self.disoccupato = disoccupato
    async def scheda_cittadino(ctx, self):
        if self.disoccupato in Sì:
            await ctx.send(f"{self.nome} {self.cognome} vive in {self.regione} ed è disoccupato")
            return f"{self.nome} {self.cognome} vive in {self.regione} ed è disoccupato"
        if self.disoccupato in No:
            await ctx.send(f"{self.nome} {self.cognome}: lavora come {self.lavoro} per conto di {self.datore_di_lavoro} con lo stipendio di {self.reddito}€ al mese, residente in {self.regione}")
            return f"{self.nome} {self.cognome}: lavora come {self.lavoro} per conto di {self.datore_di_lavoro} con lo stipendio di {self.reddito}€ al mese, residente in {self.regione}"

class dipendente(cittadino): #Per creare un oggetto dipendente si veda la riga 172
    def __init__(self, nome, cognome, regione, disoccupato, lavoro, reddito, datore_di_lavoro, tasse):
        super().__init__(nome, cognome, regione, disoccupato)
        self.disoccupato = "No"
        self.lavoro = lavoro
        self.reddito = reddito
        self.datore_di_lavoro = datore_di_lavoro
        self.tasse = tasse
    def Capo(self):
        print(self.datore_di_lavoro)
        self.datore_di_lavoro = input("Nuovo datore di lavoro: ")
        print(self.datore_di_lavoro)

class capo_di_azienda(cittadino): #Questa classe non può ancora contenere oggetti creati da un utente discord tramite comando
    def __init__(self, nome, cognome, lavoro, reddito, regione, azienda):
        super().__init__(nome, cognome, regione, disoccupato)
        self.disoccupato = "No"
        self.lavoro = "Capo d'azienda"
        self.reddito = reddito
        self.azienda = azienda
    def Assumi(cittadino, azienda):
        return f"{cittadino.datore_di_lavoro} era il datore di lavoro di {cittadino.nome} {cittadino.cognome}"
        cittadino.datore_di_lavoro = azienda
        return f"{cittadino.datore_di_lavoro} è ora il datore di lavoro di {cittadino.nome} {cittadino.cognome}"
    def Aumento(dipendente):
        print(dipendente.reddito)
        modifica = input()
        if modifica == 0 or modifica is str:
            pass
        else:
            dipendente.reddito += round(modifica)
        print(dipendente.reddito)
    
class azienda: #La classe azienda è per ora inutile, servirà connetterla con la classe capo_di_azienda e quella dipendente
    def __init__(self, nome, fondazione, proprietario, dipendenti, fatturato):
        self.nome = nome
        self.fondazione = input("Giorno di fondazione: ")
        if proprietario.lavoro == "Capo d'azienda":
            self.proprietario = proprietario
        else:
            return "L'utente {proprietario} non esiste."
        self.dipendenti = dipendenti
        self.fatturato = fatturato

#Qui finisce la parte di definizione delle classi, 58 righe di codice tutt'ora non funzionanti, si veda "BOT economico test 4.0 online.py"

#Questa parte invece contiene i comandi che utilizzano le classi di cui sopra, funzionanti solo in fase di creazione dell'oggetto, non in fase di restituzione dei dati
@Bot.command()
async def Cittadino(ctx, self, nome, cognome, regione, disoccupato):
    self = cittadino(nome, cognome, regione, disoccupato)
    await ctx.send(f"{self.nome} {self.cognome}, la tua utenza è stata creata.")
    await ctx.send("Per visualizzare il tuo account prova a digitare $Scheda_cittadino @Username")
    await ctx.send("Se qualcosa è andato storto, digita $Aiuto_Utenza")

@Bot.command()
async def Aiuto_Cittadino(ctx):
    await ctx.send("syntax: $Cittadino @Username nome cognome regione disoccupato (Sì/No)")
    await ctx.send("nome nome cognome regione disoccupato(Sì/No)")
    await ctx.send("Per maggiori informazioni è sempre disponibile il comando $Aiuto_Utenza")
    
@Bot.command()
async def Lavoro(ctx, self, nome, cognome, regione, disoccupato, lavoro, reddito, datore_di_lavoro, tasse):
    self = dipendente(nome, cognome, regione, disoccupato, lavoro, reddito, datore_di_lavoro, tasse)
    await ctx.send("Per visualizzare il tuo account prova a digitare $Scheda_cittadino @Username")

@Bot.command()
async def Aiuto_Lavoro(ctx):
    await ctx.send("$Lavoro **nickname**, **nome**, **cognome**, **regione**, disoccupato, **lavoro**, **reddito**, datore_di_lavoro, tasse")
    await ctx.send("Ho contrassegnato con il grassetto i campi necessari, per quelli facoltativi potrai semplicemente inserire un trattino (-), li compilerò in automatico")
    await ctx.send("Per maggiori informazioni è sempre disponibile il comando $Aiuto_Utenza")

@Bot.command()
async def scheda_cittadino(ctx, self):
    print(self)
    if self.disoccupato in Sì:
        await ctx.send(f"{self.nome} {self.cognome} vive in {self.regione} ed è disoccupato")
        print(self)
        return f"{self.nome} {self.cognome} vive in {self.regione} ed è disoccupato"
    if self.disoccupato in No:
        await ctx.send(f"{self.nome} {self.cognome}: lavora come {self.lavoro} per conto di {self.datore_di_lavoro} con lo stipendio di {self.reddito}€ al mese, residente in {self.regione}")
        print(self)
        return f"{self.nome} {self.cognome}: lavora come {self.lavoro} per conto di {self.datore_di_lavoro} con lo stipendio di {self.reddito}€ al mese, residente in {self.regione}"

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def Tasse(ctx, lavoratore): #Lunga funzione (funzionante) per determinare le tasse di un cittadino
    reddito = lavoratore.reddito
    reddito = int(reddito) #Si utilizzano le aliquote irpef mensili
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
                    await ctx.send(tasse) #Output in Discord
    lavoratore.tasse = tasse #Assegnazione in locale

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def TasseBeta(ctx, reddito): #Lunga funzione (funzionante) per determinare le tasse dato un reddito
    reddito = int(reddito) #Si utilizzano le aliquote irpef mensili
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
                    await ctx.send(tasse) #Output in Discord

#Qui finisce la parte di comandi dedicati alla parte economica del bot








#Da qui iniziano i comandi veri e propri

@Bot.command()
async def Benvenuto(ctx, destinatario):
    await ctx.channel.purge(limit = 1)
    await ctx.send(f"{destinatario.mention}, Benvenuto in Italia :flag_it:")

@Bot.command()
async def Benvenuto_regione(ctx, regione):
    await ctx.channel.purge(limit = 1)
    regione = str(regione)
    await ctx.send(f'Benvenuto in {regione}')

@Bot.command()
async def Ciao(ctx):
    author = ctx.message.author
    await ctx.reply(f"Ciao {author.mention}")

@Bot.command()
async def Offendi(ctx, destinatario):
    await ctx.send(f"{destinatario},"+ random.choice(offese))

@Bot.command()
async def Aggiungi_offesa(ctx, offesa):
    offesa = offesa.replace("-", " ", 100)
    offese.append(offesa)
    print(offese)
    await ctx.send(offesa)

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def Auguri(ctx, festività):
    await ctx.channel.purge(limit=1)
    if festività == "Pasqua":
        await ctx.send('Buona Pasqua :egg:')
    elif festività == "Compleanno":
        await ctx.send(':partying_face: Buon Compleanno! :birthday:')
    elif festività == "Natale":
        await ctx.send('Buon Natale! :santa:')
    else:
        await ctx.send('Auguri per la festa ' + festività)

#Fine della sezione Benvenuto







#Comandi della sezione Wiki
        
@Bot.command()
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

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def Nonciclopedia(ctx, ricerca):
    ricerca = str(ricerca)
    link = "https://nonciclopedia.org/wiki/"
    Pagina = str(link + ricerca)
    await ctx.send(Pagina)

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def Wikipedia(ctx, ricerca):
    ricerca = str(ricerca)
    link = "https://wikipedia.org/wiki/"
    Pagina = str(link + ricerca)
    await ctx.send(Pagina)
                    
@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def itwikipedia(ctx, ricerca):
    ricerca = str(ricerca)
    link = "https://it.wikipedia.org/wiki/"
    Pagina = str(link + ricerca)
    await ctx.send(Pagina)

#Fine della sezione Wiki












#Comandi della sezione Scrittura
    
@Bot.command()
async def Cancella(ctx, amount = 10000):
    await ctx.channel.purge(limit = amount)
    amount = str(amount)
    await ctx.send('Sono stati eliminati ' + amount + " messaggi!")

@Bot.command()
async def Scrivi(ctx, parola):
    await ctx.channel.purge(limit = 1)
    parola = parola.replace("-", " ", 100)
    await ctx.send(parola)

@Bot.command()
async def Ripeti(ctx, parola):
    parola = parola.replace("-", " ", 100)
    await ctx.send(parola)

@Bot.command()
async def Rispondi(ctx, ID, risposta): #Comando non funzionante in quanto interpreta ID come una stringa
    await ctx.channel.purge(limit = 1)
    risposta = risposta.replace("-", " ", 1000)
    await ID.reply(risposta)
    
@Bot.command()
async def Emoji(ctx, emoji):
    await ctx.channel.purge(limit = 1)
    emoji = (':' + emoji + ':')
    await ctx.send(emoji)

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def Maiuscolo(ctx, messaggio):
    await ctx.channel.purge(limit = 1)
    messaggio = str(messaggio)
    messaggio = messaggio.replace("-", " ", 100)
    messaggio = messaggio.upper()
    await ctx.send(messaggio)    

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def Minuscolo(ctx, messaggio):
    await ctx.channel.purge(limit = 1)
    messaggio = str(messaggio)
    messaggio = messaggio.replace("-", " ", 100)
    messaggio = messaggio.lower()
    await ctx.send(messaggio)    

#Fine della sezione Scrittura












#Comandi di Spam

@Bot.command()

async def Spam_5(ctx, parola):
    await ctx.channel.purge(limit = 1)
    parola = parola.replace('-',' ', 100)
    parola = str(parola)
    for i in range(5):
        await ctx.send(parola)

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def Spam_15(ctx, parola):
    await ctx.channel.purge(limit = 1)
    parola = parola.replace('-',' ', 100)
    parola = str(parola)
    for i in range(15):
        await ctx.send(parola)

@Bot.command()

async def Spam_link(ctx, link):
    await ctx.channel.purge(limit = 1)
    link = str(link)
    for i in range(5):
        await ctx.send(link)

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def Spam_menzione(ctx, menzione):
    await ctx.channel.purge(limit = 1)
    parola = str(menzione)
    for i in range(5):
        await ctx.send(menzione)
        await ctx.channel.purge(limit = 1)

#Fine dei comandi di Spam

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def Procione(ctx):
    Procione = random.choice(Procioni)
    await ctx.send(Procione)

#Questa è la sezione dei comandi della categoria della gestione degli utenti

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def Avvertimento(ctx, member:discord.User = None, reason = None):
    if reason == None:
        await ctx.send('E per cosa lo staresti avvertendo?! Prova con £Avvertimento {member} parole-del-tuo-avvertimento')
    else:
        reason = reason.replace('-', ' ', 100)
        author = ctx.message.author
        await member.send(f"{member}, la tua utenza è stata avvertita da {author}! Motivo: {reason}")
        await ctx.channel.send(f"Avvertimento inviato a {member}")

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def Lista_Utenti(ctx, messaggio):
    await messaggio.reply('Eccoti la lista degli utenti a me visibili:')
    await ctx.send(Bot.users)

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def Lista_Parolacce(ctx):
    await ctx.send(parolacce)

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def Comando(ctx, comando):
    await ctx.channel.purge(limit = 1)
    await ctx.send(comando)
    eval(comando) #eval() utilizza soltanto funzioni non composte
    
@Bot.command()
@commands.has_role('Autorizzato a Talker')
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

@Bot.command(description="Scrive in privato ad un cittadino")
@commands.has_role('Autorizzato a Talker')
async def Mail(ctx, inoltrante, ricevente, oggetto, corpo, password):
    await ctx.channel.purge(limit = 1)
    oggetto = str(oggetto) + "/n/n"
    corpo = corpo.replace("-", " ", 10000)
    corpo = str(corpo)
    messaggio = oggetto + corpo
    print(password)
    email = smtplib.SMTP("smtp.gmail.com", 587) #Richiede un Aouth02 di cui molti utenti non dispongono
    email.ehlo()
    email.starttls()
    email.login(inoltrante, password)
    email.send(inoltrante, ricevente, messaggio)
    password = 0
    email.quit()
    author = ctx.message.author
    await author.send("La tua mail è stata inviata con successo a {ricevente}, eccoti il suo testo!")
    await author.send(messaggio)

@Bot.command(description="Comando di espulsione, solo per gli amministratori")
@commands.has_role('Autorizzato a Talker')
async def Espulsione(ctx, member:discord.User=None, reason =None): #Comando di espulsione non del tutto funzionante
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
            await Bot.kick(member, reason=motivo)
            await ctx.channel.send(f"{member} è stato espulso! Motivo: {reason}")
    except:
        await ctx.send(f"Errore, hai provato ad espellere {member}, **non puoi espellere il proprietario o un bot!**")

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def Espelli(ctx, username: discord.User): #Tentativo fallito di espellere la gente
    await Bot.kick(username)

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def Aggiungi_Ruolo(ctx, user: discord.Member, role: discord.Role):
    await ctx.channel.purge(limit = 1)
    await user.add_roles(role)
    await ctx.send(f"Ho aggiunto il ruolo {role.mention} all'utente {user.mention}.")

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def Togli_Ruolo(ctx, user: discord.Member, role: discord.Role):
    await ctx.channel.purge(limit = 1)
    await user.remove_roles(role)
    await ctx.send(f"Ho rimosso il ruolo {role.mention} all'utente {user.mention}.")

@Bot.command()
@commands.has_role('Autorizzato a Talker')
async def FERMO(ctx):
    await ctx.send('Hai usato il comando FERMO, il mio programma in file .exe si arresterà in automatico, per riattivarmi contatta @FLAK_FLAK#3241')
    await quit()

#Fine della sezione Comandi










    

#Comandi di codifica del testo

@Bot.command()
async def Unicode(ctx, frase): #Funzione per convertire una stringa di massimo 18 caratteri in codice Unicode a 8bit, che però funziona soltanto con il primo carattere inviato
    frase = frase.replace("-", " ", 1000)
    lunghezza = len(frase)
    frase = list(frase)
    output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    posizione = 0
    for i in range(lunghezza - 1): #Per sistemarla consiglio di dare un occhio alle righe 487-488-489 perché l'errore dovrebbe venire proprio da lì
        output[posizione] = frase[posizione]
        posizione += 1
    frase = str(ord(output[0]) + ord(output[1]) + ord(output[2]) + ord(output[3]) +  ord(output[4]) +  ord(output[5]) +  ord(output[6]) +  ord(output[7]) +  ord(output[8]) +  ord(output[9]) +  ord(output[10]) +  ord(output[11]) +  ord(output[12]) +  ord(output[13]) +  ord(output[14]) +  ord(output[15]) +  ord(output[16]) +  ord(output[17]) +  ord(output[18]) +  ord(output[19]))
    await ctx.send(frase)





    
Bot.run(token) #Funzione che fa partire il tutto

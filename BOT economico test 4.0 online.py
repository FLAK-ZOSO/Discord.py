import random
import discord
from discord.ext import commands
from discord import client
import time
import webbrowser

token = "ODI4MDA3ODc5MDY3MTcyODg1.YGjUbg.WXC9LRX1SZLvB16GFUuHmImfjY4"
client = commands.Bot(command_prefix = "$")

@client.event

async def on_ready():
    print(client.user, " è ora online ", "ID: ", client.user.id)

@client.command()

async def Benvenuto(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send("Benvenuto nel server")

@client.command()

async def Comando(ctx, comando): 
    await ctx.channel.purge(limit = 1)
    eval(comando) #eval() funziona solo per operazioni non composte
    
No = ["Niente", "niente", "Nnt", "nnt", "nulla", "Nulla", "no", "No", "NO"]
Sì = ["Sì", "sì", "si", "Si", "SI", "ok", "Ok", "OK"]
Giorno = 0

class cittadino:
    def __init__(self, nome, cognome, regione, disoccupato):
        self.nome = nome
        self.cognome = cognome
        self.regione = regione
        self.disoccupato = disoccupato
    def scheda_cittadino(self):
        if self.disoccupato in Sì:
            return f"{self.nome} {self.cognome} vive in {self.regione} ed è disoccupato"
        if self.disoccupato in No:
            return f"{self.nome} {self.cognome}: lavora come {self.lavoro} per conto di {self.datore_di_lavoro} con lo stipendio di {self.reddito}€ al mese, residente in {self.regione}"

class dipendente(cittadino):
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

class capo_di_azienda(cittadino):
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
    
class azienda:
    def __init__(self, nome, fondazione, proprietario, dipendenti, fatturato):
        self.nome = nome
        self.fondazione = input("Giorno di fondazione: ")
        if proprietario.lavoro == "Capo d'azienda":
            self.proprietario = proprietario
        else:
            return "L'utente {proprietario} non esiste."
        self.dipendenti = dipendenti
        self.fatturato = fatturato
        
@client.command()

async def Giorno(ctx): #Questo ancora non funziona
    Giorno = int(Giorno+1)
    await ctx.send(Giorno)
    
@client.command()

async def Aiuto_Cittadino(ctx):
    await ctx.send("syntax: $Cittadino nome, cognome, regione, disoccupato (Sì/No)")
    await ctx.send("nome = cittadino(nome, cognome, regione, disoccupato(sì/no))")
    await ctx.send("nome = lavoratore(nome, cognome, regione, disoccupato('-'), lavoro('-'), reddito('-'), datore_di_lavoro, tasse('-'))")

@client.command()

async def Account(ctx, self, nome, cognome, regione, disoccupato):
    self = cittadino(nome, cognome, regione, disoccupato)
    print(self.nome)
    await ctx.send("Se qualcosa è andato storto, digita '£Aiuto_Account'")

@client.command()

async def Lavoro(ctx, self, nome, cognome, regione, disoccupato, lavoro, reddito, datore_di_lavoro, tasse):
    self = lavoro(nome, cognome, regione, disoccupato, lavoro, reddito, datore_di_lavoro, tasse)

def Bilancio(username):
    if username in cittadino:
        print(username.patrimonio)
def Paga(username):
    if username in users:
        username.patrimonio += username.reddito
def Stipendio(username):
    print(username.reddito)
def Patrimonio(username):
    print(username.patrimonio)
def Tasse(cittadino): 
    if cittadino.reddito <= 1250:
        tasse = round(cittadino.reddito*0.23)
        cittadino.tasse = tasse
        print(tasse)
    if cittadino.reddito > 1250:
        tasse = round(1250*0.23)
        reddito_residuo = round(cittadino.reddito-1250)
        if cittadino.reddito  <= 2333:
            tasse = round(tasse + reddito_residuo*0.27)
            cittadino.tasse = tasse
            print(tasse)
        if cittadino.reddito > 2333:
            tasse = round(tasse + 1083*0.27)
            reddito_residuo = round(reddito_residuo - 1083)
            if cittadino.reddito  <= 4583:
                tasse = round(tasse + reddito_residuo*0.38)
                cittadino.tasse = tasse
                print(tasse)
            if cittadino.reddito > 4583:
                tasse = round(tasse + 2250*0.38)
                reddito_residuo = round(reddito_residuo - 2250)
                if cittadino.reddito  <= 6250:
                    tasse = round(tasse + reddito_residuo*0.41)
                    cittadino.tasse = tasse
                    print(tasse)
                if cittadino.reddito > 6250:
                    tasse = round(tasse + 1667*0.41)
                    reddito_residuo = round(reddito_residuo - 1667)
                    tasse = round(reddito_residuo*0.43)
                    cittadino.tasse = tasse
                    print(tasse)
def Contribuzione(username):
    if Giorno%30 != 0:
        "Non è ancora il momento di pagare le tasse."
    if Giorno%30 == 0:
        Tasse(username)
        print(username.tasse)
        username.patrimonio = round(username.patrimonio-username.tasse)
        
client.run(token)

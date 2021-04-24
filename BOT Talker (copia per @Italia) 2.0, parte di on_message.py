import random
import string
import discord
from discord.ext import commands
from discord.utils import get
from discord import client
import time
import webbrowser
import asyncio

print("Eseguendo il programma...")
token = "ODI4MDA3ODc5MDY3MTcyODg1.YGjUbg.WXC9LRX1SZLvB16GFUuHmImfjY4"
Bot = commands.Bot(command_prefix = "$")

@Bot.event
async def on_ready():
    print(Bot.user, " è ora online ", "ID: ", Bot.user.id)

parolacce = ['fanculo', 'merda', 'troia', "stronza", "stronzo", 'Stronzo', "Stronza", "Troia", "Coglione", "COGLIONE", "PORCO"]
@Bot.event #Qui ci sarà l'elenco dei vari messaggi ai quali reagire
async def on_message(messaggio):
    author = messaggio.author
    if author != Bot.user:
        if  messaggio.content == '$FERMO':
            await quit()
        if 'Italia' in messaggio.content or 'ITALIA' in messaggio.content or 'italia' in messaggio.content or 'Italia#5030' in messaggio.content or '@Italia#5030' in messaggio.content:
            sono_stato_menzionato = str(f'{author.mention}, perché mi hai menzionato? Trovi la mia lista comandi con $Aiuto.')
            await messaggio.reply(sono_stato_menzionato)
            print(f'{author} MI HA MENZIONATO in {messaggio.channel}!')
        for i in parolacce:
            if i in messaggio.content:
                await messaggio.reply(f"{author.mention}, non dire parolacce, trovi le parolacce con $Lista_Parolacce")
                return
            
        if 'Cazzo' in messaggio.content or 'CAZZO' in messaggio.content or 'cazzo' in messaggio.content:
            if 'Cazzo' in messaggio.content:
                parolaccia = 'Cazzo'
            if 'CAZZO' in messaggio.content:
                parolaccia = 'CAZZO'
            if 'cazzo' in messaggio.content:
                parolaccia = 'cazzo'
            print(f"{author} ha detto '{parolaccia}' in {messaggio.channel}.")
            parolaccia = str(f"{author.mention}, hai detto '{parolaccia}', modera il linguaggio.")
            await messaggio.reply(parolaccia)
            await messaggio.reply(f'Segnalalo con `$Avvertimento {author.mention} regola-il-linguaggio`')
            await author.send(f'Hai detto {parolaccia}. Nel server dove ti trovavi è da preferirsi un linguaggio meno scurrile.')
            
        if 'Puttana' in messaggio.content or 'PUTTANA' in messaggio.content or 'puttana' in messaggio.content:
            if 'Puttana' in messaggio.content:
                parolaccia = 'Puttana'
            if 'PUTTANA' in messaggio.content:
                parolaccia = 'PUTTANA'
            if 'puttana' in messaggio.content:
                parolaccia = 'puttana'
            print(f"{author} ha detto '{parolaccia}' in {messaggio.channel}.")
            parolaccia = str(f"{author.mention}, hai detto '{parolaccia}', modera il linguaggio.")
            await messaggio.reply(parolaccia)
            await messaggio.reply(f'Segnalalo con `$Avvertimento {author.mention} regola-il-linguaggio`')
            await author.send(f'Hai detto {parolaccia}. Nel server dove ti trovavi è da preferirsi un linguaggio meno scurrile.')

Bot.run(token)

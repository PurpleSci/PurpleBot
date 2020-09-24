import discord
import os
import random
from discord.ext import commands

client = commands.Bot(command_prefix="p:")

greetings = ["Hello!", "Hallo!", "Bonjour!", "Ciao!", "¡Hola!",
             "Hej!", "Ahoj!", "Aloha!", "Привет!", "Χαίρετε!",
             "你好!", "こんにちは!", "여보세요!", "!مرحبا", "हैलो!"]

predictions = ["Yeah, sure. But don't disturb me again anytime soon, OK?", "I guess, no.", "I'm too busy to bother with you now. Please ask again later. Or, better, don't ask me anything ever. I'm a bad predictor, you know."]

vowels = ["a","e","i","o","u","y"]

consonants = ["b","c","d","f","g","h","j","k","l","m", \
                 "n","p","q","r","s","t","v","w","x","z"]

@client.event
async def on_connect():
    print("Connecting to Discord.....")

@client.event
    await client.change_presence(status=discord.Status.online,
    activity=discord.Game(f"Type \'p:help\' for the commands. On {len(client.guilds)} active servers"))
    print('PurpleBot has connected to Discord.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Client-side ping took {round(client.latency * 1000)}ms')

@client.command()
async def about(ctx):
    await ctx.send(f'PurpleBot is a Discord bot by Purple Scientist written in Python.')

@client.command()
async def license(ctx):
    await ctx.send(f'PurpleBot is licensed under MIT. That means it\'s open-source and you are free to redistribute your own modifications of the bot.')

@client.command()
async def github(ctx):
    await ctx.send(f'PurpleBot\'s source code is avalaible at GitHub: https://github.com/PurpleSci/PurpleBot')

@client.command()
async def invite(ctx):
    await ctx.send(f'If you want to integrate PurpleBot into your server, use this link: https://discord.com/api/oauth2/authorize?client_id=750677937837178920&permissions=8&scope=bot')

@client.command()
async def hello(ctx):
    await ctx.send(random.choice(greetings))

@client.command()
async def predict(ctx):
    await ctx.send(random.choice(predictions))

@client.command()
async def pogchamp(ctx):
    await ctx.send('''
░░░░░▒░░▄██▄░▒░░░░░░
░░░▄██████████▄▒▒░░░
░▒▄████████████▓▓▒░░
▓███▓▓█████▀▀████▒░░
▄███████▀▀▒░░░░▀█▒░░
████████▄░░░░░░░▀▄░░
▀██████▀░░▄▀▀▄░░▄█▒░
░█████▀░░░░▄▄░░▒▄▀░░
░█▒▒██░░░░▀▄█░░▒▄█░░
░█░▓▒█▄░░░░░░░░░▒▓░░
░▀▄░░▀▀░▒░░░░░▄▄░▒░░
░░█▒▒▒▒▒▒▒▒▒░░░░▒░░░
░░░▓▒▒▒▒▒░▒▒▄██▀░░░░
░░░░▓▒▒▒░▒▒░▓▀▀▒░░░░
░░░░░▓▓▒▒░▒░░▓▓░░░░░
░░░░░░░▒▒▒▒▒▒▒░░░░░░
''')

@client.command()
async def pi(ctx):
    await ctx.send(f'Here is π calculated to the first 1000000 digits: http://newton.ex.ac.uk/research/qsystems/collabs/pi/pi6.txt')

@client.command()
async def ptable(ctx):
    await ctx.send(f'Ptable is an interactive online version of the Periodic Table of Elements: https://ptable.com/')

@client.command()
async def rubbish(ctx):
    sentence = ""
    for i in range(random.randrange(3,7)):
        word = str()
        for j in range(random.randrange(1,5)):
            word = word + random.choice(consonants) + random.choice(vowels)
        sentence = sentence + word + " "
    await ctx.send(sentence.capitalize().rstrip() + random.choice(["!","?","."]))
    
@client.event
async def on_disconnect():
    print("PurpleBot disconnected.")

client.run(os.environ['DISCORD_TOKEN'])

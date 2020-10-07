import discord
import os
import random
from discord.ext import commands

client = commands.Bot(command_prefix="p:")

greetings = ["Hello!", "Hallo!", "Bonjour!", "Ciao!", "¡Hola!",
             "Hej!", "Ahoj!", "Aloha!", "Привет!", "Χαίρετε!",
             "你好!", "こんにちは!", "여보세요!", "!مرحبا", "हैलो!"]

predictions = ["Yeah, sure.", "Probably yes.", "I guess, no.", "What about no?", "Ask again later.", "I'm busy now, you know."]

death_scenarios = ["A snake bit you.", "You met a vampire and he sucked all your blood.", \
                   "You drank a glass of juice, but there was poison inside.", \
                   "You were thrown out into space by a giant gorilla.", "You ate too much mushrooms.", \
                   "A heavy hammer fell onto your head.", "A zombie strangled you to death.", \
                   "A maniac cut your throat while you were sleeping.", "You became too old.", \
                   "You decided that you've had enough and committed suicide.", \
                   "You wanted to take a vacation in Chernobyl.", \
                   "Voldemort came to you and said 'Avada Kedavra!'", \
                   "You were trying to install Gentoo Linux, but failed."]

scary_things = ["😈", "💀", "👻", "🎃", "🧛‍♂️", "🦇", "🕷", "🧟"]

vowels = ["a","e","i","o","u","y"]

consonants = ["b","c","d","f","g","h","j","k","l","m", \
                 "n","p","q","r","s","t","v","w","x","z"]

@client.event
async def on_connect():
    print("Connecting to Discord.....")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
    activity=discord.Game(f"Type \'p:help\' for the commands. On {len(client.guilds)} servers"))
    print("PurpleBot has connected to Discord")

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
async def randnum(ctx):
    await ctx.send(random.randint(0, 10000))

@client.command()
async def predict(ctx):
    await ctx.send(random.choice(predictions))

@client.command()
async def die(ctx):
    await ctx.send(random.choice(death_scenarios))

@client.command()
async def boo(ctx):
    await ctx.send(random.choice(scary_things))

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

# Let's make the Discord.py module understand that there is a folder for additional commands (cogs).

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['DISCORD_TOKEN'])

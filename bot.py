import discord
import os
import math
import random
from discord.ext import commands

client = commands.Bot(command_prefix="p:")
client.remove_command('help')

greetings = [
    "Hello!", "Hallo!", "Bonjour!", "Ciao!", "¡Hola!",
    "Hej!", "Ahoj!", "Aloha!", "Привет!", "Χαίρετε!",
    "你好!", "こんにちは!", "여보세요!", "!مرحبا", "हैलो!"
]

predictions = [
    "Yeah, sure.", "Probably yes.", "Yes, totally.", "Obviously, yes!",
    "I guess, no.", "What about no?", "Nah. Not at all.", "Are you kidding me? Of course, no!",
    "Hmm, I don't know.", "I can't tell.", "I can't tell right now, try again later.",
    "Sorry Link, I can't *give* free predictions. Come back when you're a little, mmmmmmm... richer!"
]

death_scenarios = [
    "A snake bit you.", "You met a vampire and he sucked all your blood.", \
    "You drank a glass of juice, but there was poison inside.", \
    "You were thrown out into space by a giant monkey.", "You decided to eat 1,000,000 chips.", \
    "A heavy hammer fell onto your head.", "A zombie strangled you to death.", \
    "A maniac cut your throat while you were sleeping.", "You became too old.", \
    "You committed suicide.", \
    "You wanted to take a vacation in Pripyat.", \
    "Voldemort came to you and said \'Avada Kedavra!\'", \
    "You were trying to install Gentoo, but failed.", \
    "Jigglypuff hugged you too hard.", \
    "You weren't rich enough when you went to buy lamp oil, rope, and bombs."
]

vowels_en = ["a","e","i","o","u"]

consonants_en = [
    "b","c","d","f","g","h","j","k","l","m", \
    "n","p","q","r","s","t","v","w","x","y","z"
]

vowels_ru = ["а","е","и","о","у","ы","э","ю","я"]

consonants_ru = ["б","в","г","д","ж","з","к","л","м","н", \
                 "п","р","с","т","ф","х","ц","ч","ш","щ",]

@client.event
async def on_connect():
    print("Connecting to Discord...")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
    activity=discord.Game(f"p:help | {len(client.guilds)} servers"))
    print("PurpleBot has connected to Discord.")

@client.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: Pong! Client-side ping latency is **{round(client.latency * 1000)}ms**')

@client.command()
async def about(ctx):
    await ctx.send(f':robot: PurpleBot is a Discord bot by Purple Scientist written in Python.')

@client.command()
async def license(ctx):
    await ctx.send(f':page_facing_up: PurpleBot is licensed under MIT. That means it\'s open-source and you are free to redistribute your own modifications of the bot.')

@client.command()
async def github(ctx):
    await ctx.send(f':computer: PurpleBot\'s source code is avalaible at GitHub: https://github.com/PurpleSci/PurpleBot')

@client.command()
async def invite(ctx):
    await ctx.send(f':arrow_right: If you want to add PurpleBot to your server, use this link: https://discord.com/api/oauth2/authorize?client_id=750677937837178920&permissions=8&scope=bot')

@client.command()
async def hello(ctx):
    await ctx.send(random.choice(greetings))

@client.command()
async def randnum(ctx,a,b):
    await ctx.send(random.randint(int(a), int(b)))

@client.command()
async def predict(ctx):
    await ctx.send(random.choice(predictions))

@client.command()
async def die(ctx):
    await ctx.send(random.choice(death_scenarios))

@client.command()
async def rick(ctx):
    await ctx.send(f'https://tenor.com/view/rick-ashley-dance-80s-music-gif-12136175')

@client.command()
async def crabrave(ctx):
    await ctx.send(f'https://tenor.com/view/crabs-dancing-having-fun-having-party-party-gif-15660530')

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
async def sans(ctx):
    await ctx.send('''
░░░░░░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░░░░░░
░░░░░░░░░█░░░░░░░░░░░░░█░░░░░░░░░
░░░░░░░░█░░░░░░░░░░▄▄▄░░█░░░░░░░░
░░░░░░░░█░░▄▄▄░░▄░░███░░█░░░░░░░░
░░░░░░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░░░░░░
░░░░░░░░█░░▀█▀█▀█▀█▀█▀░░█░░░░░░░░
░░░░░░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░░░░░░
░░░░░░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░░░░░░
░░░░░▄▀░▄▄▀▄▄▀▀▀▄▀▀▀▄▄▀▄▄░▀▄░░░░░
░░░░░█░░░░▀▄░█▄░░░▄█░▄▀░░░░█░░░░░
░░░░░░▀▄▄░█░░█▄▄▄▄▄█░░█░▄▄▀░░░░░░
░░░░░░░░▀██▄▄███████▄▄██▀░░░░░░░░
░░░░░░░░████████▀████████░░░░░░░░
░░░░░░░▄▄█▀▀▀▀█░░░█▀▀▀▀█▄▄░░░░░░░
░░░░░░░▀▄▄▄▄▄▀▀░░░▀▀▄▄▄▄▄▀░░﻿░░░░░
''')

@client.command()
async def add(ctx,a,b):
    await ctx.send(float(a) + float(b))

@client.command()
async def subtract(ctx,a,b):
    await ctx.send(float(a) - float(b))

@client.command()
async def multiply(ctx,a,b):
    await ctx.send(float(a) * float(b))

@client.command()
async def divide(ctx,a,b):
    await ctx.send(float(a) / float(b))

@client.command()
async def power(ctx,a,b):
    await ctx.send(float(a) ** float(b))

@client.command()
async def sqrt(ctx,a):
    await ctx.send(math.sqrt(float(a)))

@client.command()
async def pi(ctx):
    await ctx.send(f'π = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679...')

@client.command()
async def ptable(ctx):
    await ctx.send(f'Ptable is an interactive online version of the Periodic Table of Elements: https://ptable.com/')

@client.command()
async def rubbish(ctx,lang):
    sentence = ""
    if lang == "en" or lang == "ru":
        for i in range(random.randrange(3,7)):
            word = str()
            if lang == "en":
                for j in range(random.randrange(1,5)):
                    word = word + random.choice(consonants_en) + random.choice(vowels_en)
            if lang == "ru":
                for j in range(random.randrange(1,5)):
                    word = word + random.choice(consonants_ru) + random.choice(vowels_ru)
            sentence = sentence + word + " "
        await ctx.send(sentence.capitalize().rstrip() + random.choice(["!","?","."]))
    else:
        await ctx.send(f'Please choose a correct language.')

@client.command()
async def say(ctx,*,arg):
    await ctx.channel.purge(limit=1)
    if(arg != "@everyone"):
        if (arg != "@here"):
            await ctx.send(f"{arg}")
        else:
            await ctx.send("You are not allowed to ping `@here`. Continuing this act will result in a punishment.")
    else:
        await ctx.send("You are not allowed to ping `@everyone`. Continuing this act will result in a punishment.")

@client.command()
async def piglatin(ctx,word):
    if word[0] in "aeiou":
        await ctx.send(word + 'way')
    else:
        await ctx.send(word[1:] + word[0] + 'ay')

@client.command()
async def avatar(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.purple(), title=f"{member}'s avatar")
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)

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

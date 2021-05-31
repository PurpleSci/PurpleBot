import discord
import os
import math
import random
import requests
from discord.ext import commands

bot = commands.Bot(command_prefix="p:")
bot.remove_command('help')

api_key = "80f144b817b3a44688f3e15b237db53f"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

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
    "n","p","q","r","s","t","v","w","x","y","z"]

vowels_ru = ["а","е","и","о","у","ы","э","ю","я"]

consonants_ru = ["б","в","г","д","ж","з","к","л","м","н", \
                 "п","р","с","т","ф","х","ц","ч","ш","щ"]

@bot.event
async def on_connect():
    print("Connecting to Discord...")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"p:help | {len(bot.guilds)} servers"))
    print("PurpleBot has connected to Discord.")

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! **{round(bot.latency * 1000)} ms**')

@bot.command()
async def about(ctx):
    await ctx.send(f'PurpleBot is a Discord bot by Purple Scientist written in Python.')

@bot.command()
async def license(ctx):
    await ctx.send(f'PurpleBot is licensed under MIT. That means it\'s open-source and you are free to redistribute your own modifications of the bot.')

@bot.command()
async def github(ctx):
    await ctx.send(f'PurpleBot\'s source code is avalaible at GitHub: https://github.com/PurpleSci/PurpleBot')

@bot.command()
async def invite(ctx):
    await ctx.send(f'If you want to add PurpleBot to your server, use this link: https://discord.com/api/oauth2/authorize?bot_id=750677937837178920&permissions=8&scope=bot')

@bot.command()
async def hello(ctx):
    await ctx.send(random.choice(greetings))

@bot.command()
async def randnum(ctx,a,b):
    await ctx.send(random.randint(int(a), int(b)))

@bot.command()
async def predict(ctx):
    await ctx.send(random.choice(predictions))

@bot.command()
async def die(ctx):
    await ctx.send(random.choice(death_scenarios))

@bot.command()
async def rick(ctx):
    await ctx.send(f'https://tenor.com/view/rick-ashley-dance-80s-music-gif-12136175')

@bot.command()
async def crab(ctx):
    await ctx.send(f'https://tenor.com/view/crabs-dancing-having-fun-having-party-party-gif-15660530')

@bot.command()
async def gandalf(ctx):
    await ctx.send(f'https://tenor.com/view/gandalf-happy-dance-lord-of-the-rings-lotr-gif-3551563')

@bot.command()
async def calc(ctx, operation, *nums):
    if operation not in ['+', '-', '*', '/']:
        await ctx.send('Please enter a valid operation type.')
    var = f' {operation} '.join(nums)
    await ctx.send(f'{var} = {eval(var)}')

@bot.command()
async def pi(ctx):
    await ctx.send(f'π = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679...')

@bot.command()
async def rubbish(ctx, lang):
    sentence = ""
    for i in range(random.randrange(3,7)):
        word = str()
        if lang == "ru":
            for j in range(random.randrange(1,5)):
                word = word + random.choice(consonants_ru) + random.choice(vowels_ru)
        else:
            for j in range(random.randrange(1,5)):
                word = word + random.choice(consonants_en) + random.choice(vowels_en)
        sentence = sentence + word + " "
    await ctx.send(sentence.capitalize().rstrip() + random.choice(["!","?","."]))

@bot.command()
async def say(ctx,*,arg):
    await ctx.channel.purge(limit=1)
    if(arg != "@everyone"):
        if (arg != "@here"):
            await ctx.send(f"{arg}")
        else:
            await ctx.send("You are not allowed to ping `@here`. Continuing this act will result in a punishment.")
    else:
        await ctx.send("You are not allowed to ping `@everyone`. Continuing this act will result in a punishment.")

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    embed = discord.Embed(title=f"{member}'s avatar",
                          color=ctx.guild.me.top_role.color, 
                          timestamp=ctx.message.created_at)
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def weather(ctx, *, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_temperature_celsius = str(round(current_temperature - 273.15))
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]        
        embed = discord.Embed(title=f"Weather in {city_name}",
                            color=ctx.guild.me.top_role.color,
                            timestamp=ctx.message.created_at)
        embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
        embed.add_field(name="Temperature (C)", value=f"**{current_temperature_celsius}°C**", inline=False)
        embed.add_field(name="Humidity (%)", value=f"**{current_humidity}%**", inline=False)
        embed.add_field(name="Atmospheric Pressure (hPa)", value=f"**{current_pressure} hPa**", inline=False)
        embed.set_thumbnail(url="https://portal.trta.org/imis15/images/TRTA/sun.png")
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        await channel.send(embed=embed)
    else:
        await channel.send("City not found.")

@bot.event
async def on_disconnect():
    print("PurpleBot disconnected.")

# Let's make the Discord.py module understand that there is a folder for additional commands (cogs).

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.environ['DISCORD_TOKEN'])

import discord
import os
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
    "I guess, no.", "What about no?", "Nah. Not at all.", "Are you kidding me? Of course, no!"
]

death_scenarios = [
    "A snake bit you.", "You met a vampire and he sucked all your blood.", \
    "You drank a glass of juice, but there was poison inside.", \
    "You were thrown out into space by a giant monkey.", "You ate too many mushrooms.", \
    "A heavy hammer fell onto your head.", "A zombie strangled you to death.", \
    "A maniac cut your throat while you were sleeping.", "You became too old.", \
    "You decided that you've had enough and committed suicide.", \
    "You wanted to take a vacation in Chernobyl.", \
    "Voldemort came to you and said \'Avada Kedavra!\'", \
    "You were trying to install Arch Linux, but failed."
]

scary_things = ["😈", "💀", "👻", "🎃", "🧛‍♂️", "🦇", "🧟"]

windows_versions = [
    "Windows 1.x", \
    "Windows 2.x", \
    "Windows 3.x", \
    "Windows 95", \
    "Windows 98", \
    "Windows 2000", \
    "Windows Me", \
    "Windows XP", \
    "Windows Vista", \
    "Windows 7", \
    "Windows 8", \
    "Windows 10"
]

macos_versions = [
    "macOS 10.0 (Cheetah)", \
    "macOS 10.1 (Puma)", \
    "macOS 10.2 (Jaguar)", \
    "macOS 10.3 (Panther)", \
    "macOS 10.4 (Tiger)", \
    "macOS 10.5 (Leopard)", \
    "macOS 10.6 (Snow Leopard)", \
    "macOS 10.7 (Lion)", \
    "macOS 10.8 (Mountain Lion)", \
    "macOS 10.9 (Mavericks)", \
    "macOS 10.10 (Yosemite)", \
    "macOS 10.11 (El Capitan)", \
    "macOS 10.12 (Sierra)", \
    "macOS 10.13 (High Sierra)", \
    "macOS 10.14 (Mojave)", \
    "macOS 10.15 (Catalina)", \
    "macOS 11.0 (Big Sur)"
]

distros = [
    "Ubuntu", \
    "Debian", \
    "Arch", \
    "Manjaro", \
    "Fedora", \
    "OpenSUSE", \
    "RHEL", \
    "CentOS", \
    "Linux Mint", \
    "elementary OS", \
    "Pop!_OS", \
    "Solus", \
    "Gentoo", \
    "Slackware", \
    "Alpine", \
    "Void", \
    "Deepin", \
    "KDE neon", \
    "Kali Linux", \
    "MX Linux", \
    "Linux Lite", \
    "Endeavour OS", \
    "Zorin OS", \
    "Feren OS", \
]

ubuntu_versions = [
    "Ubuntu 4.10 (Warty Warthog)", \
    "Ubuntu 5.04 (Hoary Hedgehog)", \
	"Ubuntu 5.10 (Breezy Badger)", \
    "Ubuntu 6.06 LTS (Dapper Drake)", \
	"Ubuntu 6.10 (Edgy Eft)", \
	"Ubuntu 7.04 (Feisty Fawn)", \
	"Ubuntu 7.10 (Gutsy Gibbon)", \
	"Ubuntu 8.04 LTS (Hardy Heron)", \
	"Ubuntu 8.10 (Intrepid Ibex)", \
	"Ubuntu 9.04 (Jaunty Jackalope)", \
	"Ubuntu 9.10 (Karmic Koala)",  \
	"Ubuntu 10.04 LTS (Lucid Lynx)",  \
	"Ubuntu 10.10 (Maverick Meerkat)",  \
	"Ubuntu 11.04 (Natty Narwhal)",  \
	"Ubuntu 11.10 (Oneiric Ocelot)",  \
	"Ubuntu 12.04 LTS (Precise Pangolin)",  \
	"Ubuntu 12.10 (Quantal Quetzal)",  \
	"Ubuntu 13.04 (Raring Ringtail)",  \
	"Ubuntu 13.10 (Saucy Salamander)",  \
	"Ubuntu 14.04 LTS (Trusty Tahr)",  \
	"Ubuntu 14.10 (Utopic Unicorn)",  \
	"Ubuntu 15.04 (Vivid Vervet)",  \
	"Ubuntu 15.10 (Wily Werewolf)",  \
	"Ubuntu 16.04 LTS (Xenial Xerus)",  \
	"Ubuntu 16.10 (Yakkety Yak)",  \
	"Ubuntu 17.04 (Zesty Zapus)",  \
	"Ubuntu 17.10 (Artful Aardvark)",  \
	"Ubuntu 18.04 LTS (Bionic Beaver)",  \
	"Ubuntu 18.10 (Cosmic Cuttlefish)",  \
	"Ubuntu 19.04 (Disco Dingo)",  \
	"Ubuntu 19.10 (Eoan Ermine)",  \
	"Ubuntu 20.04 LTS (Focal Fossa)",  \
	"Ubuntu 20.10 (Groovy Gorilla)", \
    "Ubuntu 21.04 (Hirsute Hippo)"
]

debian_versions = [
    "Debian 1.1 (Buzz)", \
    "Debian 1.2 (Rex)", \
    "Debian 1.3 (Bo)", \
    "Debian 2.0 (Hamm)", \
    "Debian 2.1 (Slink)", \
    "Debian 2.2 (Potato)", \
    "Debian 3.0 (Woody)", \
    "Debian 3.1 (Sarge)", \
    "Debian 4.0 (Etch)", \
    "Debian 5.0 (Lenny)", \
    "Debian 6.0 (Squeeze)", \
    "Debian 7 (Wheezy)", \
    "Debian 8 (Jessie)", \
    "Debian 9 (Stretch)", \
    "Debian 10 (Buster)", \
    "Debian 11 (Bullseye)", \
    "Debian 12 (Bookworm)", \
    "Debian 13 (Trixie)"
]

android_versions = [
    "Android 1.5 (Cupcake)", \
    "Android 1.6 (Donut)", \
    "Android 2.0 (Eclair)", \
    "Android 2.2 (Froyo)", \
    "Android 2.3 (Gingerbread)", \
    "Android 3.0 (Honeycomb)", \
    "Android 4.0 (Ice Cream Sandwich)", \
    "Android 4.1 (Jelly Bean)", \
    "Android 4.4 (KitKat)", \
    "Android 5.0 (Lollipop)", \
    "Android 6.0 (Marshmallow)", \
    "Android 7.0 (Nougat)", \
    "Android 8.0 (Oreo)", \
    "Android 9 (Pie)", \
    "Android 10", \
    "Android 11", \
    "Android 12"
]

vowels_en = ["a","e","i","o","u","y"]

consonants_en = [
    "b","c","d","f","g","h","j","k","l","m", \
    "n","p","q","r","s","t","v","w","x","z"
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
async def rick(ctx):
    await ctx.send(f'https://tenor.com/view/rick-astley-rick-roll-dancing-dance-moves-gif-14097983')

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
async def windows(ctx):
    await ctx.send(random.choice(windows_versions))

@client.command()
async def macos(ctx):
    await ctx.send(random.choice(macos_versions))

@client.command()
async def distro(ctx):
    await ctx.send(random.choice(distros))

@client.command()
async def ubuntu(ctx):
    await ctx.send(random.choice(ubuntu_versions))

@client.command()
async def debian(ctx):
    await ctx.send(random.choice(debian_versions))

@client.command()
async def android(ctx):
    await ctx.send(random.choice(android_versions))

@client.command()
async def gnu(ctx):
    await ctx.send(
'''
I'd just like to interject for a moment. What you’re referring to as Linux, is in fact, GNU/Linux, or as I’ve recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.

Many computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called “Linux”, and many of its users are not aware that it is basically the GNU system, developed by the GNU Project. There really is a Linux, and these people are using it, but it is just a part of the system they use.

Linux is the kernel: the program in the system that allocates the machine’s resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called “Linux” distributions are really distributions of GNU/Linux.
'''
    )

@client.command()
async def groovy(ctx):
    await ctx.send(f'https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_500,h_776/https://assets.ubuntu.com/v1/fe951eda-20.10_Groovy+Gorilla_RPi_Sketch.svg')

@client.command()
async def pi(ctx):
    await ctx.send(f'Here is π calculated to the first 1000000 digits: http://newton.ex.ac.uk/research/qsystems/collabs/pi/pi6.txt')

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
async def avatar(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.purple(), title=f"{member}'s avatar")
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)

@client.command()
async def beemovie(ctx):
    await ctx.send("So you want to read the entire Bee Movie script, huh? What are you doing with your life? Anyway, if you really need it that much, here you go: https://gist.githubusercontent.com/The5heepDev/a15539b297a7862af4f12ce07fee6bb7/raw/7164813a9b8d0a3b2dcffd5b80005f1967887475/entire_bee_movie_script")

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

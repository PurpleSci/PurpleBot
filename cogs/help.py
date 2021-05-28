import discord
import os
import random
from discord.ext import commands

class Help(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    async def help(self,ctx):
        await ctx.send('''

**PurpleBot Command List**

**Moderation**
`ban, kick, mute, unban, unmute`

**Fun**
`crabrave, die, hello, piglatin, \
pog, predict, randnum, rick, \
sans, say`

**Science & Math**
`add, subtract, multiply, divide, \
power, sqrt, pi, weather`

**Utility**
`about, avatar, github, help, \
invite, license, ping`
 ''')
  
def setup(client):
    client.add_cog(Help(client))

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

:police_officer: **Moderation:**
`ban`
`kick`
`mute`
`unban`
`unmute`

:joy: **Fun:**
`crabrave`
`die`
`hello`
`piglatin`
`predict`
`randnum`
`rick`
`say`

:regional_indicator_a: **ASCII Art:**
`gollum`
`pikachu`
`tux`

:microscope: **Science & Math:**
`add`
`subtract`
`multiply`
`divide`
`power`
`sqrt`
`pi`
`ptable`

:gear: **Utility:**
`about`
`avatar`
`github`
`help`
`invite`
`license`
`ping`
 ''')
  
def setup(client):
    client.add_cog(Help(client))

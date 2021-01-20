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
`boo`
`beemovie`
`crabrave`
`die`
`hello`
`pogchamp`
`predict`
`randnum`
`rick`
`say`

:microscope: **Science:**
`pi`
`ptable`

:desktop: **IT & Linux: **
`android`
`debian`
`distro`
`gnu`
`groovy`
`macos`
`ubuntu`
`windows`

:gear: **Utility:**
`about`
`avatar`
`github`
`help`
`invite`
`license`
`ping`
`unload`
 ''')
  
def setup(client):
    client.add_cog(Help(client))

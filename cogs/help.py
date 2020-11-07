import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import has_permissions
from time import sleep
from datetime import datetime

class Help(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def help(self,ctx):
        await ctx.send('''
**```
PurpleBot's commands.
```**
Categories:

Moderation: 
   ban, kick, mute, unban, unmute
Fun: 
   boo, crabrave, die, hello, pogchamp, predict, randnum, meme
Science: 
   pi, ping
Linux: 
   debian, distro, groovy, interject, ubuntu
Utility: 
   about, github, help, invite, license, ping, unload
 ''')
  
def setup(client):
    client.add_cog(Help(client))

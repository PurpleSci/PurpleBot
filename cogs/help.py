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
**```
PurpleBot's commands.
```**
*```
Categories:
```*
```
Moderation: 
   ban, kick, mute, unban, unmute
```
```
Fun: 
   boo, crabrave, die, hello, pogchamp, predict, randnum, meme
```
```
Science: 
   pi, ping
```
```
Linux: 
   debian, distro, groovy, interject, ubuntu
```
```
Utility: 
   about, github, help, invite, license, ping, unload
```
 ''')
  
def setup(client):
    client.add_cog(Help(client))

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
PurpleBot Command List
```**
```
Moderation: 
ban
kick
mute
unban
unmute
```
```
Fun: 
boo
crabrave
die
hello
pogchamp
predict
randnum
rick
say
```
```
Science: 
pi
ptable
```
```
IT & Linux: 
android
debian
distro
gnu
groovy
macos
ubuntu
windows
```
```
Utility: 
about
avatar
github
help
invite
license
ping
unload
```
 ''')
  
def setup(client):
    client.add_cog(Help(client))

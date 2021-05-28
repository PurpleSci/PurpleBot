import discord
import os
import random
from discord.ext import commands

class Help(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(title=f"PurpleBot Command List",
                          color=ctx.guild.me.top_role.color, 
                          timestamp=ctx.message.created_at)
        embed.add_field(name="Moderation", value=f"`ban, kick, mute, unban, unmute`", inline=False)
        embed.add_field(name="Fun", value=f"`crabrave, die, hello, piglatin,
                                             pog, predict, randnum, rick,
                                             sans, say`", inline=False)
        embed.add_field(name="Science & Math", value=f"`add, subtract, multiply, divide,
                                                        power, sqrt, pi, weather`", inline=False)
        embed.add_field(name="Utility", value=f"about, avatar, github, help,
                                                invite, license, ping", inline=False)                                                
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))

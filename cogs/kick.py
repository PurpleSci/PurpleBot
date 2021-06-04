import discord
import os
from discord.ext import commands
from discord.ext.commands import has_permissions

class Moderation(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def kick(self,ctx,member : discord.Member, *, reason = None):
        embed=discord.Embed(title="Kicked.", color=discord.Colour.purple())
        await member.kick(reason=reason)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Moderation(client))

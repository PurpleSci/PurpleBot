import discord
import os
from discord.ext import commands
from discord.ext.commands import has_permissions

class Moderation(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def unmute(self,ctx,member : discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        embed=discord.Embed(title=":white_check_mark: Unmuted!", color=discord.Colour.purple())
        await ctx.send(embed=embed)
        await member.remove_roles(role)


def setup(client):
    client.add_cog(Moderation(client))

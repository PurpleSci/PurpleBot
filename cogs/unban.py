import discord
import os
from discord.ext import commands
from discord.ext.commands import has_permissions

class Moderation(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def unban(self,ctx, *, member):
        embed=discord.Embed(title=":white_check_mark: Unbanned!", color=discord.Colour.purple())
        await ctx.send(embed=embed)

        banned_users = await ctx.guild.bans()

        for ban_entry in banned_users:
            user = ban_entry.user
            await ctx.guild.unban(user)

def setup(client):
    client.add_cog(Moderation(client))
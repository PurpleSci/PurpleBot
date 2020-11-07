import discord
import os
from discord.ext import commands
from discord.ext.commands import has_permissions

class Moderation(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def mute(self,ctx,member : discord.Member, *, reason = None):
        embed=discord.Embed(title=":white_check_mark: Muted!", color=discord.Colour.purple())
        await ctx.send(embed=embed)
        
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True
        if discord.utils.get(ctx.guild.roles, name="Muted"):
            await member.add_roles(role)
        else:
            role = await ctx.guild.create_role(name='Muted', permissions=discord.Permissions(0))
            for channel in ctx.guild.channels:
                await channel.set_permissions(role, overwrite=overwrite)
        await member.add_roles(role)

def setup(client):
    client.add_cog(Moderation(client))
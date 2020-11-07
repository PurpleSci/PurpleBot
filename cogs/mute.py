import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import has_permissions
from time import sleep
from datetime import datetime

class Moderation(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def mute(self,ctx,member : discord.Member, *, reason = None):
        role = discord.utils.get(ctx.guild.roles, name="MutedUsers")
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True
        if discord.utils.get(ctx.guild.roles, name="MutedUsers"):
            await member.add_roles(role)
        else:
            role = await ctx.guild.create_role(name='MutedUsers', permissions=discord.Permissions(0))
            for channel in ctx.guild.channels:
                await channel.set_permissions(role, overwrite=overwrite)
        await ctx.send(f':white_check_mark: The user {user.mention} has been muted.')
        await member.add_roles(role)
        
    @commands.command()
    @has_permissions(administrator=True)
    async def unmute(self,ctx,member : discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="MutedUsers")
        await ctx.send(f":white_check_mark: The user {user.mention} has been unmuted.")
        await member.remove_roles(role)

def setup(client):
    client.add_cog(Moderation(client))

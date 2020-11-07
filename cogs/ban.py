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
    async def ban(self,ctx,member : discord.Member, *, reason = None):
        await ctx.send(f':white_check_mark: The user {user.mention} has been banned.')
        await member.ban(reason=reason)
        
    @commands.command()
    @has_permissions(administrator=True)
    async def unban(self,ctx, *, member):
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            await ctx.send(f':white_check_mark: The user {user.mention} has been unbanned.')
            await ctx.guild.unban(user)

def setup(client):
    client.add_cog(Moderation(client))

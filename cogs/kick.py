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
    async def kick(self,ctx,member : discord.Member, *, reason = None):
        await ctx.send(f':white_check_mark: The member {user.mention} has been kicked.')
        await member.kick(reason=reason)

def setup(client):
    client.add_cog(Moderation(client))

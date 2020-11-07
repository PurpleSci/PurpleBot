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
    @has_permissions(manage_messages=True)
    async def remove(self,ctx, amount : int):
        await ctx.send(F"Removing messages...")
        sleep(1)
        await ctx.channel.purge(limit=amount+1)
        sent = await ctx.send(F":white_check_mark: {amount} messages have been removed.")
        sleep(1)
        await sent.delete()

def setup(client):
    client.add_cog(Moderation(client)
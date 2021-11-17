import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import time


class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("Clear Cog Ready")

    @has_permissions(administrator=True)
    @commands.command(aliases=['c'])
    async def clear(self, ctx, amount = 1):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send("Cleared ``" + str(amount) + "`` Messages")
        time.sleep(0.5)
        await ctx.channel.purge(limit=1)

def setup(client):
    client.add_cog(Clear(client))

import disnake
from disnake.ext import commands
import asyncio


class Avatar(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Avatar Cog Ready")

    @commands.command(aliases=['a'])
    async def avatar(self, ctx):
        if ctx.message.mentions:
            await ctx.message.reply(ctx.message.mentions[0].avatar_url)
        else:
            await ctx.message.reply(ctx.message.author.avatar_url)

def setup(client):
    client.add_cog(Avatar(client))

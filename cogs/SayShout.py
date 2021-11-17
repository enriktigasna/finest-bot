import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio


class Say(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Say and Shout cog ready')

    @commands.command()
    @has_permissions(administrator=True)
    async def say(self, ctx, message=None):
        await ctx.send(f"{ctx.message.content} ".removeprefix(".say "))
        await ctx.message.delete()

    @commands.command()
    @has_permissions(administrator=True)
    async def shout(self, ctx, channel: discord.TextChannel):
        try:
            await channel.send(ctx.message.content[28:])
            await ctx.message.delete()
        except:
            embed=discord.Embed( color=0x17157e)
            embed.set_author(name=ctx.message.author.name + "#" + ctx.message.author.discriminator, icon_url=ctx.message.author.avatar_url)
            embed.add_field(name=".shout Usage", value=".shout \<channel\> \<input\>", inline=False)

def setup(client):
    client.add_cog(Say(client))

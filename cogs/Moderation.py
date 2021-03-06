import disnake
from disnake.ext import commands
from disnake.ext.commands import has_permissions

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation Cog Ready")

    # Add ban, mute and kick.. We need to check if user has perm to ban in general. And if the person they are banning is a role below them

    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx):
        if ctx.message.mentions():
            if ctx.message.author.top_role > ctx.message.mentions[0].top_role:
                await ctx.reply(f"Adios <@{ctx.author.id}>")
            else:
                await ctx.reply("lol you can't")
        else:
            await ctx.reply("Usage: .ban user [reason]")


def setup(client):
    client.add_cog(Moderation(client))

import nextcord
from nextcord.ext import commands
import asyncio



class BasicCommands(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Basic Command Cog Ready")

    @commands.command()
    async def suggest(self, ctx):
        await ctx.reply("**Suggest features or responses in fun commands.**\nhttps://docs.google.com/forms/d/e/1FAIpQLSd6aisR0uKNH8avEPdZWJVok843Yvmfso085s9pMkBrWZV10g/viewform?usp=sf_link")

    @commands.command()
    async def rules(self, ctx):
        embed=nextcord.Embed(title="Rules", color=0x37e154)
        embed.set_author(name=ctx.message.author.name + "#" + str(ctx.message.author.discriminator), icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="Rule 1:", value="Don't swear too much", inline=False)
        embed.add_field(name="Rule 2:", value="Be nice", inline=False)
        embed.add_field(name="Rule 3:", value="Don't be rude", inline=False)
        embed.add_field(name="Rule 4:", value="Don't be toxic", inline=False)
        embed.add_field(name="Rule 5:", value="No racism", inline=False)
        embed.add_field(name="Rule 6:", value="No sexism", inline=False)
        embed.add_field(name="Rule 7:", value="No Spamming", inline=False)
        embed.add_field(name="Rule 8:", value="Do not post links or invites in the wrong channels. (Not #💬nextcord-server-invites)", inline=False)
        embed.add_field(name="Rule 9:", value="Use the correct channels. We made them for a reason", inline=False)
        embed.set_footer(text=".report if you see someone breaking a rule")
        await ctx.message.reply(embed=embed)

def setup(client):
    client.add_cog(BasicCommands(client))

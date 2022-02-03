import disnake
from disnake.ext import commands

class Report(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Report Cog Ready")


    @commands.command(aliases=['r'])
    async def report(self, ctx):
        if ctx.message.mentions:
            ReportsChannel = self.client.get_channel(861003050901700648)
            embed=disnake.Embed(title="Report", color=0xad1f1f)
            embed.set_author(name=ctx.author.name + "#" + ctx.author.discriminator, url=ctx.message.jump_url, icon_url=ctx.author.avatar_url)
            embed.add_field(name="Reported User:", value="@" + str(ctx.message.mentions[0]), inline=True)
            embed.add_field(name="Reason for Report:", value=ctx.message.content[30:], inline=True)
            embed.set_footer(text="Thank You For Moderating!")
            await ReportsChannel.send(embed=embed)
            await ReportsChannel.send("<@&853609251602956298>")
            await ctx.message.reply("Thanks for reporting! Staff will look into it ASAP. Report Reason: " + ctx.message.content[30:] + ", User Reported: " + str(ctx.message.mentions[0]))




def setup(client):
    client.add_cog(Report(client))

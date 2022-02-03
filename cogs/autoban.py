import disnake
from disnake.ext import commands


class Autoban(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, ctx):
        member = ctx.author
        game = member.activity.name.lower()
        if (game == "genshin impact"):
            await member.timeout(self, duration=86400)
            await ctx.send(f"Wow! <@{member.id}> has been caught playing Genshin Impact! He will be recieving a 24hr timeout because of this.")
    def __init__(self, bot):
        self.bot = bot

    
  
def setup(bot):
    bot.add_cog(Autoban(bot))

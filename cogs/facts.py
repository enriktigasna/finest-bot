import disnake
from disnake.ext import commands
import asyncio
import random


class Facts(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Facts Cog Ready')

    @commands.command(aliases=['fact', 'fax', 'f'])
    async def facts(self, ctx):
        responses = ['LimeDragonBoi told me out of nowhere that he could suffocate in his girlfriends boobs out of nowhere. I thought it was funny so I told people and he started censoring it. It\'s something he doesn\'t want you to know lol',
                     'Putin is a dictator',
                     'An Alexa speaker could realistically fit in your ass',
                     'Most of these are vulgar, political or both',
                     'I am dumb',
                     'No Idea what to add',
                     'Sup guys it\'s meeeees']
        response = random.choice(responses)
        embed = disnake.Embed(title="Fun facts:")
        embed.set_author(name=ctx.author.name + "#" + ctx.author.discriminator, url=ctx.message.jump_url, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Fact:", value=f"{response}")
        embed.set_footer(text='>suggest for fact suggestions')
        await ctx.reply(embed=embed)
def setup(client):
    client.add_cog(Facts(client))

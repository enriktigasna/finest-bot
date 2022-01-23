import nextcord
from nextcord.ext import commands
import random

class _8ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("8 Ball Cog Ready")

    @commands.command(name='8ball', aliases=['8'])
    async def eightball(self, ctx, *, question):
        responses = ['as I see it, yes',
                     'Yes.',
                     'Positive',
                     'From my point of view, yes',
                     'Convinced.',
                     'Most Likley.',
                     'Chances High',
                     'No.',
                     'Negative.',
                     'Not Convinced.',
                     'Perhaps.',
                     'Not Sure',
                     'Maybe',
                     'I cannot predict now.',
                     'Im to lazy to predict.',
                     '*takes off clothes* shit in my ass',
                     'Eh..'
                     ]
        response = random.choice(responses)
        embed = nextcord.Embed(title=":8ball: It has spoken")
        embed.add_field(name='Question: ', value=f'{question}', inline=True)
        embed.add_field(name='Answer: ', value=f'{response}', inline=True)
        embed.set_footer(text=".suggest for answer suggestions.")
        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(_8ball(client))

import nextcord
from nextcord.ext import commands
import random

class KanyeQuotes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Kanye Quotes Cog Ready')

    @commands.command(aliases=['Kanyequote', 'kanyequote', 'KanyeQuote', 'KanyeQuotes', 'Kanyequotes'])
    async def kanyequotes(self, ctx):
        responses = ['Put my fist in her like a civil rights sign',
                     'I am a god',
                     'Everybody think they so woke, but they\'re following the rules of what woke is supposed to be..',
                     'Now if I fuck this model \nand she just bleach her asshole \nthen I get bleach on my T-Shirt \nThen i\'mma feel like an asshole',
                     'I treat cash like the government treats AIDS, I won\'t stop till all my n*ggas get it.',
                     'I just needed time alone with my own thoughts. \nGot treasures in my mind but couldn\'t open up my own vault. \nMy childlike creativity, purity, and honesty \nis honestly being crowded by these grown thoughts \nReality is catching up with me\nTaking my inner child, I\'m fighting for custody. \nWith these responsibilities that they entrusted me\nAs I look down on my diamond encrusted piece.',
                     'I think me and Taylor might still have sex, I made that bitch famous!',
                     'What if Mary was in the club? Before she met Joseph, with no love? Covered in lamb\'s wool. And she was \'s surrounded by the fucking wolves. We\'re surrounded by. The fucking wolves.',
                     'I have called this private meeting today. Because we have an imposter among us (2004)',
                     'Oh! I have the perfect song for the kids to play. Drug dealing just to get by..',
                     'If your stripper name "Porsche" and you get tips from many men\nThen your fat friend, her nickname is "Minivan"',
                     'If I go to prison I won\'t finish the sen-',
                     'The entire of Verse 2 of Cudi Montage. Look it up Trust me.',
                     '(Kanye Implying he was insane to support trump) I was off the meds, I was called insane\nWhat a awesome thing, engulfed in shame\nI want all the rain, I want all the pain\nI want all the smoke, I want all the blame',
                     'My greatest pain is that I will never see myself perform live.',
                     'If you learn from your mistakes then I\'m a fucking genius (Spoiler Alert: He is)',
                     'We\'re all self concious. I\'m just the first to admit it.',
                     'Name one genius that ain\'t crazy',
                     'Thank God I ain\'t too cool for the safe belt',
                     'We\'re one race, the human race. We\'re a civilization. We\'re a blipp in the universe. Yet we are still trying to pull each other down constantly..',
                     'Even if all I did failed. The fact that I did it is a success',
                     'People talk so much shit about me at barber shops, they forget to get their hair cut'
                     ]
        response = random.choice(responses)
        embed = nextcord.Embed(title="Kanye Quotes:")
        embed.set_author(name=ctx.author.name + "#" + ctx.author.discriminator, url=ctx.message.jump_url, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Kanye Quote:", value=f"{response}")
        embed.set_footer(text='.suggest for Quote suggestions')
        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(KanyeQuotes(client))

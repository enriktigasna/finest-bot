import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio
from time import sleep
import random
from random import randint, uniform


TOKEN = "ODMwODMzOTE1NTQzNTUyMDIw.YHMcYQ.dmi2t_LqE6j8sx04-lgdZyNhM-c"

client = commands.Bot(command_prefix='.')
client.remove_command('help')




@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(activity=discord.Game(name="Today we sex!"))
    


@client.command()
@has_permissions(administrator=True)
async def say(ctx, message=None):
    print(message)
    await ctx.send(f"{ctx.message.content} ".removeprefix(".say "))
    await ctx.message.delete()

@client.group(invoke_without_command=True)  
async def help(ctx):    
    embed=discord.Embed(title="Commands", color=0x17157e)
    embed.set_author(name=ctx.message.author.name + "#" + ctx.message.author.discriminator, icon_url=ctx.message.author.avatar_url)
    if ctx.message.content[5:7] == " 2":
        embed.add_field(name=".report", value="Report a user. It will be sent to the mods in a hidden channel and they will be pinged. Don't use unless someone is breaking a rule.", inline=False)
        embed.add_field(name=".rules", value="View the server rules", inline=False)
        embed.set_footer(text="Page (2/2)")
    else:
        embed.add_field(name=".avatar", value="Sends your avatar. Or the avatar of anyone mentioned or replied to.", inline=False)
        embed.add_field(name=".clear", value="Clears the amount of messages you input (Default = 1)", inline=False)
        embed.add_field(name=".help", value="Shows this page. Do .help [Page] for more help pages", inline=False)
        embed.add_field(name=".say", value="Says what you input and removes your message. (Administrator Exclusive)", inline=False)
        embed.add_field(name=".shout", value="Says what you input in a specific channel (Administrator Exclusive)", inline=False)
        embed.add_field(name=".8ball", value="Ask and you will recieve the truth.", inline=False)
        embed.set_footer(text="Page (1/2)")
    await ctx.message.reply(embed=embed)

@client.command()
async def avatar(ctx):
    if ctx.message.mentions:
        await ctx.message.reply(ctx.message.mentions[0].avatar_url)
    else:
        await ctx.message.reply(ctx.message.author.avatar_url)

@client.command()
@has_permissions(administrator=True)
async def shout(ctx, channel: discord.TextChannel):
    try:
        await channel.send(ctx.message.content[28:])
        await ctx.message.delete()
    except:
        embed=discord.Embed( color=0x17157e)
        embed.set_author(name=ctx.message.author.name + "#" + ctx.message.author.discriminator, icon_url=ctx.message.author.avatar_url)
        embed.add_field(name=".shout Usage", value=".shout \<channel\> \<input\>", inline=False)

@client.command()
async def clear(ctx, amount = 1):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send("Cleared ``" + str(amount) + "`` Messages")
    sleep(0.5)
    await ctx.channel.purge(limit=1)

@client.command()
async def report(ctx):
    print(ctx.message.content)
    if ctx.message.mentions:
        ReportsChannel = client.get_channel(861003050901700648)
        embed=discord.Embed(title="Report", color=0xad1f1f)
        embed.set_author(name=ctx.author.name + "#" + ctx.author.discriminator, url=ctx.message.jump_url, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Reported User:", value="@" + str(ctx.message.mentions[0]), inline=True)
        embed.add_field(name="Reason for Report:", value=ctx.message.content[30:], inline=True)
        embed.set_footer(text="Thank You For Moderating!")
        await ReportsChannel.send(embed=embed)
        await ReportsChannel.send("<@&853609251602956298>")
        await ctx.message.reply("Thanks for reporting! Staff will look into it ASAP. Report Reason: " + ctx.message.content[30:] + ", User Reported: " + str(ctx.message.mentions[0]))

@client.command()
async def rules(ctx):
    embed=discord.Embed(title="Rules", color=0x37e154)
    embed.set_author(name=ctx.message.author.name + "#" + str(ctx.message.author.discriminator), icon_url=ctx.message.author.avatar_url)
    embed.add_field(name="Rule 1:", value="Don't swear too much", inline=False)
    embed.add_field(name="Rule 2:", value="Be nice", inline=False)
    embed.add_field(name="Rule 3:", value="Don't be rude", inline=False)
    embed.add_field(name="Rule 4:", value="Don't be toxic", inline=False)
    embed.add_field(name="Rule 5:", value="No racism", inline=False)
    embed.add_field(name="Rule 6:", value="No sexism", inline=False)
    embed.add_field(name="Rule 7:", value="No Spamming", inline=False)
    embed.add_field(name="Rule 8:", value="Do not post links or invites in the wrong channels. (Not #💬discord-server-invites)", inline=False)
    embed.add_field(name="Rule 9:", value="Use the correct channels. We made them for a reason", inline=False)
    embed.set_footer(text=".report if you see someone breaking a rule")
    await ctx.message.reply(embed=embed)

@client.command(name='8ball')
async def eightball(ctx, *, question):
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
    embed = discord.Embed(title="It has spoken")
    embed.add_field(name='Question: ', value=f'{question}', inline=True)
    embed.add_field(name='Answer: ', value=f'{response}', inline=True)
    await ctx.reply(embed=embed)

@client.command(aliases=['fact', 'fax'])
async def facts(ctx, *question):
    responses = ['BabyFireDragon2 told me out of nowhere that he could suffocate in his girlfriends boobs out of nowhere. I thought it was funny so I told people and he started cencoring it. It\'s something he doesn\'t want you to know lol',
                 'Trans ppl are valid',
                 'Most "Libertarians" are hypocrits',
                 'Putin is a dictator',
                 'An Alexa speaker could realistically fit in your ass',
                 'Most of these are vulgar, political or both',
                 'I am dumb',
                 'No Idea what to add'
                 ]
    response = random.choice(responses)
    embed = discord.Embed(title="Fun facts:")
    embed.set_author(name=ctx.author.name + "#" + ctx.author.discriminator, url=ctx.message.jump_url, icon_url=ctx.author.avatar_url)
    embed.add_field(name='Fact: ', value=f'{response}', inline=True)
    embed.set_footer(text="DM enriktigasna#6969 for fact suggestions")
    await ctx.reply(embed=embed)


client.run(TOKEN)

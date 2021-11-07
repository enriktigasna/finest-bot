import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio
from time import sleep
import random
from random import randint, uniform
import os
import json

#CENSOR THIS WHEN SHARING CODE CENSOR THIS WHEN SHARING CODE CENSOR THIS WHEN SHARING CODE


client = commands.Bot(command_prefix='>')
client.remove_command('help')



# Cogwork
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# Ready
@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(activity=discord.Game(name="Today we sex!"))



#Run
client.run(json.load(open("config.json"))["token"])

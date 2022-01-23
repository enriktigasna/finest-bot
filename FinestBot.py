import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
import asyncio
from time import sleep
import random
from random import randint, uniform
import os
import json

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



# Test
@client.slash_command(name="ping")
async def ping(interaction):
    await interaction.response.send_message("Pong!")




# Ready
@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(activity=nextcord.Game(name="Today we sex!"))



#Run
client.run(json.load(open("config.json"))["token"])

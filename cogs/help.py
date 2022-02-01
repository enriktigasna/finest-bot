import disnake
from disnake.ext import commands
import asyncio

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Help Cog Ready')
    
    
    @commands.group(invoke_without_command=True, aliases=['h'])  
    async def help(self, ctx):    
        embed=disnake.Embed(title="Commands", color=0x17157e)
        embed.set_author(name=ctx.message.author.name + "#" + ctx.message.author.discriminator, icon_url=ctx.message.author.avatar_url)
        if ctx.message.content[5:7] == " 2":
            embed.add_field(name=".report", value="Report a user. It will be sent to the mods in a hidden channel and they will be pinged. Don't use unless someone is breaking a rule.", inline=False)
            embed.add_field(name=".rules", value="View the server rules", inline=False)
            embed.add_field(name=".shout", value="Gives you a fun fact", inline=False)
            embed.set_footer(text="Page (2/2)")
        else:
            embed.add_field(name=".avatar", value="Sends your avatar. Or the avatar of anyone mentioned or replied to.", inline=False)
            embed.add_field(name=".clear", value="Clears the amount of messages you input (Default = 1)", inline=False)
            embed.add_field(name=".help", value="Shows this page. Do .help [Page] for more help pages", inline=False)
            embed.add_field(name=".say", value="Says what you input and removes your message. (Administrator Exclusive)", inline=False)
            embed.add_field(name=".shout", value="Says what you input in a specific channel (Administrator Exclusive)", inline=False)
            embed.add_field(name=".8ball", value="Ask and you will recieve the truth.", inline=False)
            embed.add_field(name=".userinfo", value="Get the user info of someone. (UI Copied from ServerStats. Originally coded tho)", inline=False),
            embed.add_field(name=".kanyequotes", value="Get a Kanye Quote", inline=False)
            embed.set_footer(text="Page (1/2)")
        await ctx.message.reply(embed=embed)

def setup(client):
    client.add_cog(Help(client))

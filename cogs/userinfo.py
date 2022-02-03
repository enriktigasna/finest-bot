import disnake
from disnake.ext import commands

class userinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("User Info Cog Ready")

    @commands.command()
    async def userinfo(self, ctx):
        if ctx.message.mentions:
            user = ctx.message.mentions[0]
        else:
            user = ctx.message.author
        
        
        role_names = []
        for role in list(reversed(user.roles))[0:10]:
            role_names.append(role.name)
        role_names = ', '.join(role_names)

        perm_list = [perm[0] for perm in user.guild_permissions if perm[1]]
        perm_list_parsed = '\n'.join(perm_list).replace("_", " ").title()
        perm_list_parsed = "✅ " + perm_list_parsed.replace("\n", "\n✅ ")
        
        embed=disnake.Embed(title="**:busts_in_silhouette: USER INFORMATION :busts_in_silhouette:**", color=0x7289da)
        embed.add_field(name="Username", value=f"```{user}```", inline=True)
        embed.add_field(name="User ID", value=f"```{user.id}```", inline=True)
        embed.add_field(name="Roles [ "+str(len(user.roles))+" ] (shows up to 10 roles)", value=f"```{role_names}```", inline=False)
        embed.add_field(name="Nickname", value=f"```{user.display_name}```", inline=True)
        if user.bot:
            embed.add_field(name="Is a bot", value="```Yes```", inline=True)
        else:
            embed.add_field(name="Is a bot", value="```No```", inline=True)
        embed.set_thumbnail(url=user.avatar_url)
        if user.guild_permissions.administrator:
            embed.add_field(name="Global Permissions", value=f"```👑 Administrator (all permissions)```", inline=False)
        else:
            embed.add_field(name="Global Permissions", value=f"```{perm_list_parsed}```", inline=False)
        embed.add_field(name="Joined this server on (YYYY-MM-DD)", value=f"```{user.joined_at}```", inline=False)
        embed.add_field(name="Account created on (YYYY-MM-DD)", value=f"```{user.created_at}```", inline=False)
        await ctx.reply(embed=embed)


def setup(client):
    client.add_cog(userinfo(client))

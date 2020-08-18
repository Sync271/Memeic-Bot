import discord
from discord.ext import commands
import json
import datetime
from datetime import timezone
import time
class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.remove_command('help')
#Latency
    @commands.command()
    async def botinfo(self, ctx):
        dt = datetime.datetime.now()
        timestamp = (time.mktime(dt.timetuple()))
        embed=discord.Embed(title="**About**", description="Boring chat sessions are over with our new Memeic Bot! A bot dedicated to audio memes, plays in meme sounds which range from movies, anime, TV shows, vines, and more. The commands list is easy to use and ever-increasing.\nHow does it work? Type in the names of the memes as commands and the bot does your bidding. Simple (We also documented all the commands deployed by our bot so you won't get lost).\n[Add](https://discord.com/api/oauth2/authorize?client_id=721451412331954306&permissions=37223744&scope=bot) our Memeic Bot to your server now to enhance and memeify your sessions.", color=0xff5900, timestamp=datetime.datetime.utcfromtimestamp(timestamp))
        embed.set_author(name="Memeic",url="https://paypal.me/memeicbot", icon_url="https://cdn.discordapp.com/avatars/721451412331954306/6b261f077bb81c1df586b403a2f17301.png?size=256")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/721451412331954306/6b261f077bb81c1df586b403a2f17301.png?size=256")
        embed.set_image(url="https://cdn.discordapp.com/avatars/721451412331954306/6b261f077bb81c1df586b403a2f17301.png?size=256")
        embed.add_field(name="**Developers:**", value="**```Sync271#8085\nKämpfer#2790\njim carry#2042```**", inline=True)
        embed.add_field(name="**Currently Trolling:**", value=f"**```{len(self.client.guilds)} Servers\n{len(self.client.users)} Members```**", inline=True)
        embed.add_field(name="**Birthday:**", value="**```13th June 2020\nQuite a chaotic birth!```**", inline=True)
        embed.add_field(name="**Owner's Twitter:**", value="**```@sync_271```**", inline=True)
        embed.add_field(name="**Current Server:**", value=f"\n**```{ctx.guild.name}```**", inline=True)
        embed.add_field(name="**Donations:**", value="**If you enjoy the bot and want us to keep continuing, please consider donating at:```paypal.me/memeicbot or click on 'Memeic' at the top of this embeded message.```**", inline=False)
        #embed.add_field(name="Serving:", value=f"{len(self.client.users)} Members", inline=False)
        embed.set_footer(text="wubba lubba dub dub", icon_url="https://cdn.discordapp.com/avatars/721451412331954306/6b261f077bb81c1df586b403a2f17301.png?size=256")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))

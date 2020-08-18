import discord
from discord.ext import commands
import json
import datetime
from datetime import timezone
import time

class HelpEmbed(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.remove_command('help')

    @commands.command()
    async def help(self, ctx):
        dt = datetime.datetime.now()
        timestamp = (time.mktime(dt.timetuple()))
        embed=discord.Embed(title="**Help**", description="**You triggered this message by using `help`, here's a list of general commands:\n[Click Here](https://docs.google.com/spreadsheets/d/1RTofoOmS47amlPxatC3-XV6sKzWGhLjq8k2zT7GRnRA/edit?usp=sharing)**", color=0xff5900, timestamp=datetime.datetime.utcfromtimestamp(timestamp))
        embed.set_author(name="Memeic", url="https://paypal.me/memeicbot", icon_url="https://cdn.discordapp.com/avatars/721451412331954306/6b261f077bb81c1df586b403a2f17301.png?size=256")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/721451412331954306/6b261f077bb81c1df586b403a2f17301.png?size=256")
        embed.set_image(url="https://cdn.discordapp.com/avatars/721451412331954306/6b261f077bb81c1df586b403a2f17301.png?size=256")
        embed.add_field(name="**To join the voice channel you're in!:\n\n**", value="**```~join```**", inline=True)
        embed.add_field(name="**To stop the music that's currently playing : **", value="**```~stop```**", inline=True)
        embed.add_field(name="**To disconnect the bot from the voice channel :**", value="** ```~leave```**", inline=True)
        embed.add_field(name="**Gives details about the bot and it's creators :**", value="**```~botinfo```**", inline=True)
        #embed.add_field(name="**Gives a list of commands for meme songs/music :**", value="**```!commands``` **", inline=True)
        #embed.add_field(name="**Report a bug by using the following syntax :**", value="** ```!reportbug title#bug```**", inline=False)
        #embed.add_field(name="**Suggest a function/feature by using the following syntax : **", value="**```!suggest title#suggestion```**", inline=True)
        embed.add_field(name="**Donations:**", value="**If you enjoy the bot and want us to keep continuing, please consider donating at:```paypal.me/memeicbot or click on 'Memeic' at the top of this embeded message.```**", inline=False)
        embed.set_footer(text="wubba lubba dub dub", icon_url="https://cdn.discordapp.com/avatars/721451412331954306/6b261f077bb81c1df586b403a2f17301.png?size=256")
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(HelpEmbed(client))

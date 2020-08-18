import discord
from discord.ext import commands
import json
import datetime
from datetime import timezone
import time

mcommands = json.load(open("musiccommands.json"))

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.remove_command('help')

    @commands.command()
    async def commands(self, ctx):
        dt = datetime.datetime.now()
        timestamp = (time.mktime(dt.timetuple()))
        embed=discord.Embed(title="**Commands**", description="**Here's a list of commands for audio memes:\n[Click Here](https://docs.google.com/spreadsheets/d/1RTofoOmS47amlPxatC3-XV6sKzWGhLjq8k2zT7GRnRA/edit?usp=sharing)**", color=0xff5900, timestamp=datetime.datetime.utcfromtimestamp(timestamp))
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))

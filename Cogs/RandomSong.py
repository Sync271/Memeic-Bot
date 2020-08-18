import discord
import asyncio
import json
import random
from discord.ext import commands

mcommands = json.load(open("musiccommands.json"))




async def random_logic(self, ctx):
    musiclist=list(mcommands.keys())
    musiclist.remove("random")
    await ctx.send(f"~{random.choice(musiclist)}")

class MM(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def random(self, ctx):
        await random_logic(self,ctx)

    @commands.Cog.listener()
    async def on_message(self, message, self_bot = True):
        if message.author.id == 721451412331954306:
            if message.content == '~random':
                ctx = await self.client.get_context(message)
                await random_logic(self,ctx)

    @random.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()


def setup(client):
    client.add_cog(MM(client))

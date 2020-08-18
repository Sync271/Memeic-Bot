import discord
import asyncio
import json
import random
from discord.ext import commands

mcommands = json.load(open("musiccommands.json"))

class MM(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("~"):
            withoutprefix = message.content.replace("~","")
            if withoutprefix in mcommands:
                ctx = await self.client.get_context(message)
                if ctx.voice_client is None:
                    if ctx.author.voice:
                        await ctx.author.voice.channel.connect()
                    else:
                        await ctx.send("You are not connected to a voice channel.")
                        raise commands.CommandError("Author not connected to a voice channel.")
                        return
                elif ctx.voice_client.is_playing():
                    ctx.voice_client.stop()
                source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(f'./Music Files/{withoutprefix}.mp3'),volume=.2)
                ctx.voice_client.play(source)
                while ctx.voice_client.is_playing():
                    await asyncio.sleep(900)
                    await ctx.voice_client.disconnect()
                    await ctx.send("Memeic left the voice channel because of inactivity.")

    @commands.command()
    async def join(self, ctx):

        if ctx.voice_client==None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
                return
        else:
            await ctx.voice_client.disconnect()
            await ctx.author.voice.channel.connect()

    @commands.command()
    async def stop(self, ctx):
        await ctx.voice_client.stop()

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

def setup(client):
    client.add_cog(MM(client))

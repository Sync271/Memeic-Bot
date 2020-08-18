import discord
import json
from discord.ext import commands
from difflib import get_close_matches
import asyncio

mcommands = json.load(open("musiccommands.json"))
general = json.load(open("generalcommands.json"))

class CommandCorrection(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        if message.author.id == 721451412331954306:
            return
        elif message.content.startswith("~"):
                withoutprefix = message.content.replace("~","")
                if withoutprefix in mcommands:
                    return
                elif withoutprefix in general:
                    return
                elif withoutprefix != None:
                    try:
                        rightGeneral= get_close_matches(withoutprefix, general.keys())[0]
                        await message.channel.send(f"Did you mean this instead? **```~%s```**" %rightGeneral)
                    except IndexError:
                        rightCommand= get_close_matches(withoutprefix, mcommands.keys())[0]
                        await message.channel.send(f"Did you mean this instead? **```~%s```** Enter Y if yes, or N if no:" %rightCommand)
                        def check(m):
                            return m.content == "Y" or "N" and m.channel == channel
                        msg = await self.client.wait_for('message', check=check, timeout = 10.0)
                        msg.content = msg.content.lower()
                        if msg.content == "y":
                            ctx = await self.client.get_context(message)
                            if ctx.voice_client is None:
                                if message.author.voice:
                                    await message.author.voice.channel.connect()
                                    await channel.send(f'~{rightCommand}')
                                else:
                                    await channel.send("You are not connected to a voice channel.")
                            elif ctx.voice_client.is_connected():
                                ctx.voice_client.stop()
                                await channel.send(f'~{rightCommand}')
                        else:
                            return
                    except asyncio.TimeoutError:
                        await channel.send('Timeout')
                        return





def setup(client):
    client.add_cog(CommandCorrection(client))

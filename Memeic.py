import discord
import os
from discord.ext import commands
import json




client = commands.Bot(command_prefix = "~")

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'Cogs.{filename[:-3]}')





client.run('Your Access Token')

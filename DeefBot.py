import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix='!')
tables = ["(╯°□°）╯︵ ┻━┻", "┬──┬﻿ ¯\\\\_(ツ)", "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻", "┻━┻ ︵﻿ ¯\\\\(ツ)/¯ ︵ ┻━┻", "┬─┬ノ( º _ ºノ)", "(ノಠ益ಠ)ノ彡┻━┻"]

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.content == "mand":
        await client.send_message(message.channel, "MAND!")
    elif message.content == "flip":
        await client.send_message(message.channel, random.choice(tables))
    elif message.content == "unflip":
        await client.send_message(message.channel, "┬─┬ ノ( ゜-゜ノ)")

client.run('erm..... get your own token!')
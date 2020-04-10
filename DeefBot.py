import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
tables = ["(╯°□°）╯︵ ┻━┻", "┬──┬﻿ ¯\\\\_(ツ)", "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻", "┻━┻ ︵﻿ ¯\\\\(ツ)/¯ ︵ ┻━┻", "┬─┬ノ( º _ ºノ)",
          "(ノಠ益ಠ)ノ彡┻━┻"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.content == "mand":
        await message.channel.send("MAND!")
    elif message.content == "flip":
        await message.channel.send(random.choice(tables))
    elif message.content == "unflip":
        await message.channel.send("┬─┬ ノ( ゜-゜ノ)")


client.run(TOKEN)

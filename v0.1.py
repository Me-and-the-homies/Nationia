# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 00:00:13 2020

@author: keerthik
"""

import discord
import nest_asyncio
nest_asyncio.apply()
# from keys import *

client = discord.Client()

@client.event
async def on_message(message):
    if message.channel == "general" and message.content != "":
        await message.channel.purge(limit=1)


client.run('NzgzMTQ2NzYwODQzMDM0NjQ0.X8WgQQ.IHQG9eLJ13O3yTvYdIK07cF9qjk')
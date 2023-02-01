import os
from keep_alive import keep_alive
from discord.ext import commands
import discord
import random
import psutil
import asyncio
import json
import datetime
import requests
import pickle
import aiohttp
from typing import Union

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='s.', intents=intents)

bot.remove_command('help')
role_id = None
verif_text = None

@bot.event
async def on_ready():
    while True:

        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching,
                                      name=f"{len(bot.guilds)} сервер"))
        await asyncio.sleep(20)
        print(f'{bot.user} bot updated its status.')



@bot.command()
async def status(ctx):
    color = int(0xfec7da)
    embed = discord.Embed(title="Тех. часть бота:", color=color)
    usage = psutil.cpu_percent()
    opera = psutil.virtual_memory().percent
    embed.add_field(name="CPU", value=f"{usage}%")
    embed.add_field(name="RAM", value=f"{opera}%")
    embed.add_field(name="Ping", value=f"{round(bot.latency * 1000)}ms", inline=True)
  
    await ctx.send(embed=embed)
  

bot.load_extension('cog.WelcomeCog')



keep_alive()  # старт вебсерв
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)  # запуск бота

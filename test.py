import ast
import discord
import asyncio
from discord.ext import commands
import os

# command_prefix 안에는 원하는 접두사를 넣어주면 된다.
# ex) !, / ....
bot = commands.Bot(command_prefix="~")

@bot.event
async def on_ready():
    print('Loggend in Bot: ', bot.user.name)
    print('Bot id: ', bot.user.id)
    print('connection was succesful!')
    print('=' * 30)
    # 위 코드는 =라는 문자를 30개 출력하라는 뜻이다.

@bot.command()
async def Hello(ctx):
    await ctx.send("Hello world!")

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
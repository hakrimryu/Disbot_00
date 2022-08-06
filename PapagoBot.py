#This code and description is written by Hoplin
#This code is written with API version 1.0.0(Rewirte-V)
#No matter to use it as non-commercial.
#Papago API Reference : https://developers.naver.com/docs/nmt/reference/

import asyncio
import datetime
from email import message
from unicodedata import name
import discord
import os
import random
from asyncio import *
from discord.ext import commands
from urllib.error import HTTPError, URLError
from papagoRequestClass import dataProcessStream

###############################################################
#discord bot tokken
token = os.environ["BOT_TOKEN"]
#Naver Open API application ID
client_id = os.environ['CLIENT_ID']
#Naver Open API application token
client_secret = os.environ['CLIENT_SECRET']
# stream Instane
streamInstance = dataProcessStream(client_id, client_secret)
###############################################################

###############################################################
#Vote Emoji List
emojiLetters = [
    "\N{REGIONAL INDICATOR SYMBOL LETTER A}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER B}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER C}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER D}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER E}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER F}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER G}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER H}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER I}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER J}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER K}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER L}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER M}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER N}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER O}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER P}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER Q}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER R}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER S}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER T}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER U}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER V}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER W}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER X}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER Y}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER Z}"]
###############################################################

client = discord.Client()
client = commands.Bot(command_prefix="~", help_command=None)


@client.event  # Use these decorator to register an event.
async def on_ready():  # on_ready() event : when the bot has finised logging in and setting things up
    await client.change_presence(status=discord.Status.online, activity=discord.Game("~help [Command list]"))
    print("New log in as {0.user}".format(client))

# Helper method
def embed_constructor(title, description, author, footer):
    embed = discord.Embed(title=title, description=description)
    embed.set_author(name=author, icon_url=author.avatar_url)
    embed.set_footer(text=footer)
    return embed

@client.event
async def on_message(message):  # on_message() event : when the bot has recieved a message
    def sendmsg(resultPackage) -> discord.Embed:
        if resultPackage['status']["code"] < 300:
            embed = discord.Embed(
                title=f"Say {message.author.display_name}", color=0x5882FA)
            embed.add_field(name=f"{resultPackage['data']['ntl']['name']}",
                            value=resultPackage['data']['ntl']['text'], inline=True)
            embed.add_field(name=f"  ▶ {resultPackage['data']['tl']['name']}",
                            value=f"    {resultPackage['data']['tl']['text']}", inline=False)
            #embed.set_footer(text="Inquiry. ADOYO. API provided by Naver Open API")
            return embed
        else:
            embed = discord.Embed(
                title="Error Code", description=resultPackage['status']['code'], color=0x5CD1E5)
            return embed
    
    await client.process_commands(message)

    #To user who sent message
    # await message.author.send(msg)
    print(message.content)
    if message.author == client.user:
        return
    if message.content.startswith("~ke"):
        #띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("Please enter the text to be translated after the command.")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send(embed=embedInstance)
        except HTTPError as e:
            await message.channel.send(f"translation server error : {e}")

    if message.content.startswith("~ek"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("Please enter the text to be translated after the command.")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send(embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("translation server error")

    if message.content.startswith("~kj"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("Please enter the text to be translated after the command.")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send(embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("translation server error")

    if message.content.startswith("~jk"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("Please enter the text to be translated after the command..")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send(embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("translation server error")

    if message.content.startswith("~kc"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("Please enter the text to be translated after the command.")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send(embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("translation server error")

    if message.content.startswith("~ck"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("Please enter the text to be translated after the command.")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send(embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("translation server error")

    if message.content.startswith("~help"):
        embed = discord.Embed(title="Command information", color=0x8A0829,
                              description="[Translation Command : 번역 명령어]\nKorean -> English : ~ke\nEnglish -> Korean : ~ek\nKorean -> Chinese : ~kc\nChinese -> Korean : ~ck\nKorean -> Japanese : ~kj\nJapanese -> Korean : ~jk\nEnter the text to be translated after each command.\nEx)~ck 大家好\n\n[Dicegame Command : 기타 명령어]\n주사위 게임 : ~주사위\n투표 : ex) ~vote 0:0:10 \"질문\" \"내용1\" \"내용2\" ....\n\n[추후 업데이트 예정]\n1. 육의전 검색\n\n\n[BUG]\n간혹 투표 생성시 이모지가 사라지는 현상이 있습니다. \n투표 삭제후 새로 등록해 주세요.}")
        embed.set_footer(text="Inquiry. ADOYO. API provided by Naver Open API")
        await message.channel.send(embed=embed)

    #######################
    # 주사위
    #######################
    if message.content.startswith("~주사위"):
        a = random.randrange(1, 1000)
        embed = discord.Embed(title="", description="", color=0xFF0000)
        embed.add_field(name=f"{message.author.display_name}님의 주사위가 데굴데굴",
                        value=f":game_die: {str(a)}가 나왔습니다. (1-999)", inline=False)
        await message.channel.send(embed=embed)

@client.command()
async def vote(ctx, duration="0:0:0", question="질문", *answers):
    # Poll attributes
    duration = list(map(int, duration.split(":")))
    multi = False
    multiple="single"

    if multiple == "multiple":
        multi = True
    emoji_answer = {}
    voters = []
    votes = {}
    total_votes = 0
    end_datetime = datetime.datetime.now() + datetime.timedelta(hours=duration[0], minutes=duration[1], seconds=duration[2])
    description = "*투표 마감시간 "
    options = ""

    # Construct poll answers
    for i, answer in enumerate(answers):
        options += emojiLetters[i] + "     " + answer + "\n"
        emoji_answer[emojiLetters[i]] = answer

    # Construct poll description
    description += "`" + end_datetime.strftime("%b %d, %Y, %I:%M %p") + "`*\n\n" + options

    # Construct votes dictionary
    for answer in answers:
        votes[answer] = []

    # Send poll message
    message = await ctx.send(embed=
                             embed_constructor(question, description, ctx.author, "# 총 투표 수: " + str(total_votes)))

    # Display poll in console
    print(question + "\n" + description + "\n" + str(votes))

    for i, answer in enumerate(answers):
        await message.add_reaction(emojiLetters[i])

    # Ensure reaction is to the poll message and the reactor is not the bot
    def check(reaction, user):
        return reaction.message.id == message.id and user.id != 797601108268155001

    # Close the poll after a certain amount of time has elapsed
    start_time = datetime.datetime.now()
    while True:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=0.1, check=check)
            await message.remove_reaction(reaction, user)

            # Check if the user has already voted
            if multi:
                if user not in voters:
                    voters.append(user)
                if user not in votes[emoji_answer[reaction.emoji]]:
                    votes[emoji_answer[reaction.emoji]].append(user)
                    total_votes += 1
                    await message.edit(
                        embed=embed_constructor(question, description, ctx.author, "# 총 투표 수: " + str(total_votes)))

            if user not in voters:
                voters.append(user)
                votes[emoji_answer[reaction.emoji]].append(user)
                total_votes += 1
                await message.edit(
                    embed=embed_constructor(question, description, ctx.author, "# 총 투표 수: " + str(total_votes)))

            print(str(votes) + " 총 투표 수: " + str(total_votes))

        except asyncio.TimeoutError:
            if datetime.datetime.now() > start_time + datetime.timedelta(hours=duration[0], minutes=duration[1], seconds=duration[2]):
                break

    await message.delete()
    print("투표종료")

    # Send message of poll results
    results = ""
    for i, answer in enumerate(votes):
        results += emojiLetters[i] + "`" + str(len(votes[answer])) + "` | "

    description = "*투표 결과*\n\n" + options + "\n" + results

    await ctx.send(embed=embed_constructor(question, description[:-2], ctx.author, "# 총 투표 수: " + str(total_votes)))


client.run(token)

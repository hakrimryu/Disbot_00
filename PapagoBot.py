#This code and description is written by Hoplin
#This code is written with API version 1.0.0(Rewirte-V)
#No matter to use it as non-commercial.
#Papago API Reference : https://developers.naver.com/docs/nmt/reference/

import discord
import os
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
streamInstance = dataProcessStream(client_id,client_secret)
###############################################################

client = discord.Client()
@client.event # Use these decorator to register an event.
async def on_ready(): # on_ready() event : when the bot has finised logging in and setting things up
    await client.change_presence(status=discord.Status.online, activity=discord.Game("!help [translation command]"))
    print("New log in as {0.user}".format(client))

@client.event
async def on_message(message): # on_message() event : when the bot has recieved a message
    def sendmsg(resultPackage) -> discord.Embed:
        if resultPackage['status']["code"] < 300:
            embed = discord.Embed(title= f"Say {message.author.display_name}", color=0x5882FA)
            embed.add_field(name=f"{resultPackage['data']['ntl']['name']}", value=resultPackage['data']['ntl']['text'],inline=True)
            embed.add_field(name=f"  ▶ {resultPackage['data']['tl']['name']}", value=f"    {resultPackage['data']['tl']['text']}",inline=False)
            #embed.set_footer(text="Inquiry. ADOYO. API provided by Naver Open API")
            return embed
        else:
            embed = discord.Embed(title="Error Code", description=resultPackage['status']['code'],color=0x5CD1E5)
            return embed

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
        embed = discord.Embed(title="Command information", color=0x8A0829, description=
        "Korean -> English : ~ke\nEnglish -> Korean : ~ek\nKorean -> Chinese : ~kc\nChinese -> Korean : ~ck\nKorean -> Japanese : ~kj\nJapanese -> Korean : ~jk\nEnter the text to be translated after each command.\nEx)~ck 大家好")
        embed.set_footer(text="Inquiry. ADOYO. API provided by Naver Open API")

        await message.channel.send(embed=embed)

client.run(token)

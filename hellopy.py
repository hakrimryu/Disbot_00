import discord

client = discord.Client()
txt = open("discord_token.txt", 'r')
token = txt.readline()
# discord_token.txt파일을 1번째 줄만 읽고 token에 저장

@client.event
async def on_ready():
    print("ready")
    game = discord.Game('My discord bot')
    await client.change_presence(status=discord.Status.online, activity=game)
    # 봇이 준비되었다는 이벤트가 실행되면 (봇이 준비되면) My discord bot 하는 중 이라고 뜨고 온라인으로 상태를 설정합니다

client.run(token)
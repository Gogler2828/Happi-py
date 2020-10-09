from discord.ext import commands
import os
import traceback

import discord
import random
import time

#with open("token.txt") as tkn:
#    token = tkn.read()

token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print("ハッピッピくんログイン中…")
    await client.change_presence(activity = discord.Game(name = "起爆コマンド待機中...",type = 1))
#    mode = 0

@client.event
async def on_message(message):
    cnt = 0
#    if mode == 2:
#        if message.content == ("やれ"):
#            await message.channel.send("はい...")
#            time.sleep(10)
#            await message.channel.send("/happy")
#            mode = 0

    if message.content == "!bye":
#        if mode == 0:
#            await message.channel.send(f"{message.author.mention},`Error:現在スリープ状態になっているか、停止コマンドをすでに受信しています。`")
#            return
        
        await client.change_presence(activity = discord.Game(name = "緊急停止信号受信・停止中..."))
#        mode = 1
        time.sleep(60)
        await message.channel.send("お騒がせしました。")
        await client.change_presence(activity = discord.Game(name = "起爆コマンド待機中..."))
#        mode = 0
        return
    
    elif message.content.find("ハッピッピ") != -1:
        if (message.author == message.guild.owner):
            await message.channel.send(f"{message.author.mention},呼んだ？？？(OTTO)")
#            mode = 2
        else:
            await message.channel.send(f"{message.author.mention},君は僕の開発者じゃないよね:anger::anger::anger:(OTTO)\n/happi!!")

    elif message.content == "/happy":
#        if mode == 1:
#            return
        
        await message.channel.send("/list")
        await message.channel.send("/get point")
        await message.channel.send("shine")
        await message.channel.send("!member")
        await message.channel.send("OTTO")
        
        while cnt <= 5:
            cntt = 0
            if (random.randrange(0,40,4) % 3 == 0) or (random.randrange(0,40,4) % 3 == 1):
                while cntt <= 5:
                    await message.channel.send("/happy")

            else:
                while cntt <= 5:
                    await message.channel.send("!5cho")
                    await message.channel.send("!spc")
                    await message.channel.send("/happy")
                
        cnt += 1

client.run(token)
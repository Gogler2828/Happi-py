import discord
import random
import time

with open("token/happi_token.txt") as tkn:
    TOKEN = tkn.read()
    client = discord.Client()

    @client.event
    async def on_ready():
        print("ハッピッピくんログイン中…")
        await client.change_presence(activity = discord.Game(name = "起爆コマンド待機中...",type = 1))

    @client.event
    async def on_message(message):
        cnt = 0
        if message.content == "!bye":
            await client.change_presence(activity = discord.Game(name = "緊急停止信号受信・停止中..."))
            time.sleep(60)
            await message.channel.send("お騒がせしました。")
            print("送信停止解除")
            await client.change_presence(activity = discord.Game(name = "起爆コマンド待機中..."))
            return
        if message.content.find("ハッピッピ") != -1:
#                if (message.author == message.guild.owner):
                    await message.channel.send(f"{message.author.mention},呼んだ？？？")
#                else:
#                   await message.channel.send("君は僕の開発者じゃないよね？？？")
        elif message.content == "/happy":
            if (random.randrange(0,40,4) % 3 == 0) or (random.randrange(0,40,4) % 3 == 1):
                while cnt <= 5:
                    await message.channel.send("/happy")
                    cnt += 1
            else:
                await message.channel.send("!5cho")
                await message.channel.send("!spc")
                while cnt <= 5:
                    await message.channel.send("/happy")
                    cnt += 1
        
        elif message.content == ("/stop"):
            if random.randrange(100) == 28:
                await client.change_presence(activity = discord.Game(name = "緊急停止信号受信・停止中..."))
                print("送信停止中...")
                time.sleep(60)
                await message.channel.send("お騒がせしました。")
                print("送信停止解除")
                await client.change_presence(activity = discord.Game(name = "起爆コマンド待機中...",type = 1))
            else:
                while cnt <= 5:
                    await message.channel.send("/happy")
                    cnt += 1
        
    client.run(TOKEN)
import datetime
import json
import os
import sys
import traceback

import discord
import requests
from dotenv import load_dotenv

import commands
import common
import isshiijin_sv

intents = discord.Intents.all()
client = discord.Client(intents=intents)

load_dotenv()

youmu_token = os.getenv("discord_token")
error_webhook_url = os.getenv("error_webhook_url")

#エラーが起きた時のアレ
def unexpected_error():
    now = datetime.datetime.now().strftime("%H:%M") #何時か
    error_msg = f"```\n{traceback.format_exc()}```" #エラーメッセージ
    error_content = {
        "username":"error was happened",
        "content":"<@1009461769120526447>",
        "avater_url": "https://media.discordapp.net/attachments/1037548622205698090/1038346353396437073/warning.png",
        "embeds":[
            {
                "title": "エラーが発生しました!",
                "description": error_msg,
                "color": 0xff0000,
                "footer": {
                    "text": now
                }
            }
        ]
    }
    requests.post(error_webhook_url, json.dumps(error_content), headers={'Content-Type': 'application/json'})

@client.event
async def on_ready():
    try:
        login_notice_ch = client.get_channel(1038360172344639528)
        await login_notice_ch.purge(limit=1)
        await login_notice_ch.send(f"{client.user.name}はオンラインです")
        print(f"{client.user}がログインしました")
    except:
        unexpected_error()

@client.event
async def on_member_join(member):
    try:
        if member.guild.id == 1023891638399012876:
            await isshiijin_sv.on_member_join(member)

    except:
        unexpected_error()

@client.event
async def on_member_remove(member):
    try:
        if member.guild.id == 1023891638399012876:
            await isshiijin_sv.on_member_join(member)

    except:
        unexpected_error()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "$stop":
        kuma_junk = 1009461769120526447
        if not kuma_junk == message.author.id:
            await message.channel.send("実行不可能なユーザです\nKuma_junkしか実行できません\n")
            return

        await message.channel.send("実行完了")
        login_notice_ch = client.get_channel(1038360172344639528)
        await login_notice_ch.purge(limit=1)
        await login_notice_ch.send(f"{client.user.name}はオフラインです")
        now = datetime.datetime.now().strftime(r"%Y年%m月%d日　%H:%M")
        stop_msg = f"{client.user.name}が停止させられました"
        main_content = {
            "username": "bot was stopped",
            "avatar_url": "https://media.discordapp.net/attachments/1037548622205698090/1038346353396437073/warning.png",
            "content": "<@1009461769120526447>",
            "embeds": [
                {
                    "title": "botが停止させられました",
                    "description": stop_msg,
                    "color": 0xff0000,
                    "footer": {
                        "text": now
                    }
                }
            ]
        }
        requests.post(error_webhook_url, json.dumps(main_content), headers={"Content-Type": "application/json"})
        await sys.exit()
        
    try:
        try:
            if message.guild is None:
                return
            #commonコマンド
            if message.content.startswith("$ban"):
                await common.ban(message)

            if message.content.startswith("$kick"):
                await common.kick(message)

            if message.content.startswith("$delete"):
                await common.delete(message)

            if message.content == "$time":
                await common.time(message)
            #オリジナル要素コマンド
            if message.content == "$help":
                await commands.help(message)

            if message.content == "$bot invite":
                await commands.invite(message,client)

            if message.content == "$shazai":
                await commands.shazai(message)

            form_list = [
                "$report",
                "$idea",
                "$opinion",
            ]
            if message.content in form_list:
                await commands.form_link(message)

            if message.content == "$gacha":
                await commands.gacha(message)

            if message.content.startswith("$baka"):
                await commands.baka(message)

        except discord.errors.Forbidden:
            try:
                await message.channel.send("botに権限がありません\n権限を付与してください")
            except discord.errors.Forbidden:
                pass

    except:
        unexpected_error()
    
client.run(youmu_token)
import datetime
import json
import os
import sys
import traceback
import random

import discord
from discord.ext import tasks
import requests
from dotenv import load_dotenv

import common
import kuma_guild

intents = discord.Intents.all()
intents.typing = False
client = discord.Client(intents=intents)

load_dotenv()
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
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "/bot_stop":
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
        
    if message.content.startswith ("/test"):
        await message.channel.send(f"{message.author}")

    try:
        try:
            if message.guild is None:
                return

            if message.content.startswith("#") or message.content.startswith("//") or \
            (message.clean_content.startswith("/*") and message.clean_content.endswith("*/")):
                return

            if message.guild.id == 1040191003006603294:
                await kuma_guild.on_message(message,client)

        except discord.errors.Forbidden:
            try:
                await message.channel.send("botに権限がありません\n権限を付与してください")
            except discord.errors.Forbidden:
                pass

    except:
        unexpected_error()

@client.event
async def on_member_join(member):
    await common.on_member_join(client,member)

@client.event
async def on_member_remove(member):
    await common.on_member_remove(client,member)

@tasks.loop(seconds=60)
async def loop_tasks():
    try:
        await client.wait_until_ready()
        now = datetime.datetime.now()

        if now.hour == 0 and now.minute == 0:
            await kuma_guild.change_date()

        if now.hour == 9 and now.minute == 30:
            await kuma_guild.vote()

    except:
        unexpected_error
    
@tasks.loop(seconds=30)
async def change_presence():
    try:
        await client.wait_until_ready
        presence_list = [
            "https://discord.gg/v88UY7Fcyc",
            "minecraftをプレイ中",
            "man10 serverに参加中",
            "botの機能を開発中",
            "某MEE6君より優秀",
            "東方原作はいいぞ"
        ]
        presence = random.choice(presence_list)
        activity = discord.CustomActivity(presence)
        try:
            await client.change_presence(status=discord.Status.online, activity=activity)
        except ConnectionResetError:
            pass
    except:
        unexpected_error

client.run(os.getenv("discord_token"))
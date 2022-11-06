import datetime
import traceback
import requests
import random
import os
import json
import time
from dotenv import load_dotenv

import discord

import commands

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
        "content":"<@1009461769120526447>",
        "avater_url": "https://media.discordapp.net/attachments/1037548622205698090/1038346353396437073/warning.png",
        "embeds":[
            {
                "title": "エラーが発生したみょん",
                "description": error_msg,
                "color": 0xff0000,
                "footer": "unexpected_error"
            }
        ]
    }
    requests.post(error_webhook_url, json.dumps(error_content), headers={'Content-Type': 'application/json'})

@client.event
async def on_ready():
    try:
        login_notice_ch = client.get_channel(1038360172344639528)
        await login_notice_ch.send(f"{client.user.name}がログインしたみょん！")
        time.sleep(2)
        await login_notice_ch.purge(limit=1)
        print("botがログインしたみょん")
    except:
        unexpected_error()


@client.event
async def on_message(message):
        if message.content == "$gacha":
            await commands.gacha(message)

client.run(youmu_token)
import time
import json

import discord

#Google form
async def form_link(message):
    if message.content == "$opinion":
        await message.channel.send("https://forms.gle/vxCa7JamHESADDKg7")

    if message.content == "$idea":
        await message.channel.send("https://forms.gle/sgLrwrqRDHfqr3xt9")

    if message.content == "$report":
        await message.channel.send("https://forms.gle/BoAtVRGJSbQh7bgv9")

#helpコマンド用関数
async def help(message):
    help_embed = discord.Embed(title="妖夢botで使えるコマンド",color=0x00ff00)

    command_help_key =  "**$help**"
    command_help_key += "\n**$idea**"
    command_help_key += "\n**$report**"
    command_help_key += "\n**$opinion**"
    command_help_value = "**このhelpを表示します**"
    command_help_value += "\n**新しいbotの機能・コマンドを提案できます**"
    command_help_value += "\n**バグの報告ができます**"
    command_help_value += "\n**botに対しての意見が送信できます**"

    help_embed.add_field(name="全サーバー共通のコマンド",value=command_help_key,inline=True)
    help_embed.add_field(name="概要",value=command_help_value,inline=True)

    command_help = "ogwとMEE6の発言に:middle_finger:をつけます"
    command_help += "\n挨拶など日常会話に反応します"
    command_help += "\nメッセージリンクを展開します"

    help_embed.add_field(name="全サーバー共通の機能",value=command_help,inline=True)

    await message.channel.send(embed=help_embed)

async def invite(message):
    channel = message.channel
    embed = discord.Embed(title="↑妖夢bot招待url",color=0x00ff00)
    embed.set_author(name="urlはここをクリック",url="https://discord.com/api/oauth2/authorize?client_id=1038284892838039572&permissions=9465621719&scope=bot")
    await message.channel.send(embed=embed)
    time.sleep(2)
    await channel.purge(limit=1)
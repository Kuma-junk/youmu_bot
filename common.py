import datetime

import discord


async def ban(message):
    kuma_junk = 1009461769120526447
    if not kuma_junk == message.author:
        await message.channel.send("あなたには権限がありません!")

    args = message.content.split()
    user = discord.utils.get(message.guild.members, name=args[1])
    await user.ban()
    embed = discord.Embed(title="BANは正常に実行されました。",color=0xff0000)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="対象",value=user,inline=False)
    embed.add_field(name="実行者",value=message.author,inline=False)
    await message.channel.send(embed=embed)

async def kick(message):
    kuma_junk = 1009461769120526447
    if not kuma_junk == message.author:
        await message.channel.send("あなたには権限がありません!")

    args = message.content.split()
    user = discord.utils.get(message.guild.members, name=args[1])
    await kick(user=user)
    embed = discord.Embed(title="kickは正常に実行されました。",color=0xff0000)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="対象",value=user,inline=False)
    embed.add_field(name="実行者",value=message.author,inline=False)
    await message.channel.send(embed=embed)

async def time(message):
    now = datetime.datetime.now().strftime(r"%Y年%m月%d日 %H:%M")
    await message.channel.send("今は" + now + "だよ")

async def delete(message):
    channel = message.channel
    args = message.content.split()
    delete_message = args[1]
    limit = int(delete_message)
    await channel.purge(limit=limit)
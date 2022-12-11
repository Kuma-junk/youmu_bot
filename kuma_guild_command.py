import discord
import json
import time
import asyncio
import re

#認証
async def auth(message,client):
    """
    新規ロールを外してrgstedロールをつける関数"""

    new_role = message.guild.get_role(1047761021999255582)
    rgst_role = message.guild.get_role(1046300278170865715)
    if not new_role in message.author.roles:
        await message.channel.send("新規役職がついてないよ")
        return

    if not message.channel.id == 1048056229206962256:
        await message.channel.send("最初の説明読みました?\nチャンネルが違います!")
        return

    await message.channel.send("あなたが13歳(中二以上)、また一般常識があるかをテストします\n3回間違えるとやり直しです")
    time.sleep(1)
    await message.channel.send("連立方程式の問題です。次の連立方程式を解いてください。120秒でタイムアウトします\n2x+3y=-x+y=5x+y+12\n回答形式\nx=~,y=~\n")

    def check1(m):
        return m.author == message.author

    for i in range(3):
        try:
            reply = await client.wait_for("message", check=check1, timeout=120)
        except asyncio.TimeoutError:
            await message.channel.send("タイムアウトしました。/authコマンドを打つところからやり直してください。")
            return
        answer_filter = re.compile(r"(X|x)=(-|ー)2(、|,|，|| )(y|Y)=3")
        if answer_filter.fullmatch(reply.content):
            await message.channel.send(
                f"{message.author.mention}\nあなたは多分13歳以上です。第一認証を突破しました\n"
                f"次の問題にカタカナで答えてください。15秒でタイムアウトします\n"
                f"**日本の国鳥は?**"
            )
            break
        else:
            if i <= 2:
                await message.channel.send(f"{message.author.mention}\n違います。もう一度計算してください")
            else:
                await message.channel.send(
                    f"3かいまちがえました\n"
                    f"おべんきょうをがんばりましょう\n"
                    f"れんりつほうていしきがわかるようになったらもういちど/authしてください"
                )
                return

    def check2(m):
        return m.author == message.author

    for i in range(3):
        try:
            reply = await client.wait_for("message", check=check1, timeout=15)
        except asyncio.TimeoutError:
            await message.channel.send("タイムアウトしました。/authコマンドを打つところからやり直してください。")
            return
        answer_filter = re.compile(r"キジ")
        if answer_filter.fullmatch(reply.content):
            await message.author.remove_roles(new_role)
            await message.author.add_roles(rgst_role)
            await message.channel.send(
                f"{message.author.mention}\n第二認証を突破しました!\n"
                f"{message.author.name}さんようこそ{message.guild.name}へ!\n"
                f"色んな人とたくさん話そう!"
            )
            return
        else:
            if i <= 2:
                await message.channel.send(f"{message.author.mention}\n違います。もう一度考えてください")
            else:
                await message.channel.send(
                    f"3回間違えました\n"
                    f"ヒント:ももたろうに出てきます\n"
                    f"分かったらもういちど/authしてください"
                )
                return

import discord 
import json

import kuma_guild_command

async def on_message(message,client):
    if message.content == "/auth":
        await kuma_guild_command.auth(message,client)

    if message.content.startswith("メリクリ"):
        await message.channel.send("メリクリ！")

async def on_member_join(client,member):
    join_leave_notice_ch = client.get_channel(1045611804547633263)
    with open("./datas/user_data.json", mode="r", encoding="utf-8") as f:
        user_data_dict = json.load(f)

    first_join = False
    try:
        user_data = user_data_dict[f"{member.id}"]
    except KeyError:
        user_data_dict[f"{member.id}"] = {"ban": False, "role": [], "money": 0, "speak": 0, "score": 0}
        user_data_json = json.dumps(user_data_dict, indent=4)
        with open("./datas/user_data.json", mode="w", encoding="utf-8") as f:
            f.write(user_data_json)
        first_join = True

    new_role = member.guild.get_role(1047761021999255582)
    await member.add_roles(new_role)

    if not first_join:
        if not len(user_data["role"]) == 0:
            for role_id in user_data["role"]:
                role = member.guild.get_role(role_id)
                await member.add_roles(role)
                role_name = f"{role.name}, "

            await join_leave_notice_ch.send(f"{member.name}さんは過去に以下の役職を保有していたため付与しました```\n{role_name}```")

    #来た時に送るやつ
    join_embed = discord.Embed(title=f"ようこそ!{member.name}さん　{member.guild.name}へ!",color=0xffff00)
    join_embed.add_field(
        name="初めに",
        value="必ず<#1046299427377258597>をお読みください",
        inline=False
    )
    join_embed.add_field(
        name="BOTの機能",
        value="このサーバーには色んなコマンドがあります!\nいろんな機能を楽しもう!",
        inline=False
    )
    join_embed.add_field(
        name="最後に",
        value="authチャンネルで認証すると色んなチャンネルが見れるようになります\nauthチャンネルで/authコマンドの実行をお願いします",
        inline=False
    )
    await join_leave_notice_ch.send(embed=join_embed)

async def on_member_remove(client,member):
    join_leave_notice_ch = client.get_channel(1045611804547633263)
    remove_embed = discord.Embed(title=f"さようなら!{member.name}さん",color=0xffff00)
    remove_embed.add_field(
        name="また来てね",
        value="いつでも待ってるよ!",
        inline=False
    )
    await join_leave_notice_ch.send(embed=remove_embed)
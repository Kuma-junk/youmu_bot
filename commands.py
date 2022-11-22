import random
import time

import discord

#ガチャガチャ
async def gacha(message):
    gacha_inside = ["イッシー君の置き物",
                   "木彫りのKuma_junk",
                    "Yuuyuu4621のレプリカ",
                    "Yuuyuu4621の答案用紙",
                    "30万円PCレプリカ",
                    "妖夢の抱き枕カバー",
                    "ゴンおむら様の絵",
                    "intel 12700KF(ジャンク品)",
                    "カルピスウォーター",
                    "Yuuyuu4621のノートパソコン",
                    "ごみ",
                    "かす",
                    "くず"
                    ]
    gacha_result = random.choice(gacha_inside)+"が出ました!\n:tada:"
    gacha_result_embed = discord.Embed( 
                                        title="妖夢gacha V1",
                                        color=0x00ff00,
                                        description=gacha_result,
                                       )
    
    await message.channel.send(embed=gacha_result_embed)

async def baka(message):
    if message.author.id == 1039800528651157594:
        return
        
    try:
        args = message.content.split()
        baka_message = [f"{args[1]}はIQ5なのかみょん?",
                         f"{args[1]}は頭が悪いみょんね!",
                         f"{args[1]}は人をおちょくることしかできないみょんか?",
                         f"{args[1]}は万死に値するみょん!\n出ていけみょん",
                         f"{args[1]}!\nKuma_junkさんはIQ130みょんよ!",
                         "Kuma_junkさんとはぜんぜん頭の良さが違うみょんね!",
                         "不登校のKuma_junkさんに頭の良さ負けるなんてはずかしいみょんね!",
                         "メンションすんなやボケェ！！！！！！！"]

        baka_message_result = random.choice(baka_message)
        baka_message_embed = discord.Embed( 
                                            title=":middle_finger:",
                                            color=0x00ff00,
                                            description=baka_message_result,
                                           )
    
        await message.channel.send(embed=baka_message_embed)
    
    except IndexError:
        await message.channel.send("変な変数いれてんじゃねぇよ")
    

#おふざけadmin
async def admin(message):
    await message.channel.send("あなたには権限がないみょん！\n怒られたいのかみょん？\nドMだみょんね!")

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

async def invite(message,client):
    channel = message.channel
    embed = discord.Embed(title="↑妖夢bot招待url",color=0x00ff00)
    embed.set_author(name="urlはここをクリック",url="https://discord.com/api/oauth2/authorize?client_id=1038284892838039572&permissions=9465621719&scope=bot")
    await message.channel.send(embed=embed)
    time.sleep(2)
    await channel.purge(limit=1)

async def shazai(message):
    embed = discord.Embed(title="イッシー人への謝罪",
                          description=f"この度は誠に申し訳ございませんでした。\n私は勝手なことをしてしまい、イッシー人様のサーバーlogin履歴を消してしまいました。\nどんな処分も受け入れるつもりです。\n本当に申し訳ございませんでした",
                          color=00000000
                         )
    embed.set_author(name=message.author)
    embed.set_footer(f"{message.author}")
    
    await message.channel.send(embed=embed)
import random

import discord

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
    gacha_result = random.choice(gacha_inside)+"が出たみょん!\n:tada:"
    gacha_result_embed = discord.Embed( 
                                        title="妖夢gacha V1",
                                        color=0x00ff00,
                                        description=gacha_result,
                                       )
    
    await message.channel.send(embed=gacha_result_embed)

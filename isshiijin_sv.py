import discord

join_leave_notice_ch = 1023891638399012876

async def on_member_join(member):
    join_embed = discord.Embed(title=f"ようこそ!{member.guild.name}へ!",color=0xffff00)
    join_embed.add_field(name="初めに",value="必ず<#1022450233076092948>をお読みください")
    join_embed.add_field(name="bot",value="このサーバーにはいろんなbotがいます\nいろんな機能を楽しもう!")
    join_embed.add_field(name="最後に",value="$helpと打ってみてね")
    await join_leave_notice_ch.send(embed=join_embed)
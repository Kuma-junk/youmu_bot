import discord

import kuma_guild

join_leave_notice_ch = 1045611804547633263

async def on_member_join(client,member):
    if member.guild.id == 1040191003006603294:
        await kuma_guild.on_member_join(client,member)

async def on_member_remove(client,member):
    if member.guild.id == 1040191003006603294:
        await kuma_guild.on_member_remove(client,member)

#Google form
async def form_link(message):
    if message.content == "$opinion":
        await message.channel.send("https://forms.gle/vxCa7JamHESADDKg7")

    if message.content == "$idea":
        await message.channel.send("https://forms.gle/sgLrwrqRDHfqr3xt9")

    if message.content == "$report":
        await message.channel.send("https://forms.gle/BoAtVRGJSbQh7bgv9")
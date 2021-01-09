import discord

client = discord.Client()


token = '★봇토큰★'
channel = '★디엠 내용 보내질 채널ID★'


@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('★~하는중에 표시될 네임 작성★')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.guild is None:
        if message.author.bot:
            return
        else:
            embed = discord.Embed(colour=discord.Colour.blue(), timestamp=message.created_at)
            embed.add_field(name='전송자', value=message.author, inline=False)
            embed.add_field(name='내용', value=message.content, inline=False)
            embed.set_footer(text=f'!디엠 <@{message.author.id}> [할말] 을 통해 답장을 보내주세요!')
            await client.get_channel(channel).send(f"`{message.author.name}({message.author.id})`", embed=embed)

    if message.content.startswith('!디엠'):
        msg = message.content[25:]
        await message.mentions[0].send(f"**{message.author.name}** 님의 답장: {msg}")
        await message.channel.send(f'`{message.mentions[0]}`에게 DM을 보냈습니다')
        
client.run(token)

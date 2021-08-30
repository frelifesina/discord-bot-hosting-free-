import discord 
import asyncio

client = discord.Client()

@client.event
async def on_rady():
    print(client.user.id)
    print("Hello python!")
    game = discord.Game("I Am AI.. you know my mind..? I")
    await client.change_presence(status=discord.status.online, activity=game)
@client.event
async def on_message(message):
    if message.content.startswith("/소개"):
        await message.channel.send("안녕하세요 저는 디스코드봇 AI라고 합니다 이렇게 쉬운걸 만드느라 10분이나 걸렸지만 잘 부탁드려요")
    if message.content.startswith("/버전"):
        await message.channel.send("나의 버전은 0.1입니다 앞으로 꾸준히 업그레이드 예정입니다")

    if message.content.startswith("/최초의 임베드"):
        embed = discord.Embed(title="타이틀", description="디스크립션", color = 0x00ff00)
        embed.add_field(name="임베드 이름", value="변수")
        
        embed.set_footer(text="텍스트")
        await message.channel.send(embed=embed)

    if message.content.startswith("/DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await message.author.send(msg)
    if message.content.startswith("/너의??"):
        await message.channel.send("이름은")

client.run("ODgxMzY0NTE3OTE1ODc3Mzk4.YSrwrA.Y0W2m5rHkqr1mr9PlpyUWBSBKR8")


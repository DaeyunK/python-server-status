import discord
from discord.ext import commands

app = commands.Bot(command_prefix="?", help_command=None)
ch = app.get_channel(채널아이디)

@app.event
async def on_ready():
    game = discord.Game('서술')
    await app.change_presence(status=discord.Status.idle, activity=game)

@app.command()
@commands.has_permissions(administrator=True)
async def 서버온(ctx):
    embed = discord.Embed(title="``🟢``  **서버 상태**", description="서버 상태가 **ON** 으로 변경 되었습니다. \n\n 서버 주소 : OOO.com", color=0xFF0000)
    await ch.send(embed=embed)

@app.command()
@commands.has_permissions(administrator=True)
async def 서버오프(ctx):
    embed = discord.Embed(title="``🔴``  **서버 상태**", description="서버 상태가 **OFF** 으로 변경 되었습니다.", color=0x00FF00)
    await ch.send(embed=embed)

@app.command()
@commands.has_permissions(administrator=True)
async def 서버점검(ctx, amount):
    embed = discord.Embed(title="``🟡``  **서버 상태**", description="서버 상태가 **점검 중** 으로 변경 되었습니다. \n\n 예상 점검 시간 {} 분".format(amount), color=0xFFFF00)
    await ch.send(embed=embed)

app.run("TOKEN")
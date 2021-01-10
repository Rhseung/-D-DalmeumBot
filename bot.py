import discord
from discord.ext import commands
 
app = commands.Bot(command_prefix='`')
 
@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def repeat(ctx, *, text):
  await ctx.send(text)
     
app.run('NDgyMTAwMjczODQyNjE4Mzc4.W35s3g.7Y839hANecV3yxxmDAPTfrQx5Uw')
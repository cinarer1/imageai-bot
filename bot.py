import discord
from discord.ext import commands
import teachable  # Bu senin özel modülünse sorun yok

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh: int = 5):
    await ctx.send("he" * count_heh)

    
    
    
    
    
    

bot.run("MTM2MjQ3ODc2NjIyNzcxODQ1Ng.Gk0drw.-kb78cbGU1k5mOUTM4ByO6rtOLZVNtesWUyCUI")
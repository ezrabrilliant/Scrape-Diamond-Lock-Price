import discord
from discord.ext import commands
from graph import generate_graph
from candle import generate_candle
import os
from dotenv import load_dotenv

load_dotenv()
dc_token = os.getenv("dc")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} is online')

@bot.command()
async def hargadl(ctx):
    generate_graph()

    with open('hargadl.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def candle(ctx, timeframe: str):
    if not timeframe:
        await ctx.reply("Please provide a timeframe")
        return

    generate_candle(timeframe)

    with open('candle.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

bot.run(dc_token)

import discord
from discord.ext import commands
import pymongo
import re
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
mongodb_connection_string = os.getenv("mongo-uri")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.remove_command('help')

db = pymongo.MongoClient(mongodb_connection_string)
hargadl = db['hargadl']
rate = hargadl['rate']

def save_data_to_db(prices, times):
    for price, time in zip(prices, times):
        rate.insert_one({"price": price, "time": time})

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.channel.id == 1083704905035952210:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if "BUY" in message.content:
            numbers = re.findall(r'\d+\.\d+', message.content)
            if numbers:
                float_numbers = [float(num) for num in numbers]
                min_number = min(float_numbers)
                if min_number <= 10:
                    min_price_str = f'{min_number:.3f}'.replace('.', '')
                    prices = {min_price_str}  
                    
                    times = [now] * len(prices)
                    save_data_to_db(prices, times)

    await bot.process_commands(message)

bot.run()

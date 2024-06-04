import matplotlib.pyplot as plt
import pymongo
import time
from datetime import datetime
import discord
from discord.ext import commands
import nest_asyncio
import pandas as pd
import mplfinance as mpf

db = pymongo.MongoClient('mongodb+srv://botfandy:fandy1309@db.1jgy0x3.mongodb.net/')
hargadl = db['hargadl']
rate = hargadl['rate']

def read_data_from_db():
    start_time = time.time()
    prices = []
    times = []
    message_links = []
    for record in rate.find():
        prices.append(float(record["price"]))  # Convert price to float
        times.append(record["time"])
        message_links.append(record["message_link"])
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Speed Read Data", elapsed_time)
    return prices, times, message_links


def generate_graph():
    prices, times, _ = read_data_from_db()

    # Konversi waktu ke format datetime
    datetime_objects = [datetime.strptime(time, '%Y-%m-%d %H:%M:%S') for time in times]

    # Membuat dictionary untuk menyimpan harga rata-rata per jam
    hourly_avg_prices = {}
    for price, datetime_obj in zip(prices, datetime_objects):
        hour_key = datetime_obj.replace(minute=0, second=0)  # Setel menit dan detik ke 0 untuk mengelompokkan per jam
        if hour_key not in hourly_avg_prices:
            hourly_avg_prices[hour_key] = [price]
        else:
            hourly_avg_prices[hour_key].append(price)

    # Menghitung rata-rata per jam
    hourly_avg_prices = {hour: sum(prices) / len(prices) for hour, prices in hourly_avg_prices.items()}

    # Memisahkan waktu dan harga rata-rata untuk plotting
    hours = list(hourly_avg_prices.keys())
    avg_prices = list(hourly_avg_prices.values())

    # Mengatur warna latar belakang grafik menjadi hitam
    plt.rcParams['axes.facecolor'] = '#181a20'
    plt.rcParams['figure.facecolor'] = '#0e1015'
    plt.rcParams['text.color'] = 'white'
    plt.rcParams['axes.labelcolor'] = 'white'
    plt.rcParams['xtick.color'] = 'white'
    plt.rcParams['ytick.color'] = 'white'

    # Membuat grafik dengan garis berwarna hijau
    plt.plot(hours, avg_prices, color='green')


    # Mengisi area di bawah garis grafik dengan warna
    plt.fill_between(hours, avg_prices, min(avg_prices)-(min(avg_prices)*0.005), color='lightgreen', alpha=0.4)

    plt.xlabel('Time')
    plt.ylabel('Average Price')
    plt.title('Hourly Average Price')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('candledl.png')

generate_graph()


def generate_candle():
    prices, times, _ = read_data_from_db()

    # Convert time to datetime format
    datetime_objects = [datetime.strptime(time, '%Y-%m-%d %H:%M:%S') for time in times]

    # Create a DataFrame from the data
    df = pd.DataFrame({'Price': prices}, index=datetime_objects)

    # Resample the data to 1 hour intervals and calculate OHLC
    df = df.resample('4h').ohlc()

    # Flatten the column names
    df.columns = ['_'.join(col).strip() for col in df.columns.values]

    # Rename the columns to match mplfinance expectations
    df = df.rename(columns={"Price_open": "Open", "Price_high": "High", "Price_low": "Low", "Price_close": "Close"})

    mpf.plot(df, type='candle', style='yahoo', savefig='candle.png')
generate_candle()

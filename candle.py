import pandas as pd
import mplfinance as mpf
from database import read_data_from_db
from datetime import datetime

def generate_candle(timeframe):
    prices, times, _ = read_data_from_db()

    datetime_objects = [datetime.strptime(time, '%Y-%m-%d %H:%M:%S') for time in times]

    df = pd.DataFrame({'Price': prices}, index=datetime_objects)

    timeframes = timeframe.lower()
    timeframes = timeframe.replace(" ", "")
    df = df.resample(timeframes).ohlc()

    df.columns = ['_'.join(col).strip() for col in df.columns.values]

    df = df.rename(columns={"Price_open": "Open", "Price_high": "High", "Price_low": "Low", "Price_close": "Close"})

    mpf.plot(df, type='candle', style='yahoo',mav=(2,4,6),figratio=(11,8),figscale=0.85, savefig='candle.png')

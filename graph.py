import matplotlib.pyplot as plt
from datetime import datetime
from database import read_data_from_db

def generate_graph():
    prices, times, _ = read_data_from_db()

    datetime_objects = [datetime.strptime(time, '%Y-%m-%d %H:%M:%S') for time in times]

    hourly_avg_prices = {}
    for price, datetime_obj in zip(prices, datetime_objects):
        hour_key = datetime_obj.replace(minute=0, second=0)
        if hour_key not in hourly_avg_prices:
            hourly_avg_prices[hour_key] = [price]
        else:
            hourly_avg_prices[hour_key].append(price)

    hourly_avg_prices = {hour: sum(prices) / len(prices) for hour, prices in hourly_avg_prices.items()}

    hours = list(hourly_avg_prices.keys())
    avg_prices = list(hourly_avg_prices.values())

    plt.rcParams['axes.facecolor'] = '#181a20'
    plt.rcParams['figure.facecolor'] = '#0e1015'
    plt.rcParams['text.color'] = 'white'
    plt.rcParams['axes.labelcolor'] = 'white'
    plt.rcParams['xtick.color'] = 'white'
    plt.rcParams['ytick.color'] = 'white'

    plt.plot(hours, avg_prices, color='green')

    plt.fill_between(hours, avg_prices, min(avg_prices)-(min(avg_prices)*0.005), color='lightgreen', alpha=0.4)

    plt.xlabel('Time')
    plt.ylabel('Average Price')
    plt.title('Hourly Average Price')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('hargadl.png')

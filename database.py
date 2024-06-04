import pymongo
import time
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

mongodb_connection_string = os.getenv("mongo-uri")

db = pymongo.MongoClient(mongodb_connection_string)
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

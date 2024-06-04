# collect-price-dl
collect Diamond Lock price data from [GTID server](https://discord.gg/gtid)


## Usage (generate price data)
1. Install the requirements by running `pip install -r requirements.txt`
2. create a `.env` file in the root directory and fill it with the following content:
```env
DISCORD_TOKEN=your_discord_bot_token
mongo-uri=your_mongo_uri
```
3. Run the script by running `python main.py`
4. If the command `!hargadl` on discord has been called, the script will generate a file named `hargadl.png` which containing the price data of Diamond Locks.
5. If the command `!candle (timeframe)` on discord has been called, the script will produce a file called `candle.png` which contains Diamond Locks price data along with the corresponding timeframe from the user input.

## Usage (scrape price data)
1. Run the script by running `python scrape_data.py`
2. The script will scrape the price data of Diamond Locks from the GTID server and store it in the MongoDB database.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements
- [GTID server](https://discord.gg/gtid)
- [discord.py](https://discordpy.readthedocs.io/)
- [pandas](https://pandas.pydata.org/)
- [mplfinance](https://github.com/matplotlib/mplfinance)
- [pymongo](https://pymongo.readthedocs.io/en/stable/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://docs.python-requests.org/en/master/)
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [matplotlib](https://matplotlib.org/)


import time
import json

import scrapers.scrape_coingecko
import scrapers.scrape_coinlib
from filters.crypto_filter import filter_coins

if __name__ == "__main__":

    required_coins = ['BTC', 'ETH', 'ADA', 'DOT']

    while True:
        try:
            coins = scrapers.scrape_coingecko.get_data()

            if not coins:
                coins = scrapers.scrape_coinlib.get_data() 

            filtered_coins = filter_coins(coins, required_coins)

            json_object = json.dumps(filtered_coins, indent = 4) 
            print(json_object)

            # TODO: push data to DB
            time.sleep(10)
        except:
            raise TypeError

import time

import scrapers.scrape_coingecko
import scrapers.scrape_coinlib
from filters.crypto_filter import filter_coins

if __name__ == "__main__":

    required_coins = ['BTC', 'ETH', 'ADA', 'DOT']

    while True:
        coins = scrapers.scrape_coingecko.get_data()

        if coins is None:
            coins = scrapers.scrape_coinlib.get_data()

        data = filter_coins(coins, required_coins)
        print(data)

    # TODO: push data to DB
        time.sleep(10)


    
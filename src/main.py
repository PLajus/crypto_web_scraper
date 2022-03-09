import time

import scrapers.scrape_coingecko
import scrapers.scrape_coinlib

if __name__ == "__main__":

    while True:
        data = scrapers.scrape_coingecko.get_data()

        if data is None:
            data = scrapers.scrape_coinlib.get_data()

        time.sleep(10)

    # TODO: push data to DB
    
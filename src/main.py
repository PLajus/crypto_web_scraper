import scrapers.scrape_coingecko
import scrapers.scrape_coinlib

if __name__ == "__main__":
    coingecko_data = scrapers.scrape_coingecko.get_data()
    scrapers.scrape_coinlib.get_data()
    
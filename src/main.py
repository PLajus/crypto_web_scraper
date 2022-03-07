import scrapers.scrape_coingecko

if __name__ == "__main__":
    coingecko_data = scrapers.scrape_coingecko.get_data()

    print(coingecko_data)
    
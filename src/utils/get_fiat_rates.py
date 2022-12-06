import scrapers.scrape_fiat

def get_rates():

    fiat = scrapers.scrape_fiat.get_data()

    fiat = {"Fiat": fiat}

    return fiat
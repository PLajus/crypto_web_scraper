from bs4 import BeautifulSoup
import requests

def get_data():
    """Scrapes crypto name, symbol and price from CoinGecko"""

    data = []

    source = requests.get("https://www.coingecko.com/")

    soup = BeautifulSoup(source.content, 'lxml')

    table = soup.find('tbody')

    for row in table.find_all('tr', limit=3):
        try:
            name = row.find('a', class_='tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between').text.strip()
            symbol = row.find('a', class_='d-lg-none font-bold tw-w-12').text.strip()
            price_usdt = row.find('span', class_='no-wrap').text.strip()
            change_24 = row.find('span', {"data-24h" : "true"}).text.strip()

        except AttributeError:
            pass

        data.append((name, symbol, price_usdt, change_24))

        return data
import unittest
from scrapers.scrape_coingecko import get_data

class TestCoinGeckoScraper(unittest.TestCase):

    def test_data_not_empty(self):
        data = get_data()
        self.assertTrue(data)

    def test_coin_data_amount(self):
        data = get_data()
        self.assertEqual(50, len(data))

    def test_numof_data_values(self):
        data = get_data()
        self.assertEqual(4, len(data[0]))

if __name__ == '__main__':
    unittest.main()

import unittest
from scrapers.scrape_coingecko import scrape_coingecko

class TestScraper(unittest.TestCase):

    def test_data_not_empty(self):
        data = get_data()
        self.assertTrue(data)

    def test_datavalues(self):
        data = get_data()
        self.assertEqual(4, data.length())

if __name__ == '__main__':
    unittest.main()

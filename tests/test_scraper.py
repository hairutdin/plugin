import unittest
from chatbot.scraper import SahibindenScraper

class TestSahibindenScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = SahibindenScraper()

    def test_search(self):
        # Test that the search method returns the expected results
        # This will depend on the structure of the Sahibinden.com website
        data = self.scraper.search("istanbul/rent")
        self.assertIsInstance(data, list)
        for item in data:
            self.assertIsInstance(item, dict)
            self.assertIn('name', item)
            self.assertIn('price', item)
            self.assertIn('link', item)

    def test_extract_data(self):
        # Test that the _extract_data method returns the expected results
        # This will depend on the structure of the Sahibinden.com website
        pass

if __name__ == "__main__":
    unittest.main()

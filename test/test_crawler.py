import unittest

from crawler.crawler import Crawler

class CrawlerTestCase(unittest.TestCase):

    def setUp(self):
        self.crawler = Crawler()

    def test_scrape(self):
        flag = self.crawler.scrape('手機')

        self.assertTrue(flag)

    def test_scrape_return_none(self):
        flag = self.crawler.scrape()

        self.assertFalse(flag)

if __name__ == '__main__':
    unittest.main()

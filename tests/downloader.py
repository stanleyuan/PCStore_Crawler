import unittest
import requests

from unittest import mock

from crawler.downloader import Downloader

class DownloaderTestCase(unittest.TestCase):

    def setUp(self):
        self.downloader = Downloader()
        self.keyword = '手機'
        self.response = self.downloader.request(self.keyword)

    def test_request(self):

        self.assertEqual(200, self.response.status_code)

    def test_get_response_text(self):
        html = self.downloader.get_response_text(self.response)

        self.assertTrue(html)

    def test_get_text_from_keyword(self):
        html = get_text_from_keyword(self.keyword)

        self.assertTrue(html)


if __name__ == '__main__':
    unittest.main()

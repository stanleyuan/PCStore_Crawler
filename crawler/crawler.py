""" This module is the controller of crawler """
from typing import Optional

from crawler.downloader import Downloader
from crawler.parser import Parser


class Crawler:
    """Crawler"""

    def __init__(self) -> None:
        self.downloader = Downloader()
        self.parser = Parser()

    def scrape(self, keyword: Optional[str] = None) -> bool:
        """scrape

        Summary:
                summary

        Args:
            keyword: Optional[str]

        Returns:
                {variable}: bool

        Raises:

        """
        if keyword:
            html = self.downloader.get_text_from_keyword(keyword)
            if html:
                self.parser.print_result_from_parser(html)
                return True
        return False

    def change_url(self):
        """change_url"""


if __name__ == "__main__":
    CRAWLER = Crawler()
    FLAG = CRAWLER.scrape()
    print(FLAG)
    FLAG = CRAWLER.scrape("手機")
    print(FLAG)

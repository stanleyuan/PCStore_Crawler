from downloader import Downloader
from parser import Parser

class Crawler:

    def __init__(self):
        self.downloader = Downloader()
        self.parser = Parser()

    def scrape(self, keyword=None):
        if keyword:
            html = self.downloader.get_text_from_keyword(keyword)
            if html:
                self.parser.print_result_from_parser(html)
                return True
        return False

if __name__ == '__main__':
    crawler = Crawler()
    flag = crawler.scrape()
    print(flag)
    flag = crawler.scrape('手機')
    print(flag)

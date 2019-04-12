import os
from bs4 import BeautifulSoup as bs

FILE_PATH = os.path.dirname(os.path.realpath(__file__))

class Parser:

    def __init__(self):
        pass

    def parser_titles(self, html):
        titles = list()
        soup = bs(html, 'html.parser')
        results = soup.findAll("div", {"id": "keyad-pro-right3"})
        for result in results:
            title = result.find("div", {"class": "pic2t"}).find('a').text
            titles.append(title)

        return titles

    def print_result(self, titles):
        if len(titles) != 0:
            for index, title in enumerate(titles):
                print("{}: {}".format(str(index+1), title))
            return 1

        print("沒有結果")
        return 0

    def print_result_from_parser(self, html):
        titles = self.parser_titles(html)
        return self.print_result(titles)

if __name__ == '__main__':

    with open(FILE_PATH+'/target_web.html', 'r') as file:
        html = file.read()
    parser = Parser()
    titles = parser.parser_titles(html)
    parser.print_result(titles)
    parser.print_result_from_parser(html)

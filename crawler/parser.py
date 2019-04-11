import os
from bs4 import BeautifulSoup as bs

CURRENT_PATH = os.getcwd()

class Parser:

    def __init__(self):
        pass

    def parser(self, html):
        soup = bs(html, 'html.parser')
        results = soup.findAll("div", {"id": "keyad-pro-right3"})
        self.titles = list()
        for result in results:
            title = result.find("div", {"class": "pic2t"}).find('a').text
            self.titles.append(title)

    def print_result(self):
        for index, title in enumerate(self.titles):
            print("{}: {}".format(str(index+1), title))

if __name__ == '__main__':

    with open(CURRENT_PATH+'/target_web.html', 'r') as file:
        html = file.read()
    parser = Parser()
    parser.parser(html)
    parser.print_result()

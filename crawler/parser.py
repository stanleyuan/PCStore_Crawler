""" This module contains functions to parser html """
import os
from typing import List

from bs4 import BeautifulSoup as bs


FILE_PATH = os.path.dirname(os.path.realpath(__file__))


class Parser:
    """Parser"""
    def __init__(self) -> None:
        self.titles = list()

    def parser_titles(self, html: str) -> List[str]:
        """parser_titles

        Summary:
                summary

        Args:
            html: str

        Returns:
                {variable}: List[str]

        Raises:

        """
        self.titles = list()
        soup = bs(html, "html.parser")
        results = soup.findAll("div", {"id": "keyad-pro-right3"})
        for result in results:
            title = result.find("div", {"class": "pic2t"}).find("a").text
            self.titles.append(title)

        return self.titles

    def print_result(self, titles: List[str]) -> int:
        """print_result

        Summary:
                summary

        Args:
            titles: List[str]

        Returns:
                {variable}: int

        Raises:

        """
        if isinstance(titles, list):
            self.titles = titles
            for index, title in enumerate(titles):
                print("{}: {}".format(str(index + 1), title))
            return 1

        print("沒有結果")
        return 0

    def print_result_from_parser(self, html: str) -> int:
        """print_result_from_parser

        Summary:
                summary

        Args:
            html: str

        Returns:
                {variable}: int

        Raises:

        """
        titles = self.parser_titles(html)
        return self.print_result(titles)


if __name__ == "__main__":

    with open(FILE_PATH + "/target_web.html", "r") as file:
        HTML = file.read()
    PARSER = Parser()
    TITLES = PARSER.parser_titles(HTML)
    PARSER.print_result(TITLES)
    PARSER.print_result_from_parser(HTML)

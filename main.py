""" This files is the entry point for crawler"""
import argparse

from crawler.crawler import Crawler


def main():
    """main

    Crawling from the keyword

    """
    flag = False
    crawler = Crawler()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-k", "--keyword", help="keyword to search", default="templates/ssh.j2"
    )
    args = parser.parse_args()
    flag = crawler.scrape(args.keyword)

    return flag


if __name__ == '__main__':
    main()

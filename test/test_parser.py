import os
import unittest

from crawler.parser import Parser

FILE_PATH = os.path.dirname(os.path.realpath(__file__))

class ParserTestCase(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()
        with open(FILE_PATH+'/test.html', 'r') as file:
            self.html = file.read()
        self.titles = self.parser.parser_titles(self.html)

    def tearDown(self):
        pass

    def test_parser_titles(self):

        self.assertEqual(20, len(self.titles))

    def test_print_result(self):
        flag = self.parser.print_result(self.titles)

        self.assertTrue(flag)

    def test_print_result_from_parser(self):
        flag = self.parser.print_result_from_parser(self.html)

        self.assertTrue(flag)


if __name__ == '__main__':
    unittest.main()

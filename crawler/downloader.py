""" This modules contains class to request and get response """
import requests
from requests.models import Response


class Downloader:
    """Downloader

    Contains funciton:
        request
        get_response_text
        get_text_from_keyword

    """

    def __init__(self) -> None:
        self.url = "https://www.pcstore.com.tw/adm/psearch.htm"
        self.html = None

    def request(self, keyword: str) -> Response:
        """request

        Summary:
            Gets response from certain url by search keyword

        Args:
            keyword: str

        Returns:
            response: Response

        Raises:

        """
        response = None

        if response or keyword:
            keyword = keyword.encode("big5-hkscs")
            headers = {
                "authority": "www.pcstore.com.tw",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/73.0.3683.75 Safari/537.36",
                "content-type": "application/x-www-form-urlencoded",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                "origin": "https://www.pcstore.com.tw",
            }

            data = {
                "type_code": "",
                "send_keyword": "",
                "slt_k_option": 1,
                "store_k_word": keyword,
                "store_k_word2": keyword,
                "slt_p_range_s": "",
                "slt_p_range_e": "",
                "slt_k_option3": 1,
                "store_k_word3": keyword,
                "page_count": 20,
            }

            response = requests.post(self.url, headers=headers, data=data)
            response.encoding = "big5-hkscs"

        return response

    def get_response_text(self, response: Response) -> str:
        """get_response_text

        Summary:
            Gets text from a http response

        Args:
            response: Response

        Returns:
            self.html: str

        Raises:

        """
        self.html = None

        if response:
            self.html = response.text

        return self.html

    def get_text_from_keyword(self, keyword: str) -> str:
        """get_text_from_keyword

        Summary:
            Gets text by certain keyword

        Args:
            keyword: str

        Returns:
            self.html: str

        Raises:

        """
        self.html = None
        response = self.request(keyword)
        if response:
            self.html = self.get_response_text(response)

        return self.html


if __name__ == "__main__":
    DOWNLOADER = Downloader()
    RESULT = DOWNLOADER.request("手機")
    TEXT = DOWNLOADER.get_response_text(RESULT)
    print(TEXT)
    TEXT = DOWNLOADER.get_text_from_keyword("電腦")
    print(TEXT)

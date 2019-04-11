import requests

class Downloader:

    def __init__(self):
        self.url = "https://www.pcstore.com.tw/adm/psearch.htm"

    def request(self, keyword):
        response = None

        if response:
            headers = {
                'authority': 'www.pcstore.com.tw',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
                'content-type': 'application/x-www-form-urlencoded',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                'origin': 'https://www.pcstore.com.tw'
                }

            data = {
                'type_code': '',
                'send_keyword': '',
                'slt_k_option': 1,
                'store_k_word': keyword,
                'store_k_word2': keyword,
                'slt_p_range_s': '',
                'slt_p_range_e': '',
                'slt_k_option3': 1,
                'store_k_word3': keyword,
                'page_count': 20,
            }

            response = requests.post(self.url, headers=headers, data=data)
            response.encoding = 'big5-hkscs'

        return response

    def get_response_text(self, response):
        html = None

        if response:
            html = response.text

        return html


if __name__ == '__main__':
    downloader = Downloader()
    response = downloader.request('手機'.encode('big5-hkscs'))
    html = downloader.get_response_text()

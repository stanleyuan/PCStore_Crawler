# PCSTORE CRAWLER

## Summary

[PChome](https://www.pcstore.com.tw/)  的爬蟲，能夠有個function輸入關鍵字搜索，並且回傳一頁的標題

## Development
- virtualenv
```bash
pipenv sync
pipenv shell
```
- test
```bash
python -m unittest
```

- requirements
```bash
pip install -r requirements.txt
```
## Run
```bash
python main.py -k[--keyword] '手機'
```

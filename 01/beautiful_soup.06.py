from bs4 import BeautifulSoup as soup

import urllib.request as request

url = "http://info.finance.naver.com/marketindex"
res = request.urlopen(url)

content = soup(res, "html.parser")

price = content.select_one("div.head_info > span.value").string
print("usd/krw = ", price)

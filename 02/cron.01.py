from bs4 import BeautifulSoup as soup

import urllib.request as request
import datetime

url = "http://info.finance.naver.com/marketindex"
res = request.urlopen(url)

content = soup(res, "html.parser")

price = content.select_one("div.head_info > span.value").string
print("usd/krw = ", price)

today = datetime.date.today()
filename = today.strftime("%Y-%m-%d") + ".txt"

with open(filename, "w", encoding="utf-8") as fp:
    fp.write(price)

# PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/bin/python3
# PYTHONIOENCODING='utf-8'

# 0 7 * * * ~/Documents/projects/ml/practice/02/cron.01.py

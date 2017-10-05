from bs4 import BeautifulSoup as soup

import urllib.request as request

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
res = request.urlopen(url)

content = soup(res, "html.parser")

title = content.find("title").string
wf = content.find("wf").string

print(title)
print(wf)

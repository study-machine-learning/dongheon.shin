from bs4 import BeautifulSoup as soup

import urllib.request as request

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = request.urlopen(url)

content = soup(res, "html.parser")

a_list = content.select("#mw-content-text ul li a")

for a in a_list:
    name = a.string
    print("- ", name)

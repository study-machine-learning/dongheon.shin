from bs4 import BeautifulSoup as soup

import urllib.request as request
import os.path

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
filename = "data.forecast.xml"

if not os.path.exists(filename):
    request.urlretrieve(url, filename)

xml = open(filename, "r", encoding="utf-8").read()
content = soup(xml, "html.parser")

info = {}

for location in content.find_all("location"):

    name = location.find("city").string
    weather = location.find("wf").string

    if not (weather in info):
        info[weather] = []

    info[weather].append(name)

for weather in info.keys():

    print("+ ", weather)

    for name in info[weather]:
        print("| ", name)

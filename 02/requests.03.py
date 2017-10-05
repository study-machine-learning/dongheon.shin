import requests

res = requests.get("http://wikibook.co.kr/wikibook.png")

with open("test.png", "wb") as fp:
    fp.write(res.content)

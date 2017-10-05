import sys
import urllib.request as request
import urllib.parse as parse

if len(sys.argv) <= 1:
    print("usage : python3 urllib.05.py <region number>")
    sys.exit()

region = sys.argv[1]

endpoint = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
params = parse.urlencode({
    "stn": region
})

url = endpoint + "?" + params

print("url = ", url)

data = request.urlopen(url).read()
text = data.decode("utf8")

print(text)

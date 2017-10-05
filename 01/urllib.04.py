import urllib.request
import urllib.parse

endpoint = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
params = urllib.parse.urlencode({
    "stn": "108"
})

url = endpoint + "?" + params

print("url = ", url)

data = urllib.request.urlopen(url).read()
text = data.decode("utf8")

print(text)

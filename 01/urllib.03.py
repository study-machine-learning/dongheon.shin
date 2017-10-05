import urllib.request

url = "http://api.aoikujira.com/ip/ini"

data = urllib.request.urlopen(url).read()
text = data.decode("utf8")

print(text)

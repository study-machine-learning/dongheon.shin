import requests

res = requests.get("http://api.aoikujira.com/time/get.php")

text = res.text
print(text)

bin = res.content
print(bin)

import requests
import json


def k2c(k):
    return str(k - 273.15)


api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"
apikey = "<API_KEY>"

cities = ["Seoul,KR", "Tokyo,JP", "New York,US"]

for name in cities:

    url = api.format(city=name, key=apikey)
    res = requests.get(url)

    data = json.loads(res.text)

    print("+ 도시 = ", data["name"])
    print("| 날씨 = ", data["weather"][0]["description"])
    print("| 최저 기온 = ", k2c(data["main"]["temp_min"]))
    print("| 최고 기온 = ", k2c(data["main"]["temp_max"]))
    print("| 습도 = ", data["main"]["humidity"])
    print("| 기압 = ", data["main"]["pressure"])
    print("| 풍향 = ", data["wind"]["deg"])
    print("| 풍속 = ", data["wind"]["speed"])

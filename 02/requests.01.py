from bs4 import BeautifulSoup as soup

import requests

username = "callistian"
password = "my_password"

session = requests.session()

login_info = {
    "m_id": username,
    "m_passwd": password
}

url_login = "http://www.hanbit.co.kr/member/login_proc.php"

res = session.post(url_login, data=login_info)
res.raise_for_status()

url_info = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"

res = session.get(url_info)
res.raise_for_status()

content = soup(res.text, "html.parser")

mileage = content.select_one(".mileage_section1 span").string
coin = content.select_one(".mileage_section2 span").string

print("mileage = ", mileage)
print("coin = ", coin)

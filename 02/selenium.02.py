from selenium import webdriver

username = "henlix"
password = "my_password"

browser = webdriver.PhantomJS()
browser.implicitly_wait(5)

url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)

el = browser.find_element_by_id("id")
el.clear()
el.send_keys(username)

el = browser.find_element_by_id("pw")
el.clear()
el.send_keys(password)

form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()


url_shopping_list = "https://order.pay.naver.com/home?tabMenu=SHOPPING"
browser.get(url_shopping_list)

products = browser.find_elements_by_css_selector(".p_info span")

for product in products:
    print("- ", product.text)

# PYTHONIOENCODING=utf-8:surrogateescape python3 selenium.02.py

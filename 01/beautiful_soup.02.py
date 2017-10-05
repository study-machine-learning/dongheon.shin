from bs4 import BeautifulSoup as soup

html = """
<html>
    <body>
        <h1 id="title">스크레이핑이란?</h1>
        <p>웹 페이지를 분석하는 것</p>
        <p id="section">원하는 부분을 추출하는 것</p>
    </body>
</html>
"""

content = soup(html, "html.parser")

title = content.find(id="title")
section = content.find(id="section")

print("title = ", title.string)
print("section = ", section.string)

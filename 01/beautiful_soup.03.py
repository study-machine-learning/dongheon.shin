from bs4 import BeautifulSoup as soup

html = """
<html>
    <body>
        <ul>
            <li><a href="http://www.naver.com">NAVER</a></li>
            <li><a href="http://www.daum.net">DAUM</a></li>
        </ul>
    </body>
</html>
"""

content = soup(html, "html.parser")

links = content.find_all("a")

for a in links:
    print(a.string, " > ", a.attrs["href"])

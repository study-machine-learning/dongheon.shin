from bs4 import BeautifulSoup as soup

import re

html = """
<html>
    <body>
        <ul>
            <li><a href="hoge.html">hoge</a></li>
            <li><a href="https://example.com/fuga">fuga*</a></li>
            <li><a href="https://example.com/foo">foo*</a></li>
            <li><a href="https://example.com/aaa">aaa</a></li>
        </ul>
    </body>
</html>
"""

content = soup(html, "html.parser")

li = content.find_all(href=re.compile(r"https://"))

for e in li:
    print(e.attrs['href'])

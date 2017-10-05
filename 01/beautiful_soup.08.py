from bs4 import BeautifulSoup as soup

html = """
<html>
    <body>
        <ul id="bible">
            <li id="ge">GENESIS</li>
            <li id="ex">EXODUS</li>
            <li id="le">LEVITIICUS</li>
            <li id="nu">NUMBERS</li>
            <li id="de">DEUTERONOMY</li>
        </ul>
    </body>
</html>
"""


def selector(q):
    print (content.select_one(q).string)


content = soup(html, "html.parser")

selector("#nu")
selector("li#nu")
selector("ul > li#nu")
selector("#bible #nu")
selector("#bible > #nu")
selector("ul#bible > li#nu")
selector("li[id='nu']")
selector("li:nth-of-type(4)")

print(content.select("li")[3].string)
print(content.find_all("li")[3].string)

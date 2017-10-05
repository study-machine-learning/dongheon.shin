from bs4 import BeautifulSoup as soup

html = """
<html>
    <body>
        <div id="main-goods" data-lo="ko">
            <ul id="fr-list">
                <li class="red green" data-lo="ko">사과</li>
                <li class="purple" data-lo="us">포도</li>
                <li class="yellow" data-lo="us">레몬</li>
                <li class="yellow" data-lo="ko">오렌지</li>
            </ul>
            <ul id="ve-list">
                <li class="white green" data-lo="ko">무</li>
                <li class="red green" data-lo="us">파프리카</li>
                <li class="black" data-lo="ko">가지</li>
                <li class="black" data-lo="us">아보카도</li>
                <li class="white" data-lo="cn">연근</li>
            </ul>
        </div>
    </body>
</html>
"""

content = soup(html, "html.parser")

print(content.select_one("li:nth-of-type(8)").string)
print(content.select_one("#ve-list > li:nth-of-type(4)").string)
print(content.select("#ve-list > li[data-lo='us']")[1].string)
print(content.select("#ve-list > li.black")[1].string)

condition = {
    "data-lo": "us",
    "class": "black"
}

print(content.find("li", condition).string)
print(content.find(id="ve-list").find("li", condition).string)

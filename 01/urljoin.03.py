from bs4 import BeautifulSoup as soup
from urllib.request import urlretrieve
from urllib.parse import urlparse, urljoin
from os import makedirs

import os.path
import time
import re

proc_files = {}


# get links in html
def enum_links(html, base):

    content = soup(html, "html.parser")

    # add stylesheet and links
    links = content.select("link[rel='stylesheet']")
    links += content.select("a[href]")

    result = []

    for a in links:
        href = a.attrs['href']
        url = urljoin(base, href)

        result.append(url)

    return result


# download files and mark files as 'downloaded'
def download_file(url):

    link = urlparse(url)
    path = "./" + link.netloc + link.path

    if re.search(r"/$", path):
        path += "index.html"

    dirname = os.path.dirname(path)

    if os.path.exists(path):
        return path

    if not os.path.exists(dirname):
        print("mkdir = ", dirname)
        makedirs(dirname)

    try:
        print("download = ", url)
        urlretrieve(url, path)
        time.sleep(1)
        return path
    except Exception:
        print("download failed = ", url)
        return None


def analyze_html(url, root_url):

    # download a file with a specified url
    path = download_file(url)

    if path is None:
        return

    if path in proc_files:
        return

    proc_files[path] = True

    print("analyze_html = ", url)

    html = open(path, "r", encoding="utf-8").read()
    links = enum_links(html, url)

    for link in links:

        # do not download external links
        if link.find(root_url) != 0:
            if not re.search(r".css$", link):
                continue

        # analyze html file
        if re.search(r".(html|htm)$", link):
            analyze_html(link, root_url)
            continue

        # download files extracted from a specified url
        download_file(link)


if __name__ == "__main__":

    url = "https://docs.python.org/3.6/library/"
    analyze_html(url, url)

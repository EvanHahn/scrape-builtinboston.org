#!/usr/bin/env python

from requests import get
from bs4 import BeautifulSoup

soup = BeautifulSoup(get("http://bostonbuilt.org/").text)

icons = soup.select(".repping-icon")
for icon in icons:
    url = icon.parent.get("href").replace("http.", "http://")
    if (("localhost" in url) or
            ("0.0.0.0" in url) or
            ("." not in url) or
            (url == "http://")):
        continue
    if url[-1] == "'":
        url = url[:-1]
    print(url)

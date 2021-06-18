#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

LINK = "http://park11.wakwak.com/~hkn/"

def scrapeFromSazae(link) -> str:
  soup = BeautifulSoup(requests.get(LINK+"bunseki0.htm").text, "html.parser")
  print(soup.find("pre").text)


def scrape():
  soup = BeautifulSoup(requests.get(LINK+"bunseki0.htm").text, "html.parser")

  links = [url.get('href') for url in soup.find_all('a')]
  links.pop(0)

  for link in links:
    scrapeFromSazae(LINK+link)




scrape()

#!/usr/bin/env python3

import codecs
import requests
from bs4 import BeautifulSoup

LINK = "http://park11.wakwak.com/~hkn/"

def scrapeFromSazae(link):
  bf = requests.get(link);
  bf.encoding = "shift_jis"
  soup = BeautifulSoup(bf.text, "html.parser")
  print(soup.find("pre").string, file=codecs.open("res.txt","a","shift_jis"))


def scrape():
  soup = BeautifulSoup(requests.get(LINK+"bunseki0.htm").text, "html.parser")

  links = [url.get('href') for url in soup.find_all('a')]
  links.pop(0)

  for link in links:
    scrapeFromSazae(LINK+link)

scrape()

#!/usr/bin/env python3

import codecs
import requests
import os
from bs4 import BeautifulSoup

LINK = "http://park11.wakwak.com/~hkn/"
FILE = "res.txt"
BF = "res.bf.txt"

def scrapeFromSazae(link):
  bf = requests.get(link);
  bf.encoding = "shift_jis"
  soup = BeautifulSoup(bf.text, "html.parser")
  print(soup.find("pre").string, file=codecs.open(BF,"a","shift_jis"))

def scrape():
  soup = BeautifulSoup(requests.get(LINK+"bunseki0.htm").text, "html.parser")

  links = [url.get('href') for url in soup.find_all('a')]
  links.pop(0)

  for link in links:
    scrapeFromSazae(LINK+link)

def convertShiftJisToUTF8(_fin,_fout):
  fin = codecs.open(_fin,"r","shift_jis")
  fout = codecs.open(_fout,"w","utf-8")

  for i in fin:
    fout.write(i)

  fin.close()
  fout.close()

  os.remove(_fin)

scrape()
convertShiftJisToUTF8(BF,FILE)

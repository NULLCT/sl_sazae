#!/usr/bin/env python3

import codecs

def formatLine(line) -> str:
  #remove "第"
  line = line[1:]
  #放送中止
  if not line[0].isdigit():
    return "ERROR"

  #remove "回"
  line = line[0:line.find("回")] + line[line.find("回")+1:]

  cnt = 0
  for i in range(len(line)):
    if line[i] == " ":
      cnt+=1
      if cnt == 3:
        line = line[0:i] + "\n"
        break

  line = line.replace(" ",",")

  return line

def format():
  fin = ""
  with open("res.txt","r") as file:
    for line in file:
      if line != "\n":
        res = formatLine(line)
        if res != "ERROR":
          fin += res

  print(fin,end="",file=codecs.open("res_formatted.csv","w"))

format()

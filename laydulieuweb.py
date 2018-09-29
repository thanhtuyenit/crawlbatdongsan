#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 11:17:11 2018
@author: kerry
"""

# import libraries
import urllib.request
from bs4 import BeautifulSoup
import csv
import requests


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36'}
r=requests.get('https://batdongsan.com.vn/nha-dat-ban-da-nang/p5', headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
# find results within table
table = soup.find('div', attrs={'class': 'Main'})

results = soup.select('div[class*="search-productItem"]')

print('Number of results', len(results))

rows = []
rows.append(['Title', 'Area', 'Price','Location','Date','Detail'])

for result in results:
    # extract tilte
    title = result.find('a').getText()
    print(title)
    content = result.find('div', attrs ={'class':'p-main-text'}).getText()
    print(content)
    price = result.find('span', attrs ={'class':'product-price'}).getText()
    print(price)
    date = result.find('div', attrs ={'class':'floatright mar-right-10'}).getText()
    print(date)
    location = result.find('span', attrs ={'class':'product-city-dist'}).getText()
    print(s)
    s = result.find('span', attrs ={'class':'product-area'}).getText()
    print(s)
    rows.append([title,s,price,location,date,content])
with open('batdongsan.csv','w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows)
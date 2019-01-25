# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:11:07 2019
To get id

@author: york
"""

import requests
from bs4 import BeautifulSoup
import datetime
import csv

url_list = []

for p_number in range(0,82): # page 0 to 81, 最終頁數目前是手動加上去
    url_list.append('https://data.gov.tw/suggests?page='+str(p_number))

id_list = []

for url in url_list:    
    resp = requests.get(url)
    resp.encoding = 'utf-8' # encoded with format utf-8 for chinese character
    soup = BeautifulSoup(resp.text, 'lxml')
    atags = soup.find_all('a')
    
    for tag in atags:
        if (tag.get('href')[0:6] == '/node/' 
        and tag.get('href')[6:] != "37299"): # 排除"政府網站資料開放宣告"
            print(tag.get('href')[6:])
            id_list.append([tag.get('href')[6:]])

t_obj = datetime.datetime.now()
t = str(t_obj)
legal_time_str = t[0:10]+'-'+t[11:13]+'-'+t[14:16]+'-'+t[17:19]

with open('id_list_' + legal_time_str + '.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(id_list)

csvFile.close()

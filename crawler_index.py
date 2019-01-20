# -*- coding: utf-8 -*-
"""
To get id
"""

import requests
from bs4 import BeautifulSoup
import pickle

#url1 = 'https://movies.yahoo.com.tw/chart.html'
#resp1 = requests.get(url1)
#resp1.encoding = 'utf-8' # encoded with format utf-8 for chinese character
#soup1 = BeautifulSoup(resp1.text, 'lxml')

#url3 = 'https://data.gov.tw/node/7967'
#resp3 = requests.get(url3)
#resp3.encoding = 'utf-8' # encoded with format utf-8 for chinese character
#soup3 = BeautifulSoup(resp3.text, 'lxml')


url_list = []
for p_number in range(1,82):
    url_list.append(['https://data.gov.tw/suggests?page='+str(p_number)])
#print(url_list)

id_list = []
for url in url_list:    
    url = 'https://data.gov.tw/suggests?page=81'
    resp = requests.get(url)
    resp.encoding = 'utf-8' # encoded with format utf-8 for chinese character
    soup = BeautifulSoup(resp.text, 'lxml')
    atags = soup.find_all('a')
    #tbody_section.get('href')1
    for tag in atags:
        if (tag.get('href')[0:6] == '/node/' 
        and tag.get('href')[6:] != "37299"):
            print(tag.get('href')[6:])
            id_list.append(tag.get('href')[6:])

if 0:
    with open("id_list.pylist", "wb") as fp:   #Pickling
        pickle.dump(id_list, fp)
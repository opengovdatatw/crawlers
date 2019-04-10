# -*- coding: utf-8 -*-
"""
Created on Tue Apr 9 22:59:00 2019

Get { ID | numbers of agency assigned | names of those agencies }

@author: york
"""
import requests
from bs4 import BeautifulSoup
import datetime
import csv


# crawl all the node-ID

## generate all URLs
url_list = []
for page_number in range(0,83):  # page 0 to 83, 最終頁數目前是手動加上去 
    url_list.append('https://data.gov.tw/suggests?page='+str(page_number))

## collect all node-ID in `id_list`
id_list = []
for url in url_list:
    resp = requests.get(url)
    resp.encoding = 'utf-8'  # encoded with format utf-8 for chinese character
    soup = BeautifulSoup(resp.text, 'lxml')  
    atags = soup.find_all('a')
    for tag in atags:
        if (tag.get('href')[0:6] == '/node/'
        and tag.get('href')[6:] != "37299"): # 排除"政府網站資料開放宣告"
            print(tag.get('href')[6:])
            id_list.append([tag.get('href')[6:]])


all_contents = []  # This list contains all we want.

label_list = ['ID', "派發機關number", "派發機關"]  # the row of labels
all_contents.append(label_list)

for id in id_list:

    id_str = id[0]

    single_list = []

    single_list.append(id_str)  # generate URL

    url = 'https://data.gov.tw/node/' + id_str
    resp = requests.get(url)
    resp.encoding = 'utf-8' # encoded with format utf-8 for chinese character
    soup = BeautifulSoup(resp.text, 'lxml')

    if 1:
        # 派發機關
        assign_agency = soup.find_all(
            'div', class_='field field-name-field-assign-agency field-type-entityreference field-label-inline clearfix'
            )[0].find_all(
                    'div', class_='field-items'
                    )[0].find_all(
                            'div'
                            )
if 0:
    with open('all_contents_' + legal_time_str + '.csv', 'w',encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(all_contents)
    csvFile.close()


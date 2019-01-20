# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 09:38:50 2019
Given id, to get contents
@author: york
"""
import requests
from bs4 import BeautifulSoup
import pickle

with open("id_list.pylist", "rb") as fp:   # Unpickling
    id_list = pickle.load(fp)

label_list = ['ID', '建議之標題', '建議資料集名稱', '建議開放的欄位', '建議原因', '派發機關', '回復狀態', '分派狀態', '回復時間', '回應']
#    reply_1_title, reply_1_acc, reply_1_time, reply_1_conten
#    reply_2_title, reply_2_acc, reply_2_time, reply_2_conten
#    reply_3_title, reply_3_acc, reply_3_time, reply_3_conten
all_contents = []
all_contents.append(label_list)
for id in id_list:
    single_list = []
    
    single_list.append(id)    
    url = 'https://data.gov.tw/node/' + id
    resp = requests.get(url)
    resp.encoding = 'utf-8' # encoded with format utf-8 for chinese character
    soup = BeautifulSoup(resp.text, 'lxml')

    # 建議之標題--其內容
    node_title = soup.find_all('h1', class_='node-title')
    for node_title_row in node_title:
        single_list.append(node_title_row.string)

    # 欄位內容 
    field_item = soup.find_all('div', class_='field-item')
    for row in field_item[0:7]:
        single_list.append(row.string)
        
    comments_content = soup.find_all('div', class_='field field-name-comment-body field-type-text-long field-label-hidden')
    for row in comments_content:
        rowrow = row.find('p')
        single_list.append(rowrow)
    
    all_contents.append(single_list)



import csv
with open('all_contents.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(all_contents)
csvFile.close()








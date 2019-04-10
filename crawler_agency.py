# -*- coding: utf-8 -*-
"""
Created on Tue Apr 9 22:59:00 2019

Get { ID | numbers of agency assigned | names of those agencies }

@author: york
"""
import requests
from bs4 import BeautifulSoup
import csv
import datetime

# crawl all the node-ID

## collect all node-ID in `id_list`
if 0:  ### Get IDs right now
    ## generate all URLs
    url_list = []
    for page_number in range(0,83):  # page 0 to 83, 最終頁數目前是手動加上去 
        url_list.append('https://data.gov.tw/suggests?page='+str(page_number))
        id_list = []
    for url in url_list:
        resp = requests.get(url)
        resp.encoding = 'utf-8'  # encoded with format utf-8 for chinese character
        soup = BeautifulSoup(resp.text, 'lxml')  
        atags = soup.find_all('a')
        for tag in atags:
            if (tag.get('href')[0:6] == '/node/'
            and tag.get('href')[6:] != "37299"): # 排除"政府網站資料開放宣告"
                #print(tag.get('href')[6:])
                id_list.append([tag.get('href')[6:]])

else:  ### use IDs stored
    id_list = []
    with open('id_list_2019-04-10-15-35-13.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            id_list.append(row)  # e.g., id_list.append(['86086'])
    


all_contents = []  # This list contains all we want.

label_list = ['ID', "派發機關number", "派發機關"]  # the row of labels
all_contents.append(label_list)

for id in id_list:

    id_str = id[0]

    single_list = []
    
    # Put the ID in this single_list
    single_list.append(id_str)  # Get { ID }

    # Get the SOUP
    url = 'https://data.gov.tw/node/' + id_str
    resp = requests.get(url)
    resp.encoding = 'utf-8' # encoded with format utf-8 for chinese character
    soup = BeautifulSoup(resp.text, 'lxml')

# for debugging
    print(id_str)

    # Get 派發機關 form the soup
    assign_agency = soup.find_all(
        'div', class_='field field-name-field-assign-agency field-type-entityreference field-label-inline clearfix'
        )[0].find_all( # ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
                'div', class_='field-items'
                )[0].find_all(
                        'div'
                        )
    # Put the number of agencies in this single_list
    single_list.append(len(assign_agency))  # Get { ID | number }
    
    # Put the names of agencies in this single_list
    for every_item in assign_agency:
        single_list.append(every_item.string) # Get {ID|number|臺南市政府...}
    
    # Add this single_list to the chart
    all_contents.append(single_list)
    
    
if 0:
    t_obj = datetime.datetime.now()
    t = str(t_obj)
    legal_time_str = t[0:10]+'-'+t[11:13]+'-'+t[14:16]+'-'+t[17:19]
    
    with open('agency_' + legal_time_str + '.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(id_list)
    csvFile.close()



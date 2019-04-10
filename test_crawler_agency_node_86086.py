# -*- coding: utf-8 -*-
"""
Created on Tue Apr 9 22:59:00 2019

Get { ID | numbers of agency assigned | names of those agencies }

@author: york
"""
import requests
from bs4 import BeautifulSoup
import csv

id_list = [['86086']] 

all_contents = []  # This list contains all we want.

label_list = ['ID', "派發機關數量", "派發機關"]  # the row of labels
all_contents.append(label_list)

for id in id_list:

    id_str = id[0]

    single_list = []  

    # Put the ID in this single_list
    single_list.append(id_str)  

    # Get the SOUP
    url = 'https://data.gov.tw/node/' + id_str
    resp = requests.get(url)
    resp.encoding = 'utf-8' # encoded with format utf-8 for chinese character
    soup = BeautifulSoup(resp.text, 'lxml')

    # Get the 派發機關
    assign_agency = soup.find_all(
        'div', class_='field field-name-field-assign-agency field-type-entityreference field-label-inline clearfix'
        )[0].find_all(
                'div', class_='field-items'
                )[0].find_all(
                        'div')
    
    # Put the number of agencies in this single_list
    single_list.append(len(assign_agency))
    
    # Put the names of agencies in this single_list
    for every_item in assign_agency:
        single_list.append(every_item.string)
    
    # Add this single_list to the chart
    all_contents.append(single_list)
    
if 1:
    with open('test_crawler_assign_agency_node_86086.csv', 'w',encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(all_contents)
    csvFile.close()


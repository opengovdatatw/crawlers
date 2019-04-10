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



id_list = [['86086']] 

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

    # count the number of agency

    if 1:
        # 派發機關
        assign_agency = soup.find_all(
            'div', class_='field field-name-field-assign-agency field-type-entityreference field-label-inline clearfix'
            )[0].find_all(
                    'div', class_='field-items'
                    )[0].find_all(
                            'div')

        number_assign_agency = len(assign_agency)
if 0:
    with open('all_contents_' + legal_time_str + '.csv', 'w',encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(all_contents)
    csvFile.close()


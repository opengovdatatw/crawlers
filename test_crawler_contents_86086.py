# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:34:12 2019
Given ID=86086, to get contents.
For fixing issue #3
@author: york
"""
import requests
from bs4 import BeautifulSoup
import datetime
import csv

def soup_prettify2(soup, desired_indent): #where desired_indent is number of spaces as an int() 
	pretty_soup = str()
	previous_indent = 0
	for line in soup.prettify().split("\n"): # iterate over each line of a prettified soup
		current_indent = str(line).find("<") # returns the index for the opening html tag '<' 
		# which is also represents the number of spaces in the lines indentation
		if current_indent == -1 or current_indent > previous_indent + 2:
			current_indent = previous_indent + 1
			# str.find() will equal -1 when no '<' is found. This means the line is some kind 
			# of text or script instead of an HTML element and should be treated as a child 
			# of the previous line. also, current_indent should never be more than previous + 1.	
		previous_indent = current_indent
		pretty_soup += write_new_line(line, current_indent, desired_indent)
	return pretty_soup
		
def write_new_line(line, current_indent, desired_indent):
	new_line = ""
	spaces_to_add = (current_indent * desired_indent) - current_indent
	if spaces_to_add > 0:
		for i in range(spaces_to_add):
			new_line += " "		
	new_line += str(line) + "\n"
	return new_line



id_list = [['86086']] # the target node, which causing issue
        
label_list = ['ID', '建議之標題', '建議資料集名稱', '建議開放的欄位', '建議原因', '派發機關', '回復狀態', '分派狀態', '回復時間', '回應']

all_contents = []
all_contents.append(label_list)

for id in id_list:

    id_str = id[0]
    print(id_str)
    
    single_list = []
    
    single_list.append(id_str)  # generate URL
    url = 'https://data.gov.tw/node/' + id_str
    resp = requests.get(url)
    resp.encoding = 'utf-8' # encoded with format utf-8 for chinese character
    soup = BeautifulSoup(resp.text, 'lxml')
    
    if 0:
        # 開放建議標題 # <h1 class="node-title">
        node_title = soup.find_all('h1', class_='node-title')
        for node_title_row in node_title:
            single_list.append(node_title_row.string)
    if 0:
        # 建議資料集名稱 
        suggest_dataset = soup.find_all(
                'div', class_='field field-name-field-suggest-dataset field-type-text field-label-inline clearfix'
                )[0].find_all(
                        'div', class_='field-items'
                        )[0].find_all(
                                'div', class_='field-item even'
                                )[0].string
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
        # 回應之內容        
        comments_content = soup.find_all('div', class_='field field-name-comment-body field-type-text-long field-label-hidden')
        for sub_comments_content in comments_content:
            single_list.append(sub_comments_content.div.div.find_all('p'))
    if 0:
        all_contents.append(single_list)


t_obj = datetime.datetime.now()
t = str(t_obj)
legal_time_str = t[0:10]+'-'+t[11:13]+'-'+t[14:16]+'-'+t[17:19]


if 0:
    with open('all_contents_' + legal_time_str + '.csv', 'w',encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(all_contents)
    csvFile.close()
if 0:
    pretty_soup = soup_prettify2(soup, desired_indent=4)
    with open("node_86086.html", "w") as html_file:
        html_file.write(pretty_soup)
    html_file.close()

import requests
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import csv

link = 'https://medschool.ucsd.edu/som/pharmacology/faculty/Pages/default.aspx'
page_source = requests.get(link)
soup = bs(page_source.content,'html.parser')

list_names,list_titles,list_phones,list_emails = [],[],[],[]

rowsOdd = soup.find_all('tr',class_="health-sciencesTableOddRow ms-rteTableOddRow-3")
rowsEven = soup.find_all('tr',class_="health-sciencesTableEvenRow ms-rteTableEvenRow-3")
rows = rowsOdd + rowsEven

for row in rows:
    a = row.find_all('a')
    td = row.find_all('td')
    
    name = a[0].text
    list_names.append(name)

    email = a[1].text
    list_emails.append(email)

    x = 0
    for i in td:
        if '858' in str(i) and 'Odd' in str(i):
            phone = i.text
            list_phones.append(phone)
            x+=1
        else:
            continue
    if x == 0:
        list_phones.append(None)
    
    title = td[0].text
    ntitle = title[len(name)+1:]
    list_titles.append(ntitle)

#convert to CSV
dictionary = {
'Name':list_names,
'Title':list_titles,
'Email':list_emails,
'Phone':list_phones
}

dataframe = pd.DataFrame(dictionary)

dataframe.to_csv('UCSD_pharmacology.csv')
    

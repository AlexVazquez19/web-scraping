import requests
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import csv

link = 'https://medschool.ucsd.edu/som/radiology/about/directories/Pages/Faculty.aspx'
page_source = requests.get(link)
soup = bs(page_source.content,'html.parser')

table = soup.find('table',id='facultyTable')
rows = table.find_all('tr')
del(rows[0])

list_names,list_titles,list_divisions,list_emails,list_phones = [],[],[],[],[]

track = 0
for row in rows:
    a = row.find_all('a')
    td = row.find_all('td')
    
    #name
    name = a[0].text
    list_names.append(name)

    #email
    if len(a) > 1:
        email = a[1].text
        list_emails.append(email)
    else:
        list_emails.append(None)

    #title
    title = td[1].text
    list_titles.append(title)

    #division
    division = td[2].text
    list_divisions.append(division)

    #phone
    phone = row.find('span',style="white-space:nowrap;display:block")
    if phone != None:
        list_phones.append(phone.text)
    else:
        list_phones.append(None)
    print(phone.text)
    
    track+=1
    print(track)
    
#convert to CSV
dictionary = {
'Name':list_names,
'Title':list_titles,
'Division':list_divisions,
'Email':list_emails,
'Phone':list_phones
}

dataframe = pd.DataFrame(dictionary)

dataframe.to_csv('UCSD_radiology.csv')
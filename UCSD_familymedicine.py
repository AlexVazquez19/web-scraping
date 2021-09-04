import requests
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import csv

link = 'https://medschool.ucsd.edu/som/neurosciences/faculty/Pages/default.aspx'
page_source = requests.get(link)
soup = bs(page_source.content,'html.parser')

table = soup.find('table',id="facultyTable")
rows = table.find_all('tr')
del(rows[0])

list_names,list_titles,list_divisions,list_emails,list_phones = [],[],[],[],[]

track=0
for row in rows:
    td = row.find_all('td')

    #name
    name = row.find('a')
    if name != None:
        list_names.append(name.text)
    else:
        list_names.append(None)

    #title
    title = td[1].text
    list_titles.append(title)

    #division
    division = td[2].text
    list_divisions.append(division)

    #emails
    email = td[3].find('a')
    if email != None:
        list_emails.append(email.text)
    else:
        list_emails.append(None)

    #phone
    phone = td[3].find('span')
    if phone != None:
        list_phones.append(phone.text)
    else:
        list_phones.append(None)
    
    track+=1
    print(track)
    if track == 140:
        break


#convert to CSV
dictionary = {
'Name':list_names,
'Title':list_titles,
'Division':list_divisions,
'Email':list_emails,
'Phone':list_phones,
}

dataframe = pd.DataFrame(dictionary)

dataframe.to_csv('UCSD_neurosciences_faculty.csv')

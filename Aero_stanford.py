import requests
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import csv
import random

link = 'https://aa.stanford.edu/people/faculty'
page_source = requests.get(link)
soup = bs(page_source.content,'html.parser')

col1 = soup.find_all('div',class_="flex-3-of-12 views-col col-1")
col2 = soup.find_all('div',class_="flex-3-of-12 views-col col-2")
col3 = soup.find_all('div',class_="flex-3-of-12 views-col col-3")
cols = col1 + col2 + col3

list_names,list_titles,list_bios,list_emails = [],[],[],[]

track = 0
for col in cols:
    #name
    name = col.find('div',class_="field-content")
    list_names.append(name.text.strip())

    lnk = col.find('a').get('href')
    fullLink = 'https://aa.stanford.edu/' + lnk
    page_source2 = requests.get(fullLink)
    soup2 = bs(page_source2.content,'html.parser')
    
    #title
    title = soup2.find('div',class_="su-person-full-title node stanford-person string-long label-hidden")
    if title != None:
        list_titles.append(title.text.strip())
    else:
        list_titles.append(None)
    
    #email
    email = soup2.find('div',class_="su-person-email node stanford-person email label-hidden")
    if email != None:
        list_emails.append(email.text)
    else:
        list_emails.append(None)
    
    #bio
    bio = soup2.find('div',class_="su-person-body su-wysiwyg-text node stanford-person body text-with-summary label-hidden")
    if bio != None:
        list_bios.append(bio.text)
    else:
        list_bios.append(None)

    track+=1
    print(track)

#convert to CSV
dictionary = {
'Name':list_names,
'Title':list_titles,
'Email':list_emails,
'Bio':list_bios
}

dataframe = pd.DataFrame(dictionary)

dataframe.to_csv('Aero_Stanford.csv')
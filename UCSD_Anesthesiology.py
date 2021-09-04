import requests
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import csv
import random

link = 'https://medschool.ucsd.edu/som/anesthesia/about/Pages/Faculty.aspx'
page_source = requests.get(link)
soup = bs(page_source.content,'html.parser')

td = soup.find_all('td')
td2 = []
for i in td:
    td2.append(i.text)

names = []
titles = []
divisions = []
emails = []
z = 0
for j in td2:
    if z == 0:
        names.append(j)
    elif z == 1:
        titles.append(j)
    elif z == 2:
        divisions.append(j)
    elif z == 3:
        emails.append(j)
    z+=1
    if z == 4:
        z = 0

#convert to CSV
dictionary = {
'Name':names,
'Title':titles,
'Division':divisions,
'Email':emails
}

dataframe = pd.DataFrame(dictionary)

dataframe.to_csv('UCSD_Anesthesiology_faculty.csv')
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import csv

link = 'https://medschool.ucsd.edu/som/medicine/about/faculty/Pages/Faculty-Directory.aspx'
page_source = requests.get(link)
soup = bs(page_source.content,'html.parser')

tr = soup.find_all('tr')
del tr[0]

#find elements
names = []
titles = []
divisions = []
emails = []
for elem in tr:
    name = elem.find('a').text
    names.append(name)

    td = elem.find_all('td')
    title = td[1].text
    titles.append(title)
    division = td[2].text
    divisions.append(division)
    email = td[3].text
    emails.append(email)

#convert to CSV
dictionary = {
'Name':names,
'Title':titles,
'Division':divisions,
'Email':emails
}

dataframe = pd.DataFrame(dictionary)

dataframe.to_csv('UCSD_medicine_faculty.csv')


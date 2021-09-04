from typing import Text
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import csv
import random

link = 'https://aerospace.illinois.edu/directory/faculty'
page_source = requests.get(link)
soup = bs(page_source.content,'html.parser')

list_names,list_emails,list_titles,list_phones,list_resInterests,list_resAreas = [],[],[],[],[],[]

track = 0
profiles = soup.find_all('div',class_='item person cat15 aero')
for profile in profiles:
    
    name = profile.find('div',class_='name').text
    list_names.append(name)

    title = profile.find('div',class_='title').text
    list_titles.append(title)

    email = profile.find('div',class_='email')
    if email != None:
        email2 = email.find('a')
        if email2 != None:
            email3 = email2.get('href')
            list_emails.append(email3[7:])
        else:
            list_emails.append(None)
    else:
        list_emails.append(None)

    phone = profile.find('div',class_='phone')
    if phone != None:
        phone2 = phone.find('a')
        if phone2 != None:
            phone3 = phone2.get('href')
            list_phones.append(phone3[4:])
        else:
            list_phones.append(None)
    else:
        list_phones.append(None)

    lnk = 'https://aerospace.illinois.edu' + profile.find('div',class_='name').find('a').get('href')
    source = requests.get(lnk)
    soup2 = bs(source.content,'html.parser')
    prof = soup2.find('div',class_="directory-profile maxwidth800")
    
    if 'Research Interests' in str(prof):
        pr = str(prof)
        idx = pr.index('Research Interests')
        cut = pr[idx+33:]

        res = []
        i = 0
        while i < len(cut):
            if cut[i:i+5] == '</li>':
                break
            res.append(cut[i])
            i+=1
        resInterest = ''.join(res)
        list_resInterests.append(resInterest)
    else:
        list_resInterests.append(None)

    resArea = prof.find('div',class_="extProfileAREA")
    if resArea != None:
        resArea2 = resArea.text.strip()[14:].strip()
        list_resAreas.append(resArea2)
    else:
        list_resAreas.append(None)

    track+=1
    print(track)

'''
print('____________________')
print(len(list_names))
print(len(list_titles))
print(len(list_emails))
print(len(list_phones))
print(len(list_resInterests))
print(len(list_resAreas))
'''

#convert to CSV
dictionary = {
'Name':list_names,
'Title':list_titles,
'Email':list_emails,
'Phone':list_phones,
'Research Interests':list_resInterests,
'Research Areas':list_resAreas
}

dataframe = pd.DataFrame(dictionary)

dataframe.to_csv('Aero_illinois.csv')
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import csv

link = 'https://medschool.ucsd.edu/som/cmm/faculty/pages/default.aspx'
page_source = requests.get(link)
soup = bs(page_source.content,'html.parser')

td = soup.find_all('td')
list_names = []
list_links = []
for i in td:
    a = i.find_all('a')
    for j in a:
        list_names.append(j.text)
        list_links.append(j.get('href'))

list_names2 = []
list_titles = []
list_research = []
list_emails = []
list_phones = []
list_focus = []
track = 0
for link in list_links:
    full_link = 'https://medschool.ucsd.edu/' + link
    #full_link = 'https://medschool.ucsd.edu/som/cmm/faculty/Pages/Maike-Sander.aspx'
    source = requests.get(full_link)
    soup2 = bs(source.content,'html.parser')

    #name
    name = soup2.find('div',class_='faculty-name').find('span').text.strip()
    list_names2.append(name)

    #title
    title = soup2.find('div',class_='faculty-name')
    if title != None:
        title2 = title.text.strip()
        title3 = title2[len(name):]
        title4 = title3[:-9].strip()
        list_titles.append(title4)
    else:
        list_titles.append(None)

    #research interests
    research_interests = soup2.find('div',id="ctl00_PlaceHolderMain_ctl05__ControlWrapper_RichHtmlField",class_="ms-rtestate-field",style="display:inline")
    if research_interests != None:
        ri2 = research_interests.find_all('p')
        list_research.append(ri2[0].text)
    else:
         list_research.append(None)

    #email
    email = soup2.find('div',id="ctl00_PlaceHolderMain_ctl04__ControlWrapper_RichHtmlField")
    if email != None and 'mailto' in str(email):
        email2 = email.find_all('a')
        email3 = email2[0].text
        list_emails.append(email3)
    else:
        list_emails.append(None)
    
    #phone
    phone = soup2.find('div',id="ctl00_PlaceHolderMain_ctl04__ControlWrapper_RichHtmlField")
    if phone != None:
        ph = str(phone.text)
        list_phones.append(ph[8:20])
    else:
        list_phones.append(None)
    
    #focus
    focus = soup2.find_all('p',style="text-align:justify;")
    if focus != None and len(focus) > 1:
        list_focus.append(focus[1].text)
    else:
        list_focus.append(None)
    
    track+=1
    print(track)

'''
print(list_names2)
print('')
print(list_titles)
print('')
print(list_emails)
print('')
print(list_phones)
print('')
print(list_research)
print('')
print(list_focus)
'''

#convert to CSV
dictionary = {
'Name':list_names2,
'Title':list_titles,
'Email':list_emails,
'Phone':list_phones,
'Research Interests':list_research,
}

dataframe = pd.DataFrame(dictionary)

dataframe.to_csv('UCSD_cellular_faculty.csv')
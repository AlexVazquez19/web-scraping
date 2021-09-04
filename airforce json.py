import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import csv
import json
import time as t
import datetime

link = 'https://www.usafa.edu/faculty-and-staff/?staff-page-no=1'
page_source = requests.get(link)
soup = bs(page_source.content,'html.parser')

page_links = soup.find_all('a',class_="abcfslPageLink abcfslPageLink_G")
total_pages = int(page_links[-2].text)
print('loading1...')

page_links_list = []
x = 1
for page in range(total_pages):
    start = 'https://www.usafa.edu/faculty-and-staff/?staff-page-no='
    num = str(x)
    combined = start + num
    x += 1
    page_links_list.append(combined)
print('loading2...')

master_list = []
list_names = []
list_positions = []
list_phones = []
list_emails = []
list_bios = []
list_research = []
list_education = []
list_professional = []
list_publications = []
list_honors = []
list_text = []

print('starting loop...')
tracker = 0
for page in page_links_list:
    src = requests.get(page)
    soup1 = bs(src.content,'html.parser')

    profile_div = soup1.find_all('div',class_='SPTL')
    profile_links = []
    for i in profile_div:
        j = i.find('a')
        link = j.get('href')
        profile_links.append(link)

    tracker2 = tracker
    for lnk in profile_links:
        if 'https://www.usafa.edu/facultyprofile/' not in lnk:
            continue
        
        source = requests.get(lnk)
        soups = bs(source.content,'html.parser')
        dic = {}

        #name
        name = soups.find('h4',class_='MP-F1').text
        list_names.append(name)

        #position
        find_position = soups.find('p',class_='T-F23')
        if find_position != None:
            position = find_position.text
        else:
            position = None
        list_positions.append(position)

        #phone number
        find_phone = soups.find('p',class_='T-F2')
        if find_phone != None:
            phone = find_phone.text
        else:
            phone = None
        list_phones.append(phone)

        #email
        find_email = soups.find('p',class_='TH-F29')
        if find_email != None:
            email = find_email.find('a').get('href')[7:]
        else:
            email = None
        list_emails.append(email)

        #research and scholarly interests
        find_research = soups.find('div',class_='CE-F13')
        if find_research != None:
            research = find_research.text
        else:
            research = None
        list_research.append(research)

        #bio
        find_bio = soups.find('div',class_='CE-F7')
        if find_bio != None:
            bio = find_bio.text
        else:
            bio = None
        list_bios.append(bio)

        #education
        find_education = soups.find('div',class_='CE-F15')
        if find_education != None:
            education = find_education.text
        else:
            education = None
        list_education.append(education)

        #professional experience
        find_professional = soups.find('div',class_='CE-F11')
        if find_professional != None:
            professional = find_professional.text
        else:
            professional = None
        list_professional.append(professional)

        #publications
        find_publications = soups.find('p',class_='CE-F22')
        if find_publications != None:
            publications = find_publications.text
        else:
            publications = None
        list_publications.append(publications)

        #honors and awards
        find_honors = soups.find('div',class_='CE-F9')
        if find_honors != None:
            honors = find_honors.text
        else:
            honors = None
        list_honors.append(honors)

        if research == None:
            research = 'None'
        if bio == None:
            bio = 'None'
        if education == None:
            education = 'None'
        if professional == None:
            professional = 'None'
        if publications == None:
            publications = 'None'
        strtext = research + ', ' + bio + ', ' + education + ', ' + professional + ', ' + publications
        list_text.append(strtext)

        nameNoSpecial = ''
        for i in range(len(name)):
            if name[i].isalnum() == True:
                nameNoSpecial += name[i]
        doc_id = 'airforceacademy' + nameNoSpecial

        dic['title'] = name
        dic['company'] = 'Air Force Academy'
        dic['text'] = strtext
        dic['date'] = ''
        dic['emails'] = [email]
        dic['phone_numbers'] = [phone]
        dic['websites'] = ['']
        dic['location'] = ''
        dic['tags'] = ['']
        dic['people'] = [name]
        dic['doc_id'] = doc_id

        JSONdic = json.dumps(dic)
        master_list.append(JSONdic)

        tracker2 += 1
        print(tracker2,end=' ',flush=True)

    tracker += 100
    if tracker == 100:
        break
    print(tracker)

#print(list_names)
#print(list_positions)
#print(list_phones)
#print(list_emails)
#print(list_bios)
#print(list_research)
#print(list_education)
#print(list_professional)
#print(list_publications)
#print(list_honors)
#print(list_text[0])
#print(master_list)

dictionary = {
'Name':list_names,
'Position':list_positions,
'Phone':list_phones,
'Email':list_emails,
'Research':list_research,
'Bio':list_bios,
'Education':list_education,
'Professional Experience':list_professional,
'Publications':list_publications,
'Honors & Awards':list_honors
}

jsonFile = open("airforceacademy_v2.ndjson", "w")
jsonFile.write('\n'.join(master_list))
jsonFile.write('\n')
jsonFile.close()


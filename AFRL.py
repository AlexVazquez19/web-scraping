import requests
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import csv

link = 'https://afrlscholars.usra.edu/opportunities/mentors/'
page_source = requests.get(link)
soup = bs(page_source.content,'html.parser')

profiles = soup.find('div',class_='4u 12u(small) bio')
profiles_links = profiles.find_all('a')

new_links = []
for lnk in profiles_links:
    ext = lnk.get('href')
    new = 'https://afrlscholars.usra.edu/opportunities/mentors/' + ext
    new_links.append(new)

names = []
bios = []
tracker = 0
for lnk in new_links:
    src = requests.get(lnk)
    soup2 = bs(src.content,'html.parser')
    bio = soup2.find('div',class_='8u 12u(small)')
    name = bio.find('b').text
    bio_text = bio.find('p').text
    
    remove = name.split()
    remove2 = []
    for i in remove:
        remove2.append(i.lower())
    query_words = bio_text.split()
    resultwords  = []
    track = 0
    for word in query_words:
        if track < len(remove2):    
            if word.lower() not in remove2:
                resultwords.append(word)
            else:
                track+=1
        else:
            resultwords.append(word)

        
        
    new_bio = ' '.join(resultwords)
    
    names.append(name)
    bios.append(new_bio)
    
    tracker += 1
    print(tracker)

#print(names)
#print(bios)



#Create CSV
dictionary = {
'Name':names,
'Bio':bios
}

dataframe = pd.DataFrame(dictionary)

dataframe.to_csv('afrlV2.csv')

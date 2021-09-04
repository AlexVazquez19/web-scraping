import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

chromedriver_path = "/Users/alejandrovazquez/Downloads/chromedriver"
driver = webdriver.Chrome(chromedriver_path)
URL = 'https://www.ycombinator.com/companies/?batch=S19&batch=W19&batch=W20&batch=S20&batch=W21&batch=S21&regions=United%20States&status=Active&team_size=%5B%221%22%2C%2250%22%5D'
driver.get(URL)
time.sleep(2)

#----------Infinite scroller----------
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(.5)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
#-------------------------------------

#Get raw html of website
page_src = driver.page_source
soup = BeautifulSoup(page_src,'html.parser')
driver.quit()
elems = soup.find('div','styles-module__section___2yul1 styles-module__results___2lP37')

#Creates a list of the company names
company_names = elems.find_all('span',class_='styles-module__coName___3zz21')
company_names_notags = []
for company in company_names:
    company_names_notags.append(company.text)

#Creates a list of company descriptions
company_descriptions = elems.find_all('span',class_='styles-module__coDescription___1b_yd')
company_descriptions_notags = []
for description in company_descriptions:
    company_descriptions_notags.append(description.text)

#Creates a list of company links 
company_links = []
for lnk in elems.find_all('a'):
    company_links.append('https://www.ycombinator.com' + lnk.get('href'))

company_emails = ['hello@zerodown.com', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'hello@therify.co', 'plai@plai.app', 'NA', 'NA', 'info@genomelink.io', 'NA', 'contact@litnerd.com', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'amar@kaipodlearning.com', 'hi@shimmer.care', 'NA', 'NA', 'NA', 'NA', 'hello@covie.io', 'NA', 'hello@simonsays.ai', 'NA', 'NA', 'hello@maroo.us', 'NA', 'NA', 'NA', 'mohit@anakin.company', 'NA', 'info@joindeed.com', 'NA', 'NA', 'info@catenabiosciences.com', 'NA', 'NA', 'NA', 'NA', 'info@hedgehog.app', 'NA', 'business@mentor.cam', 'info@epsilon3.io', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'systems@mayanalytics.com', 'NA', 'contact@waydev.co', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'team@navattic.com', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'hello@rejoyhealth.com', '', 'NA', '', 'NA', 'NA', 'NA', 'NA', 'info@stayflexi.com', 'NA', 'NA', 'NA', 'NA', 'contact@virtualworldarcade.com', 'NA', 'NA', 'NA', 'NA', 'info@worksphere.co', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'info@tint.ai', 'pb@lastbit.io', 'NA', 'support@simplify.jobs', 'founders@milk.video', 'support@processlabs.ai', 'NA', 'support@solosuit.com', 'NA', 'NA', 'hi@quiknode.io', 'NA', '', 'NA', 'NA', 'NA', 'av@datrics.ai', 'NA', 'contact@usehudu.com', 'NA', 'NA', 'NA', 'NA', 'NA', 'support@popl.co', 'NA', 'NA', 'NA', 'NA', 'Hello@Pangea.app', 'info@topkey.io', 'NA', 'NA', 'NA', 'info@alinea-invest.com', 'social@lendflow.io', 'NA', 'NA', 'NA', 'NA', '', 'NA', '', 'sales@firstbase.io', 'NA', 'timbarat@gridware.io', 'NA', 'contact@factionmoto.com', 'hello@remix.so', 'NA', 'NA', 'NA', 'support@sivo.com', 'charge@chargerunning.com', 'NA', 'NA', 'NA', 'NA', 'roger@finary.io', 'NA', '', 'NA', 'NA', 'NA', 'NA', 'hello@spruceid.com', 'NA', 'NA', 'partnerships@coverified.us', 'NA', 'NA', 'NA', 'info@joingerald.com', 'trisha@queenly.com', 'NA', 'NA', 'NA', 'NA', 'NA', 'contact@gigs.live', 'NA', 'NA', 'contacto@imhapi.app', '', 'info@getspokn.com', 'NA', 'hi@taloflow.ai', '', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'hello@runway.team', 'founders@chums.co', 'NA', 'NA', 'NA', 'NA', 'info@capway.co', 'NA', 'NA', 'NA', 'NA', 'NA', 'contact@fieldguide.io', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'hello@warmly.ai', 'NA', 'hello@tryglimpse.com', 'NA', 'NA', 'julia@localmilkrun.com', 'NA', 'NA', 'NA', 'NA', 'NA', 'contact@draftwise.com', 'jase@ready.net', 'NA', 'NA', 'contact@laylo.com', 'NA', 'NA', 'NA', 'NA', 'NA', 'founders@hotplate.com', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'info@piepacker.com', 'hello@notabene.id', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'adam@withyotta.com', '', 'NA', 'NA', 'hello@osmind.org', 'hello@vectrix.io', 'NA', 'NA', 'hello@blissway.com', 'NA', 'NA', 'NA', 'NA', 'NA', 'hello@speedscale.com', 'contact@corecare.io', 'NA', 'support@charityvest.org', 'NA', 'NA', 'NA', 'NA', '', 'NA', '', 'business@queue.gg', 'NA', 'NA', 'NA', 'NA', 'NA', '', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', '', 'NA', 'NA', 'NA', 'hello@searchlight.ai', 'hi@elpha.com', 'NA', 'NA', 'NA', 'NA', 'NA', 'sales@gaspos.co', 'NA', 'support@prelay.com', 'NA', 'marketing@airbyte.io', 'NA', 'NA', 'NA', 'NA', 'josue@guruhotel.com', 'NA', 'NA', 'NA', 'NA', 'sales@electroneek.com', 'NA', 'NA', 'NA', 'NA', 'contact@hiresweet.com', 'support@deepsource.io', 'hello@upflow.io', 'NA', 'NA', 'contact@skypher.co', '', 'NA', 'hey@posthog.com', 'NA', 'NA', 'NA', 'NA', '', 'NA', 'NA', 'hello@buildbuddy.io', '', 'NA', 'contact@tryresponse.com', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'hello@globalbelly.com', 'NA', 'founders@duffl.com', 'help@riyacollective.com', 'NA', 'info@felixbt.com', 'NA', 'NA', 'support@fly.io.', 'team@trygrain.com', '', 'NA', 'info@getbenepass.com', 'info@ezewholesale.com', 'NA', '', 'NA', 'NA', 'NA', 'NA', 'NA', '', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'support@dashworks.ai', '', 'NA', 'contact@acho.io', 'info@exosonic.com', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', '', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'management@mindsdb.com', 'NA', 'NA', 'NA', 'NA', 'contact@polytomic.com', 'NA', 'NA', 'NA', 'info@abalonebio.com', 'NA', '', 'contact@phonic.ai', 'NA', 'NA', 'NA', 'support@datree.io', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'supoprt@taskade.com', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'info@boostbiomes.com', 'NA', 'NA', 'NA', 'contact@lineleaptickets.com', 'contact@earth-ai.com', 'NA', 'contact@wasmer.io', 'info@microverse.org', 'NA', 'info@spotlessmaterials.com\u200b', 'NA', 'NA', 'NA', 'NA', 'NA', 'help@joinblair.com', 'NA', 'NA', 'katherine@florecruit.com', 'NA', 'NA', 'NA', 'NA', 'don@node.eco', 'sales@kubesail.com', 'NA', 'NA', 'NA', 'NA', 'NA', 'info@upequity.com', 'NA', 'NA', 'business@yummy-future.com', 'truenorth@embrace.io', 'support@refinery.io', 'NA', 'NA', 'NA', 'NA', 'contact@trmlabs.com', 'NA', 'NA', 'contact@narrator.ai', '', 'NA', 'support@everloved.com', 'NA', 'NA', 'NA', 'management@hypeandvice.com', 'NA', 'NA', 'NA', 'NA', 'info@givelegacy.com', 'customers@wellprincipled.com', 'info@kraftful.com', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'hello@courier.com', 'NA', 'NA', 'NA', 'NA', 'NA', 'hi@popsql.com', 'NA', 'NA', 'NA', 'NA', 'NA', 'support@spiralgenetics.com', 'support@shef.com', 'info@unionapt.live', 'jijo@buymeacoffee.com', 'hey@catch.co', '', 'NA', '', 'hello@naturallclub.com', 'NA', 'NA', '', 'NA', '', 'ruben@careerkarma.com', 'team@withfriends.co', 'tony@cosmicjs.com', 'info@tryhabitat.com', 'info@workclout.com', 'info@voting.works', '', '', '', '', 'NA', 'sup@beacons.ai', 'hello@slapdash.com', 'support@mudrex.com', '', 'NA', 'info@ampup.io', 'hello@dover.io', '', 'info@alpaca.markets', 'INFO@SARATOGA-ENERGY.COM', 'rohan@upsolve.org', 'hello@superb-ai.com', 'NA', 'info@jetpackaviation.com', '', 'NA', 'NA', 'NA', 'info@instapathbio.com', 'NA', '', 'NA', 'hello@ravn.com', 'hello@doppler.com', '', '', 'tribe@qwest.co', 'NA', 'contact@intacttherapeutics.com', '', '', 'support@handle.com', '', 'contact@probablygenetic.com', 'info@askdata.com', 'hello@okteto.com', 'info@bensen.ai', 'info@atomicalchemy.us', '', 'info@aiinsurance.io', 'hi@avo.app', 'help@theforage.com', 'team@sapling.ai', 'info@weathercheck.co', 'hello@basilica.ai', 'help@communityphone.org', 'info@adventurous.co', 'help@couturme.com', 'jwenig@coursedog.com', 'support@golinks.io', 'hello@middesk.com', 'NA', 'questions@windwalk.games', 'wes@leahlabs.com', '', 'info@medcrypt.co', 'info@brainkey.ai', 'founders@hatchify.co', 'hello@flowercompany.com', 'hello@portalentryways.com', '', '', 'team@windsor.io', 'hello@preflighthq.com', 'NA', '', '', 'NA', '', 'info@getgex.com', 'NA', '', 'NA', '', '', 'support@kalshi.com', 'hello@kopa.co', 'support@keepertax.com', 'contact@vectordash.com', 'founders@interprime.co', '', 'info@pachama.com', 'NA', 'snigdha@thejuggernaut.com', 'info@geosite.io', 'NA', 'hi@rentthebackyard.com', 'support@encarte.io', 'NA', 'hello@flockjay.com', 'contact@overview.ai']


company_emails = []
x=0
for link in company_links:
    page = requests.get(link)
    soup3 = BeautifulSoup(page.content,'html.parser')
    link1 = soup3.find('a',class_='social crunchbase')
    if link1 != None:
        crunchbase_link = link1.get('href')
        driver.get(crunchbase_link)
        time.sleep(2.5)
        page_src = driver.page_source
        soup2 = BeautifulSoup(page_src,'html.parser')
        driver.quit()
        em1 = soup2.find_all('span',class_='ng-star-inserted')

        email = ''
        for elem in em1:
            strng = str(elem.text)
            if '@' in strng:
                email = strng
                break
        
        company_emails.append(email)

    else:
        company_emails.append('NA')

    x+=1
    if x==10:
        break



#Creates a list of company abstracts
company_abstracts = []
x=1
for link in company_links:
    page1 = requests.get(link)
    soup1 = BeautifulSoup(page1.content,'html.parser')
    abstract = soup1.find('p',class_='pre-line')
    company_abstracts.append(abstract.text)
    print(x,end=',')
    x+=1

#Creates a CSV
dictionary = {"Company Name":company_names_notags,"One-liner":company_descriptions_notags,"Abstract":company_abstracts,"Email":company_emails}

dataframe = pd.DataFrame(dictionary)

dataframe.to_csv('webscraperv3.csv')

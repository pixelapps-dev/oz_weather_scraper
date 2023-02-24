# %%
import pandas as pd 
import os 
import requests

import time 

import datetime
import pytz

# %%

# from selenium import webdriver 
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

# chrome_options = Options()
# chrome_options.add_argument("--headless")

# driver = webdriver.Firefox(options=chrome_options)

# %%

today = datetime.datetime.now()
scrape_date_stemmo = today.astimezone(pytz.timezone("Australia/Brisbane")).strftime('%Y%m%d')
scrape_hour = today.astimezone(pytz.timezone("Australia/Brisbane")).strftime('%H')

# %%


def dumper(path, name, frame):
    with open(f'{path}/{name}.csv', 'w') as f:
        frame.to_csv(f, index=False, header=True)

def rand_delay(num):
  import random 
  import time 
  rando = random.random() * num
#   print(rando)
  time.sleep(rando)

def if_no_fold_create(pathos, to_check):
    if pathos[-1] != '/':
        pathos += '/'

    folds = os.listdir(pathos)

    if to_check not in folds:
        os.mkdir(f"{pathos}{to_check}")
    # print(folds)


# %%

def scraper(stem, out_path, combo_path, urlo):

    print("## Starting: ", stem)

    # rand_delay(10)

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(urlo, headers=headers)


    print("R status: ", r.status_code)
    tabs = pd.read_html(r.text)[1:]

    # driver.get(urlo)

    time.sleep(2)

    # tabs = pd.read_html(driver.page_source)
    # print("Num tabs: ", len(tabs))


    if_no_fold_create('data/raw', scrape_date_stemmo)


    day_counter = 0

    listo = []

    for i in range(0, len(tabs)):

        # if tabs[i].columns.tolist() == ['Time (AEDT)', 'Temp (°C)', 'Feels Like (°C)', 'Humidity(%)', 'Wind Direction', 'Wind Speed (km/h) (knots)', 
        #                                 'Wind Gust (km/h) (knots)', 'Pressure (hPa)', 'Rainfall since 9 am (mm)']:

        if  'Temp (°C)' in tabs[i].columns.tolist():

            tabbo = tabs[i]
            'Time (AEDT)', 'Temp (°C)', 'Feels Like (°C)', 'Humidity(%)', 'Wind Direction', 
            'Wind Speed (km/h) (knots)', 'Wind Gust (km/h) (knots)', 
            'Pressure (hPa)', 'Rainfall since 9 am (mm)'

            inter_date = today  - datetime.timedelta(days=day_counter)
            inter_date_format = inter_date.astimezone(pytz.timezone("Australia/Brisbane")).strftime('%Y-%m-%d')

            tabbo['Date'] = inter_date_format

            # print(inter_date_format)

            dumper(f"{out_path}/{scrape_date_stemmo}", f"{stem}_{scrape_hour}_{day_counter}", tabbo)  
            listo.append(tabbo)  


            cat = pd.concat(listo)

            if os.path.isfile(f"{combo_path}/{stem}"):
                old = pd.read_csv(f"{combo_path}/{stem}")
                cat = pd.concat[old, cat]
                cat.drop_duplicates(subset=['Time (AEDT)', 'Date'], inplace=True)

            
            dumper(combo_path, stem, cat)

            day_counter += 1
        # else:
        #     print(tabs[i].columns.tolist())
        #     print("Didn't work?")
        #     continue



scraper("Sydney", 'data/raw','data',  'http://www.bom.gov.au/places/nsw/turramurra/observations/sydney---observatory-hill/')

scraper("Melbourne", 'data/raw','data',  'http://www.bom.gov.au/places/vic/melbourne/observations/melbourne-(olympic-park)/')

scraper("Brisbane", 'data/raw','data',  'http://www.bom.gov.au/places/qld/brisbane/observations/brisbane/')

scraper("Perth", 'data/raw','data',  'http://www.bom.gov.au/places/wa/perth/observations/perth/')

scraper("Adelaide", 'data/raw','data',  'http://www.bom.gov.au/places/sa/adelaide/observations/adelaide-(west-terrace----ngayirdapira)/')

scraper("Hobart", 'data/raw','data',  'http://www.bom.gov.au/places/tas/hobart/observations/hobart/')

scraper("Canberra", 'data/raw','data',  'http://www.bom.gov.au/places/act/canberra/observations/canberra/')

scraper("Darwin", 'data/raw','data',  'http://www.bom.gov.au/places/nt/darwin/')

# driver.quit()


# %%




# %%

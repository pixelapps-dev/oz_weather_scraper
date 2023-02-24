# %%
import pandas as pd 
import os 
import requests

import datetime
import pytz

# %%

today = datetime.datetime.now()
scrape_date_stemmo = today.astimezone(pytz.timezone("Australia/Brisbane")).strftime('%Y%m%d')

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

    rand_delay(10)

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(urlo, headers=headers)

    print("R status: ", r.status_code)


    if_no_fold_create('input/data/raw', scrape_date_stemmo)

    tabs = pd.read_html(r.text)[1:]

    listo = []

    for i in range(1, len(tabs)):
        
        tabbo = tabs[i]
        'Time (AEDT)', 'Temp (°C)', 'Feels Like (°C)', 'Humidity(%)', 'Wind Direction', 
        'Wind Speed (km/h) (knots)', 'Wind Gust (km/h) (knots)', 
        'Pressure (hPa)', 'Rainfall since 9 am (mm)'

        inter_date = today  - datetime.timedelta(days=i)
        inter_date_format = inter_date.astimezone(pytz.timezone("Australia/Brisbane")).strftime('%Y-%m-%d')

        tabbo['Date'] = inter_date_format

        # pp(tabbo)
        # print(i)
        # print(inter_date.strftime('%Y-%m-%d'))


        dumper(f"{out_path}/{scrape_date_stemmo}", f"{stem}_{i}", tabbo)  
        listo.append(tabbo)  


    cat = pd.concat(listo)

    if os.path.isfile(f"{combo_path}/{stem}"):
        old = pd.read_csv(f"{combo_path}/{stem}")
        cat = pd.concat[old, cat]
        cat.drop_duplicates(subset=['Time (AEDT)', 'Date'], inplace=True)

       
    dumper(combo_path, stem, cat)




scraper("Sydney", 'input/data/raw','input/data',  'http://www.bom.gov.au/places/nsw/turramurra/observations/sydney---observatory-hill/')

scraper("Melbourne", 'input/data/raw','input/data',  'http://www.bom.gov.au/places/vic/melbourne/observations/melbourne-(olympic-park)/')

scraper("Brisbane", 'input/data/raw','input/data',  'http://www.bom.gov.au/places/qld/brisbane/observations/brisbane/')

scraper("Perth", 'input/data/raw','input/data',  'http://www.bom.gov.au/places/wa/perth/observations/perth/')

scraper("Adelaide", 'input/data/raw','input/data',  'http://www.bom.gov.au/places/sa/adelaide/observations/adelaide-(west-terrace----ngayirdapira)/')

scraper("Hobart", 'input/data/raw','input/data',  'http://www.bom.gov.au/places/tas/hobart/observations/hobart/')

scraper("Canberra", 'input/data/raw','input/data',  'http://www.bom.gov.au/places/act/canberra/observations/canberra/')

scraper("Darwin", 'input/data/raw','input/data',  'http://www.bom.gov.au/places/nt/darwin/')




# %%




# %%

# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 09:13:32 2017

@author: Passanova
This script updates the database with the actual currency exchange rate
It can be run by doing python bnb_currency_parser.py
"""
from urllib.request import urlopen
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
import pandas as pd

contenturl = "http://www.bnb.bg/Statistics/StExternalSector/StExchangeRates/StERForeignCurrencies/"
soup = BeautifulSoup(urlopen(contenturl).read(), "lxml")

data = []
table = soup.find('table', attrs={'class':'table'})
table_body = table.find('tbody')


rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols] # Extract the text from the elements
    data.append([ele for ele in cols if ele]) # Exclude empty values
    
del data[-1] # Delete last element as not relevant

df = pd.DataFrame(data)
df.columns = ['Наименование', 'Код', 'За_единица', 'Лева', 'Обратен_курс']
df = df.set_index('Наименование', inplace=False)

engine = create_engine('postgresql://***:***@46.101.0.188/currency')
df.to_sql('calculator_currency', engine, if_exists='replace')

# print(df)

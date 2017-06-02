from urllib.request import urlopen
from bs4 import BeautifulSoup
from .models import Currency


def parser():
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
    data[-1].append('0')

    Currency.objects.all().delete()

    for i in data:
        Currency.objects.create(Наименование=i[0], Код=i[1], За_единица=i[2], Лева=i[3], Обратен_курс=i[4])

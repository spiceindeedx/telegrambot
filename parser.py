import requests
from bs4 import BeautifulSoup as bs

def update_binance():
    r = requests.get("https://www.binance.com/en/markets")
    soup = bs(r.text,"html.parser")
    tables_crypto = soup.find_all('div',class_="css-vlibs4")

    dict_tables = {}


    for i in range(len(tables_crypto)):
        abriviate = tables_crypto[i].find("div",class_="css-y492if").text
        full_name = tables_crypto[i].find("div",class_="css-74g683").text
        price = tables_crypto[i].find("div",class_="css-ydcgk2").text
    
        dict_tables[abriviate] = (full_name,price)
    

    return dict_tables

print(update_binance())









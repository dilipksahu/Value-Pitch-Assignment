from helium import *
from bs4 import BeautifulSoup
import pandas as pd

quotesdata = []

def request(x):
    url = f"http://quotes.toscrape.com/js/page/{x}/"
    browser = start_chrome(url, headless=True)
    soup = BeautifulSoup(browser.page_source, features='html.parser') 
    return soup.find_all('div',{'class':'quote'})

def parse(quotes):
    for item in quotes:
        quote = item.find('span',class_='text').text
        auther = item.find('small',class_='author').text
        # print(quote,auther)
        data = {
            'quote':quote,
            'auther':auther
        }
        quotesdata.append(data)

def output():
    df = pd.DataFrame(quotesdata)
    df.to_csv('quotesdata.csv',index=False)
    print("Saved to csv")

x = 1
while True:
    print(f"Getting page: {x}")
    quotes = request(x)
    x += 1
    if len(quotes) != 0:
        parse(quotes)
    else:
        break

output()
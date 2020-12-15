from requests_html import HTMLSession
import pandas as pd
import time

# url = "https://www.beerwulf.com/en-gb/c/all-beers?catalogCode=Beer_1&routeQuery=all-beers&page=1"

s = HTMLSession()
drinkslist = []

def request(url):
    r = s.get(url)
    r.html.render(sleep=3)
    return r.html.xpath('//*[@id="product-items-container"]', first=True)

def parse(products):
    for item in products.absolute_links:
        r = s.get(item)
        name = r.html.find('div.product-detail-info-title',first=True).text
        subtext = r.html.find('div.product-subtext',first=True).text
        price = r.html.find('span.price',first=True).text
        try:
            ratting = r.html.find('span.label-stars',first=True).text
        except AttributeError:
            ratting = "None"
        if r.html.find('div.add-to-cart-container'):
            stock = "in-stock"
        else:
            stock = "out-of-stock"
        # print(name,subtext,price,ratting,stock)

        drink = {
            'name': name,
            'subtext': subtext,
            'price': price,
            'ratting': ratting,
            'stock': stock
        }
        
        drinkslist.append(drink)

def output():
    df = pd.DataFrame(drinkslist)
    df.to_csv('drinkdemo.csv',index=False)
    

x = 1

while True:
    try:
        products = request(f"https://www.beerwulf.com/en-gb/c/all-beers?catalogCode=Beer_1&routeQuery=all-beers&page={x}")
        print(f"Getting items from page: {x}")
        parse(products)
        print("Total items: ",len(drinkslist))
        x = x + 1
        time.sleep(2)
    except:
        print("NO more items...!")
        break

output()
from requests_html import HTMLSession

s = HTMLSession()

asins = ('B08L8DV7BX','B08L8BJ9VC','B07JG7DS1T','B08L8C1NJ3')


for asin in asins:
    r = s.get(f"https://www.amazon.in/dp/{asin}")
    r.html.render(sleep=5)
    print(r.status_code)
    price = r.html.find('#priceblock_ourprice')[0].text.replace('₹','').replace(',','')
    title = r.html.find("#productTitle")[0].text.strip()
    print(title,price)

    
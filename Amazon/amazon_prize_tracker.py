from requests_html import HTMLSession

s = HTMLSession()

r = s.get("https://www.amazon.in/dp/B01LZKSVRB")

r.html.render(sleep=3)

price = r.html.find("@currencyINR")[0].text

print(price)
import requests
import json
import pandas as pd

url = "https://api.afl.com.au/statspro/playersStats/seasons/CD_S2020014"

payload={}
headers = {
  'authority': 'api.afl.com.au',
  'accept': 'application/json',
  'x-media-mis-token': 'eeb2c3fa270583ca0633a1c373807257',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
  'content-type': 'application/x-www-form-urlencoded',
  'origin': 'https://www.afl.com.au',
  'sec-fetch-site': 'same-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.afl.com.au/',
  'accept-language': 'en-IN,en;q=0.9',
  'if-none-match': 'W/"b90ae035c260c0e951ce3758f13e845d"',
  'Cookie': 'JSESSIONID=33F1595EEC0F6D58BF1342C4B547BB77'
}

r = requests.get( url, headers=headers)

playersdata = r.json()

df = pd.json_normalize(playersdata.get('players'))
print(df.shape)

df.to_csv('playersdata.csv', index=False)
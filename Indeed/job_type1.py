import requests
from bs4 import BeautifulSoup

url = "https://in.indeed.com/jobs?q=data+scientist&l="

r = requests.get(url).text
soup = BeautifulSoup(r, 'lxml')

jobs = soup.find(class_='result')
job_title = jobs.h2.a.text()
print(job_title)
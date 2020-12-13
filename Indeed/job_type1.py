import requests
from bs4 import BeautifulSoup
import pandas as pd

jobdata = []

def request(x):
    url = f"https://in.indeed.com/jobs?q=data+scientist&fromage=last&start={x}"
    headers = {'User-Agent':'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, features='lxml')
    return soup.find_all('div',class_='jobsearch-SerpJobCard')

def parse(jobs):
    for job in jobs:
        title = job.find('a',class_='jobtitle').text.strip()
        company = job.find('span', class_='company').text.strip()
        try:
            ratting = job.find('span', 'ratingsContent').text.strip()
        except:
            ratting = "0.0"
        try:
            location = job.find('div', class_='location').text.strip()
        except:
            location = "None"
        summary = job.find('div', class_='summary').text.strip()
        # print(title,company,location,ratting,summary)
        jobdesciption = {
            'title':title,
            'company':company,
            'ratting':ratting,
            'location':location,
            'summary':summary
        }
        jobdata.append(jobdesciption)

def output():
    df = pd.DataFrame(jobdata)
    df.to_csv('jobdata.csv',index=False)
    print("saved to csv file")


x = 0
while x <= 40:
    print(f"Getting Page = {x}")
    jobs = request(x)
    x = x + 10
    if len(jobs) != 0:
        parse(jobs)
    else:
        break

print("Process completed Jobs Extracted",len(jobdata))
output()



import scrapy
import json

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    start_urls = ['https://curiositystream.com/categories']

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-IN,en;q=0.9",
        "origin": "https://curiositystream.com",
        "referer": "https://curiositystream.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "x-4k-capable": "0",
        "x-api-version": "v3",
        "x-client-version": "v2.44.1-1-g807f97af9",
        "x-platform": "web",
        "x-session-token": "7c0470e5ac4a8e60e7316d28b91c1e9a45bbc6d9"
    }


    def parse(self, response):
        url = "https://api.curiositystream.com/v1/categories/"

        request = scrapy.Request(url, callback=self.parse_api, headers=self.headers)

        yield request

    def parse_api(self, response):
        raw_data = response.body
        resp = json.loads(raw_data)
        
        movies = resp.get('data')
        for cat in movies:
            for sub in cat['subcategories']:
                yield {
                    'category': cat.get('name'),
                    'image_label': cat.get('image_label'),
                    'sub-category': sub.get('name'),
                    'image_url': sub.get('image_url'),
                    'header_url': sub.get('header_url'),
                    'background_url': sub.get('background_url')
                }

        
                    
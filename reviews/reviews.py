from selectorlib import Extractor
import requests 
import json 
from time import sleep
import csv
from dateutil import parser as dateparser
from fake_useragent import UserAgent

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('reviews/selectors.yml')

def scrape(url):  
    ua = UserAgent()

    headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': ua.random,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s"%url)
    r = requests.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
        return None
    # Pass the HTML of the page and create 
    return e.extract(r.text)

# product_data = []
# get the ASIN code from url text
with open("reviews/review_urls.csv",'r') as urllist, open('reviews/review_data.csv','w') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["ASIN","title","content","date","variant","images","verified","author","rating","product","url"],quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for url in urllist.readlines():
        try:
            data = scrape(url)  
        except:
            continue
        if data:
            try:
                for r in data['reviews']:
                    r['ASIN'] = url.split('/')[5]
                    r["product"] = data["product_title"]
                    r['url'] = url
                    if 'verified' in r:
                        try:
                            if 'Verified Purchase' in r['verified']:
                                r['verified'] = 'Yes'
                            else:
                                r['verified'] = 'No'
                        except:
                            continue

                    r['rating'] = r['rating'].split(' out of')[0]
                    date_posted = r['date'].split('on ')[-1]
                    r['date'] = dateparser.parse(date_posted).strftime('%d %b %Y')
                    try:
                        writer.writerow(r)
                    except:
                        continue
                sleep(1)
            except:
                continue
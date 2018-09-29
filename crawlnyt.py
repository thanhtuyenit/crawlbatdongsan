from nytimesarticle import articleAPI
from bs4 import BeautifulSoup
import csv
import requests

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36'}

api = articleAPI('578de830956d4362b3d25df7ad69043b')
def parse_articles(articles):
    news = []
    news.append(['ID','Headline','Date','Url','Source','Content'])
    for i in articles['response']['docs']:
        id = i['_id']
        headline = i['headline']['main']
        date = i['pub_date'][0:10] # cutting time of day.
        source = i['source']
       
        url = i['web_url']
        r=requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        results = soup.select('p[class*="e2kc3sl0"]')
        details = ''
        for result in results:
            t = result.getText()
            details=details+t
        news.append([id,headline,date,url,source,details])
    return(news)

def get_articles(query):
 with open('ufonews.csv','w', newline='') as f_output:
    for i in range(1,100): #NYT limits pager to first 100 pages. But rarely will you find over 100 pages of results anyway.
        articles = api.search(q = query,begin_date = 20001010 ,page=i)
        p = parse_articles(articles)
        csv_output = csv.writer(f_output)
        csv_output.writerows(p)
p =get_articles('U.F.O')
    
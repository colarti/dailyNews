import os
import requests
import json
# import time       #option 1
from sendMessage import send_message
from datetime import datetime, timedelta #option 2

API_KEY = '6a7c75fa90b540bf90732f5cd854e822'

topic = 'tesla'
# date = time.strftime("%Y-%m-%d")  #option 1
date = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d') #option 2
# date = '2023-12-15'

site = f'https://newsapi.org/v2/everything?q={topic}&from={date}&sortBy=publishedAt&language=en&apiKey=6a7c75fa90b540bf90732f5cd854e822'

data = requests.get(url=site)
print(f'DATA:{data.text}')
content = data.json()


status = f'''\
Subject: {topic.title()} News for {date}
'''
cnt = 0
for idx, article in enumerate(content["articles"][:20]):    #the first 20 articles
    try:
        if article["title"] is None:
            continue

        if "remove" in article["title"].lower():
            continue

        status += f'''
    {cnt+1}. {article["title"]}
    \t{article["description"]}
    \t{article["url"]} 
    '''
        cnt+=1
    except UnicodeError:
        continue

status = status.encode('utf-8')

print(status)
# send_message(status)
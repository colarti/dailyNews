import os
import requests
import json
import time
from sendMessage import send_message


API_KEY = '6a7c75fa90b540bf90732f5cd854e822'

topic = 'war'
date = time.strftime("%Y-%m-%d")

site = f'https://newsapi.org/v2/everything?q={topic}&from={date}&sortBy=publishedAt&apiKey=6a7c75fa90b540bf90732f5cd854e822'

data = requests.get(url=site)
content = data.json()


status = f'''\
Subject: {topic.title()} News for {date}
'''
cnt = 0
for idx, article in enumerate(content["articles"]):
    # print(article, '\n')
    # print(f'{idx+1}. {article["title"]}\n')
    # print(f'\t{article["description"]} \n')

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
send_message(status)
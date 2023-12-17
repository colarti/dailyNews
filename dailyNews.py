import os
import requests
import json


API_KEY = '6a7c75fa90b540bf90732f5cd854e822'

site = 'https://newsapi.org/v2/everything?q=tesla&from=2023-11-17&sortBy=publishedAt&apiKey=6a7c75fa90b540bf90732f5cd854e822'

data = requests.get(url=site)
content = data.text




print(f'\n\n{content}')
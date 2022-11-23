import requests
import json
import feedparser
from nltk import SnowballStemmer
import smtplib
import ssl
from email.message import EmailMessage


API_Key = 'pub_13627bd13bba18cfe272936ddfc37064fed1f'
Base_URL ='https://newsdata.io/api/1/sources?apikey=pub_13627bd13bba18cfe272936ddfc37064fed1f&category=sports'

response = requests.get(Base_URL)

if response.status_code==404:
    print('page not found')
if response.status_code==400:
    print('bad request')
elif response.status_code==200:
    data = response.json()
    results = data['results'][1]['description']
    category = data['results'][1]['category']
    language = data['results'][1]['language']
    country = data['results'][1]['country']
    The_news_content = data['results'][1]['url']

    print('News: ',results)
    print('Category/categories: ',category)
    print('Language: ',language)
    print('Country: ',country)
    print('For detailed news, the link: ', The_news_content


The_Sender ='L26042001@gmail.com'
password ='zoimgpxarocokkkn'
The_receiver ='nourshehata30@gmail.com'

subject ='The news today'
entire_email = """
Be updated with the latest news, click on th link to open:
https://newsdata.io/tracker/news/fb0b81698d0321927a2bc1c9afa81830/68
"""

msg = EmailMessage()
msg['From'] = The_Sender
msg['To'] = The_receiver
msg['Subject'] = subject
msg.set_content(entire_email)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(The_Sender, password)
    smtp.sendmail(The_Sender, The_receiver, msg.as_string())


    


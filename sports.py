import requests

API_Key = '54cf92eac6mshab2523f8196bf3bp1fb653jsna321e8ceba8c'
URL ='https://rapidapi.com/api-sports/api/api-football-beta/'

Sport = input('what kind of sports?: ')
URL = URL + 'appid=' +API_Key + '&q=' + Sport
response = requests.get(URL)
response_dict = response.json()

Sports = response_dict['Sports']
if response.status_code == 200:
    print(Sports)
else:
    print('error occurred')

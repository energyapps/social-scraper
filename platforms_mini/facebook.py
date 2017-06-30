import csv
import requests
import json
from BeautifulSoup import BeautifulSoup

# must update this every few hours/whenever its run. 
token = 'EAADqjjNdGm4BAGfKBgbE0Rt8ZB61xbZCNqz8i9bqbQD00GZA6kVbZAdFlovwhM6TV01tksySluQ0PVezRaSCwOdlA6ZClJ8fUxErQZAncgPtTu54XtBDrdknBCRNQGsrZC3uSXfrxcWZBW4LqdZAYQZAVwjG2v3e18r4XGsewIHfam1SN6vMr5ZBuk9'

handle = 'energysavergov'

url = 'https://graph.facebook.com/v2.8/'+ handle +'/?fields=fan_count&access_token=' + token

response = requests.get(url)
data = response.content
data = json.loads(data)

# soup = BeautifulSoup(html)
# likes = soup.find('a', attrs={'data-nav': 'followers'}).find('span', attrs={'class':'ProfileNav-value'}).text

# print likes
print data['fan_count']
import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://twitter.com/justinbieber'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
followers = soup.find('a', attrs={'data-nav': 'followers'}).find('span', attrs={'class':'ProfileNav-value'}).text

print followers


searchTerm = 'followers_count&quot;:'

followerIndex = html.find(searchTerm) + len(searchTerm)
followerIndexEnd = followerIndex + 50
followersString = html[followerIndex:followerIndexEnd]
followerCut = followersString.find(',&quot;')
followers = followersString[:followerCut]
print followers
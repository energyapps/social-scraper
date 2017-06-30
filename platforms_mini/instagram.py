import csv
import requests
# from BeautifulSoup import BeautifulSoup

handle = 'energy'

url = 'https://www.instagram.com/' + handle
response = requests.get(url)
html = response.content

searchTerm = 'followed_by": {"count": '

followerIndex = html.find(searchTerm) + len(searchTerm)
followerIndexEnd = followerIndex + 12
followersString = html[followerIndex:followerIndexEnd]
followerCut = followersString.find('}')
followers = followersString[:followerCut]
print followers
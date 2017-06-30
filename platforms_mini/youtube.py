import csv
import requests

handle = 'USdepartmentofenergy'

url = 'https://www.youtube.com/user/' + handle

response = requests.get(url)
html = response.content

searchTerm = 'subscribers">'

subscriberIndex = html.find(searchTerm) + len(searchTerm)
subscriberIndexEnd = subscriberIndex + 100
subscribersString = html[subscriberIndex:subscriberIndexEnd]
subscriberCut = subscribersString.find('</span')
subscribers = subscribersString[:subscriberCut]
print subscribers
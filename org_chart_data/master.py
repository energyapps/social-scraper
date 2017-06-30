import csv
import requests
from BeautifulSoup import BeautifulSoup
import json

with open('social_handles.csv', 'rb') as f:
# with open('/home/ec2-user/org_chart_data/social_handles.csv', 'rb') as f:	
    reader = csv.reader(f)
    next(reader)
    your_list = list(reader)

# print your_list

# define the function blocks
def facebook(handle):
	if handle != "":		
		# # must update this every few hours/whenever its run. 
		# token = 'EAADqjjNdGm4BAF9jJ0ODpTzBnBH7xLIV4y6DSyEkjEESv8B9W48ZCZCRLtZCZCuKPK662yFeGkj7Hgp9ZBCSekhKTACXNk2clTvg5hEY8MhRBUqreU7A6syzElfOoggwXTjVyyFuSbZBtZB38ZCfrTdUvbwKCFeney4SsrBwSG2OMEXoJefmDqKwVIi5fLVYpYkZD'	

		# url = 'https://graph.facebook.com/v2.8/'+ handle +'/?fields=fan_count&access_token=' + token

		# response = requests.get(url)
		# data = response.content
		# data = json.loads(data)

		# return data['fan_count']
		return ""
	else:
		return ""
	
def twitter(handle):
	if handle != "":		
		url = 'https://twitter.com/' + handle
		response = requests.get(url)
		html = response.content

		searchTerm = 'followers_count&quot;:'

		followerIndex = html.find(searchTerm) + len(searchTerm)
		followerIndexEnd = followerIndex + 50
		followersString = html[followerIndex:followerIndexEnd]
		followerCut = followersString.find(',&quot;')
		followers = followersString[:followerCut]
		return followers
	else:
		return ""
	
def instagram(handle):
	if handle != "":
		url = 'https://www.instagram.com/' + handle
		response = requests.get(url)
		html = response.content

		searchTerm = 'followed_by": {"count": '

		followerIndex = html.find(searchTerm) + len(searchTerm)
		followerIndexEnd = followerIndex + 12
		followersString = html[followerIndex:followerIndexEnd]
		followerCut = followersString.find('}')
		followers = followersString[:followerCut]
		return followers
	else:
		return ""	
	
def youtube(handle):
	if handle != "":	
		url = 'https://www.youtube.com/user/' + handle

		response = requests.get(url)
		html = response.content

		searchTerm = 'subscribers">'

		subscriberIndex = html.find(searchTerm) + len(searchTerm)
		subscriberIndexEnd = subscriberIndex + 100
		subscribersString = html[subscriberIndex:subscriberIndexEnd]
		subscriberCut = subscribersString.find('</span')
		subscribers = subscribersString[:subscriberCut]
		return subscribers
	else:
		return ""

	# possible future functions to scrape followers, likes, etc from other platforms. 
def medium(handle):
	print "not applicable for medium"
	
def pinterest(handle):
	print "not applicable for pinterest"
	
def storify(handle):
	print "not applicable for storify"
	
def linkedin(handle):
	print "not applicable for linkedin"
	
def google(handle):
	print "not applicable for google"
	
def vimeo(handle):
	print "not applicable for vimeo"
	
def flickr(handle):
	print "not applicable for flickr"
	
def slideshare(handle):
	print "not applicable for slideshare"
 	

# map the inputs to the function blocks
options = {1 : facebook,
		2 : twitter,
		3 : instagram,
		4 : youtube,
		5 : medium,
		6 : pinterest,
		7 : storify,
		8 : linkedin,
		9 : google,
		10 : vimeo,
		11 : flickr,
		12 : slideshare
		}

# options[1]()

# Gather the data from the above defined functions and put it in a file

list_of_rows = []
for row in your_list:	
	index = -1
	list_of_cells = []
	for cell in row:
		if index <= 0:
			list_of_cells.append(cell)
		elif index >0 and index <5:			
			list_of_cells.append(options[index](cell)) 
		else:
			list_of_cells.append("")
		index +=1
	list_of_rows.append(list_of_cells)
		# print y
	print list_of_cells

# outfile = open("/home/ec2-user/org_chart_data/all_social_data.csv", "wb")
outfile = open("./all_social_data.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["type","zid","facebook","twitter","instagram","youtube","medium","pinterest","storify","linkedin","google","vimeo","flickr","slideshare"])
writer.writerows(list_of_rows)
import csv
import requests
import json
from time import gmtime, strftime
time = strftime("%d %b %Y %H:%M:%S")
print time

with open('social_data.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

# print your_list

# define the function blocks
def facebook(handle):
	# if handle != "":		
	# 	# must update this every few hours/whenever its run. 
	# 	token = 'EAADqjjNdGm4BAGfKBgbE0Rt8ZB61xbZCNqz8i9bqbQD00GZA6kVbZAdFlovwhM6TV01tksySluQ0PVezRaSCwOdlA6ZClJ8fUxErQZAncgPtTu54XtBDrdknBCRNQGsrZC3uSXfrxcWZBW4LqdZAYQZAVwjG2v3e18r4XGsewIHfam1SN6vMr5ZBuk9'	

	# 	url = 'https://graph.facebook.com/v2.8/'+ handle +'/?fields=fan_count&access_token=' + token

	# 	response = requests.get(url)
	# 	data = response.content
	# 	data = json.loads(data)

	# 	return data['fan_count']
	# 	return ""
	# else:
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

# DOEfacebook = facebook()
DOEtwitter = twitter("energy")
DOEinstagram = instagram("energy")
DOEyoutube = youtube("USdepartmentofenergy")
# SECfacebook = facebook()
SECtwitter = twitter("secretaryperry")
# SECinstagram = instagram()
# SECyoutube = youtube()

your_list[0].append(time)
your_list[2].append(DOEtwitter)
your_list[3].append(DOEinstagram)
your_list[4].append(DOEyoutube)
your_list[6].append(SECtwitter)


# for row in your_list:

	# row.append("test")
	# print row
	# index = -1
	# list_of_cells = []
	# for cell in row:
	# 	if index <= 0:
	# 		list_of_cells.append(cell)
	# 	elif index >0 and index <5:
	# 		list_of_cells.append(options[index](cell)) 
	# 	else:
	# 		list_of_cells.append("")
	# 	index +=1
	# list_of_rows.append(list_of_cells)
	# 	# print y
	# print list_of_cells


outfile = open("./social_data_temp.csv", "wb")
writer = csv.writer(outfile)
# writer.writerow(["type","zid","facebook","twitter","instagram","youtube","medium","pinterest","storify","linkedin","google","vimeo","flickr","slideshare"])
writer.writerows(your_list)
## About
The purpose of these scripts is to collect and organize data that shows the various size of Department of Energy social media audiences by scraping social media follower data from twitter, instagram, youtube, and (if done with a temporary API key) facebook. It can be expanded to include other platforms in the future. 

There are two scripts that are housed here. Both of them can be run locally to see how they work. They are:

1. Org Chart Data
	- Collects the data for the [DOE Social Media Org Chart](https://energyapps.github.io/social)
	- Ideally will collect data either once a day or once a week. **NOTE** does not need to collect data hourly. 
	- Resulting data should look like [this](https://s3-us-west-2.amazonaws.com/energy2/social/all_social_data.csv).
2. Hourly Follower Count
	- Collects the data for the charts found at https://energyapps.github.io/social/followers and the matrix pages. 
	- Collects data hourly in order to track the growth of audience over time. 
	- Resulting data should look like [this](https://s3-us-west-2.amazonaws.com/energy2/social/social_data.csv).

**The goal of this repo is get each of these scripts onto a Jenkin's Job and served onto `https://energy.gov/api/social-media/` with read access allowed via CORS rules to `energyapps.github.io/social`. 

## Dependencies 
* Some of the python scripts make use of Beautiful Soup. The other packages it uses are csv, requests, json, and time.

## Directory

* org_chart_data/
	- master.py
		- This is the script that collects follower data from instagram, twitter, youtube and facebook. 
		- Note, facebook has been turned off in order to prevent it from breaking. Please refer to the "known problems" section below for more information.
		- NOTE: While this doesn't appear to work locally for me at the moment, I have confirmed that it works on the EC2 instance without any changes.  
	- social_handles.csv
		- This csv is a list of the social media handles that you will scrape for follower data.
* hourly_follower_count/
	- followers-hourly.py
		- Collects follower numbers hourly for DOE twitter, DOE instagram, DOE youtube, and Secretary's twitter.
		- If you have other accounts to add, they can be easily added into the bottom section of the script. 
		- Appends the most recent data onto social_data.csv
		- **NOTE** the file paths in this currently are from the EC2 instance and would need to be updated to run either locally or on jenkins. 
	- social_data.csv
		- Ongoing tally of followers on the above listed accounts. Added to hourly. 
		- **NOTE** When you move from EC2 to Jenkins, be sure to grab the latest `social_data.csv` from the S3 bucket. Otherwise you will lose a lot of data. Find it at https://s3-us-west-2.amazonaws.com/energy2/social/social_data.csv
	- scraper.sh
		- this is the shell script that runs on the EC2 instance. It copies the previous data to an "old" file, as a backup. If the `followers-hourly.py` does not complete, it will not create the new `social_data.csv` file. This script will then revert to the previous data (by changing the name of `social_data_old.csv` back to `social_data.csv`. **There is probably a safer solution for error handling but it was beyond the scope of the initial build**

* platforms_mini/
	- Each individual social media platforms' test script, for scraping follower number. 



## Known Problems

### Facebook scraping
While it is possible to scrape facebook user data using the API that they provide through [developer tools](https://developers.facebook.com/tools/accesstoken/), it is more complicated than scraping a public facing website. You are required to use an [API key](https://developers.facebook.com/tools/accesstoken/), but, from what I could tell, it expires frequently. I'm sure there is a developer tool that allows for a "set it and forget" method, but at the time I left the job, I hadn't had time to find this solution. 

Therefore, this is why we do not track hourly facebook data in [Hourly Follower Count](https://energyapps.github.io/social/followers). Additionally, it has been turned off on [DOE Social Media Org Chart](https://energyapps.github.io/social/) but can be reinstated any time someone wants to figure out a latent option. 

### Error Handling
At the time there is no elegant solution for noticing if things are broken. There are a few fail-safe's built in but they could be much improved. 

[This ticket outlines what the needs are for scraping facebook with the API key]().

## To Do List
- write tickets for folks

- Add Secretary's instagram account (@secretaryperry)
- Add Energy Press Sec Twitter (@EnergyPressSec)
- Install all python packages on the script server. 
- Install and test both scripts on the script server. 
- Ensure that Ernie and Atiq are receiving regular updates that these are working/
- Find a way to make facebook numbers update automatically without having to manually insert a temporary API key into the script. 
- Ensure that `energy.gov/api/social-media` allows `energyapps.github.io/social` via favorable CORS rules. 

## Wish List
- Make Hourly Follower Count charts explorable to focus on specific time frames. 
- Fix Matrix diagrams
- figure out a way to have backup files.  

import praw
import pickle
import time
import os

# bot login info for local testing
# with open("login.properties", "r") as loginFile:
#     login_info = loginFile.readlines()

# Retrieve heroku env variables for deployment
login_info = [os.environ['REDDIT_USERNAME'], os.environ['REDDIT_PASSWORD']]

# removing new lines from username/password
login_info[0] = login_info[0].replace('\n', '')
login_info[1] = login_info[1].replace('\n', '')

# set up praw
r = praw.Reddit('christophiorbot')
r.login(login_info[0], login_info[1])

# USER="christophior"
# print "Sending message"
# r.send_message(USER, 'Test?', 'sup bro')
# print "Message sent"

# getting submissions from subreddit
subreddit = r.get_subreddit('aww')
submissions = subreddit.get_hot(limit=10)
for submission in submissions:
	print submission.title

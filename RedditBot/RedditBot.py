import praw
import pickle
import time

# bot login info
with open("login.properties", "r") as loginFile:
    login_info = loginFile.readlines()

# zeroing out login info
login_info[0] = login_info[0].replace('\n', '')
login_info[1] = login_info[1].replace('\n', '')

# set up praw
r = praw.Reddit('trollbot')
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

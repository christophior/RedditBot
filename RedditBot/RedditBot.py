import praw
import pickle
import time
import os

if __name__ == "__main__":

    print "starting RedditBot"

    # Retrieve heroku env variables for deployment
    # login_info = [os.environ['REDDIT_USERNAME'], os.environ['REDDIT_PASSWORD']]

    # bot login info for local testing
    # with open("login.properties", "r") as loginFile:
        # login_info = loginFile.readlines()

    # removing new lines from username/password
    # login_info[0] = login_info[0].replace('\n', '')
    # login_info[1] = login_info[1].replace('\n', '')

    # set up praw
    r = praw.Reddit('christophiorbot')
    r.login('christophiorbot', 'test')

    # USER="christophior"
    # print "Sending message"
    # r.send_message(USER, 'Test?', 'sup bro')
    # print "Message sent"

    # getting submissions from subreddit
    subreddit = r.get_subreddit('aww')
    submissions = subreddit.get_hot(limit=1)
    for submission in submissions:
        new_comment = submission.add_comment('rawr')
        print submission.title

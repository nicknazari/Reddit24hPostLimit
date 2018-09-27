# nick nazari
# sep 26 2018
# github: nicknazari
# reddit bot to prevent users from posting more than once every 24h
# or the same link more than once every 24h

# edit username and password 

import praw
import time
import config

reddit_client_id = config.client_id
reddit_client_secret = config.client_secret
reddit_user_agent = 'limit posts by link or user to once every 24h, a bot by u/InsideAnalysis Github: nicknazari'
reddit_username = config.username
reddit_password = config.password

reddit = praw.Reddit(client_id = reddit_client_id,
					 client_secret = reddit_client_secret,
					 user_agent = reddit_user_agent,
					 username = reddit_username,
					 password = reddit_password)

subToSearch = 'bottrials'

linkcooldown = []
authorcooldown = []

while True:
	for submission in reddit.subreddit(subToSearch).new(limit=5):
		url = submission.url
		author = submission.author
		if url in linkcooldown or author in authorcooldown:
			reddit.redditor(str(author)).message("Post Removed", "Hello, " + str(author) + "! Your post is being removed because you have either posted more than one time within the last 24 hours or the same link has been posted within this time. Please contact the moderators of this subreddit if you have any questions." + "\n\n^^this ^^bot ^^was ^^made ^^by ^^u/InsideAnalysis")
			submission.delete()
			time.sleep(2)
		else:
			linkcooldown.append(url)
			authorcooldown.append(author)
	time.sleep(2)
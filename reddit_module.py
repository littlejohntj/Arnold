#!/usr/bin/python

"""
Quickie Media - Reddit (Arnold 2.0)
"""

import time
import praw
import textwrap
from praw.models import MoreComments

def convert_time(datestring):
    timestamp = time.localtime(datestring)
    s = str(time.strftime("%Y-%m-%d %H:%M:%S", timestamp))
    return s

def getTimeAgo(stamp):
    length = time.time() - stamp
    if length > 3600*24:
        return '%d days ago' % int(length/(3600*24))
    elif length > 3600:
        return '%d hours ago' % int(length/3600)
    else:
        return '%d minutes ago' % int(length/60)

#print the top two comments
def top_two_comments(submission, divider):
	#sort the comments
	scores =[0,0]
	for comment in submission.comments:
		if not isinstance(comment, MoreComments):
			scores = scores+[comment.score]
	scores.sort(reverse=True)
	#print(scores)

	#find and store the top two comments
	#'comment[2]' is used for deciding whether to print the divider below
	comments = [0,0,0]
	for comment in submission.comments:
		if not isinstance(comment, MoreComments):
			if (comment.score==scores[0]):
				comments[0]=comment
			if (comment.score==scores[1]):
				comments[1]=comment

	#print the top two comments
	for i in range(0,2):
		if comments[i]!=0:
			comment=comments[i]
			timeAgo = str(getTimeAgo(comment.created_utc))
			preface = 'COMMENT (' + timeAgo + ', score = ' + str(comment.score) + "): "
			if len(preface)+len(comment.body) > len(divider):
				comment.body = textwrap.fill(preface+comment.body, len(divider))
			limit = 4*len(divider)
			if len(comment.body) > limit:
				#subtract '6' due to how textwrap adds newlines
				print(comment.body[:limit-6])
			else:
				print(comment.body)
			link = str(comment.permalink)
			if len(link) > len(divider):
				link = textwrap.fill(link, len(divider))
			print(link)
			if comments[i+1]!=0:
				print(divider)

#from pprint import pprint

#reddit = praw.Reddit(user_agent='arnold')
def print_timeline(reddit):
	submissions = reddit.subreddit('all').hot(limit = 3)

	for submission in submissions:
		#pprint(vars(submission)) #pretty prints all variables with their values
		#pprint(dir(submission))  #pretty prints all variables without their values

		header = str(submission.author) + " | "  + convert_time(submission.created_utc) + " | " + "Score: " \
		   	+ str(submission.score) + " | " + "# Comments: " + str(submission.num_comments) + " | "

		divider = ""
		for i in range(1, len(header)):
			divider = divider + "-"

		if len(submission.title) > len(divider):
			submission.title = textwrap.fill(submission.title, len(divider))

		print('REDDIT')
		print(divider)
		print(header)
		print(divider)
		print(submission.title)
		#print(divider)
		print(submission.url)
		print(divider)
		#comment out the next line, if the top two comments aren't desired
		top_two_comments(submission, divider)
		print(divider)
		print("\n")

	






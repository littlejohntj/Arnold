#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

import Image_ASCII
from InstagramAPI import InstagramAPI

def login(username, password):
	insta_api = InstagramAPI(username, password)
	insta_api.login()
	return insta_api

def create_users_from_tag(tag):
	InstagramAPI.tagFeed(tag)
	media_id = InstagramAPI.LastJson
	return [User(photo["user"]["username"]) for photo in media_id["items"]]

def username_is_free(username):
	InstagramAPI.searchUsername(username)
	result = InstagramAPI.LastJson
	return result["status"] == "fail"

def get_recent_posts(insta_api):
	insta_api.timelineFeed()
	for post in filter(lambda x: x.keep, [Post(item) for item in insta_api.LastJson['items']]):
		post.print_self()
	#return filter(lambda x: x.keep, [Post(item) for item in insta_api.LastJson['items']])

class Post:

	def __init__(self, json):
	  
		if 'code' in json:
			self.keep = True
			self.code = json['code']
			self.like_count = json['like_count']
			if json['caption'] is not None:
				self.caption = json['caption']['text']
			else:
				self.caption = ""
			self.user = json['user']['username']
			self.image_link = json['image_versions2']['candidates'][-1]['url'].split('?')[0]
			self.comment_count = len(json['comments'])

			
		else:
			self.keep = False

	def print_self(self):

		print '------------------------------------------------------------------------------------'
		print self.user, '|', 'Likes:', self.like_count, '|', 'Comments:', self.comment_count, '|'
		print '------------------------------------------------------------------------------------'
		print self.caption.encode('utf-8')
		print '------------------------------------------------------------------------------------'
		print Image_ASCII.image_to_ascii(self.image_link)
		print '------------------------------------------------------------------------------------'


class User:

	def __init__(self, username):
		self.username = username
		self.populate_self()

	def populate_self(self):
		InstagramAPI.searchUsername(self.username)
		user_info = InstagramAPI.LastJson
		self.follower_count = user_info["user"]["follower_count"]
		self.following_count = user_info["user"]["following_count"]
		print "populated new account"

'''
InstagramAPI = login("sxeteej", "fsuid889(")
posts = get_recent_posts(InstagramAPI)
for p in posts:
	p.print_self()
'''



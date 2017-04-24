from __future__ import print_function
from keys import *
import pprint
import requests
import urlparse
import getpass
import oauth2 as oauth
import twitter
import praw
from InstagramAPI import InstagramAPI

# Twitter
class Twitter_Auth():
    def __init__(self):
        self.consumer_key = twitter_consumer_key
        self.consumer_secret = twitter_consumer_secret
        self.request_token_url = 'https://api.twitter.com/oauth/request_token'
        self.access_token_url = 'https://api.twitter.com/oauth/access_token'
        self.authorize_url = 'https://api.twitter.com/oauth/authorize'
        self.request_token = self.get_request_token()

    def get_request_token(self):
        """Returns dict containing request oauth token and token secret"""
        self.consumer = oauth.Consumer(self.consumer_key, self.consumer_secret)
        self.client = oauth.Client(self.consumer)

        self.response, self.content = self.client.request(self.request_token_url, "GET")
        if self.response['status'] != '200':
            raise Exception("Invalid response %s." % self.response['status'])

        return dict(urlparse.parse_qsl(self.content))

    def get_authorized_user(self):
        """Returns ready to use api object with access token and user access token secret"""
        print("Authorize Arnold on your Twitter Account")
        print("--------------------------------------------------")
        print("Go to the following url in your browser to authorize Twitter access:")
        print("%s?oauth_token=%s" % (self.authorize_url, self.request_token['oauth_token']))
        print()
        self.oauth_verifier = raw_input("Please enter the authorization pin: ")

        self.user_token = oauth.Token(self.request_token['oauth_token'],
            self.request_token['oauth_token_secret'])

        self.user_token.set_verifier(self.oauth_verifier)
        self.client = oauth.Client(self.consumer, self.user_token)
        self.response, self.content = self.client.request(self.access_token_url, "POST")

        self.user_access_tokens = dict(urlparse.parse_qsl(self.content))

        # Create instance of Twitter API with proper authorized tokens
        api = twitter.Api(
            self.consumer_key,
            self.consumer_secret,
            self.user_access_tokens['oauth_token'],
            self.user_access_tokens['oauth_token_secret']
        )

        return api


#Instagram
class Instagram_Auth():
    def __init__(self):
        self.consumer_key= instagram_consumer_key
        self.consumer_secret= instagram_consumer_secret

    def get_authorized_user(self):
        '''Handles authorizing the user for Arnold'''
        print("Authorize Arnold on your Instagram Account")
        print("--------------------------------------------------")
        self.user_name = raw_input("Username: ")
        self.password=getpass.getpass("Password: ")

        # Create instance of Instagram API with proper login
        api = InstagramAPI(
            self.user_name,
            self.password
        )
        api.login()
        return api


#Reddit
class Reddit_Auth():
    def __init__(self):
        self.consumer_key=reddit_consumer_key
        self.consumer_secret=reddit_consumer_secret

    def get_authorized_user(self):
        '''Handles authorizing the user for Arnold by logging in'''
        print("Authorize Arnold on your Reddit Account")
        print("--------------------------------------------------")
        self.user_name = raw_input("Username: ")
        self.password=getpass.getpass("Password: ")


        # Create instance of Reddit API with proper authorized tokens and login
        api = praw.Reddit(
            client_id = self.consumer_key,
            client_secret = self.consumer_secret,
            password = self.password,
            user_agent="testscript for Arnold",
            username = self.user_name
        )

        return api



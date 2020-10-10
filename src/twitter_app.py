import socket
import sys
import requests
import requests_oauthlib
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Create .env file path
dotenv_path = join(dirname(__file__), '.env')
# load file from the path
load_dotenv(dotenv_path)


ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
my_auth = requests_oauthlib.OAuth1(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET)

def get_tweets():
	print('get tweets')
	url = 'https://stream.twitter.com/1.1/statuses/filter.json'
	query_data = [('language', 'en'), ('track','hospital')]
	query_url = url + '?' + '&'.join([str(t[0]) + '=' + str(t[1]) for t in query_data])
	print(query_url)
	response = requests.get(query_url, auth=my_auth, stream=True)
	# print(response)
	return response

if __name__ == "__main__":
	print('main function')
	tweets=get_tweets()
	print(tweets.status_code)
	for i in tweets.iter_lines():
		full_tweet = json.loads(i)
		tweet_text = full_tweet['text']
		print("Tweet Text: " + tweet_text)


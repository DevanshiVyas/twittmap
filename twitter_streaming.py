# -*- coding: utf-8 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from HTMLParser import HTMLParser
from elasticsearch import Elasticsearch, exceptions
import urllib3
urllib3.disable_warnings()

access_token = "705491955774595072-pIWKpOYm7iK8fzhqqLtv0h5ZlPNUl18"
access_token_secret = "BYaoKxaXl60rdcO98XpXzUKDmj6fefJQGrvDTdxKkqXuk"
consumer_key = "WuWtVBneDIFi8PetwWejZjw5C"
consumer_secret = "tCV2bjdlvFNowl8e9mwMYb4UrNj7LjXqpltERZZn3JZSOLfrsM"
keywordList = ['movies','sports','music','finance','technology','fashion','science','travel','health','cricket','india']

es = Elasticsearch()

def findCategory(text, keywordList):
    category = []
    for keyword in keywordList:
        if keyword in text:
            category.append(keyword)
    return category

class StdOutListener(StreamListener):
    def __init__(self):
        self.counter = 0
        self.limit = 500
    def on_data(self, data):
        if self.counter < self.limit:
            decoded = json.loads(HTMLParser().unescape(data))
            if decoded.get('coordinates',None) is not None:
                id = decoded['id']
                time = decoded.get('created_at','')
                text = decoded['text'].lower().encode('ascii','ignore').decode('ascii')
                coordinates = decoded.get('coordinates','').get('coordinates','')
                category = findCategory(text, keywordList)
                tweet = {'timestamp':time,'text':text,'coordinates':coordinates,'category':category}
                print "tweet", tweet
                res = es.index(index="faaltu", doc_type="tweet", id=id, body=tweet)
                self.counter += 1
                print 'Tweet Count# ' + `self.counter`
        else:
            twitterStream.disconnect()

    def on_error(self, status):
        print "error: ", status

if __name__ == '__main__':

    #This handles Twitter authentification and the connection to Twitter Streaming API
    while True:
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        twitterStream = Stream(auth, l)
        twitterStream.filter(track=['movies','sports','music','finance','technology','fashion','science','travel','health','cricket','india'])

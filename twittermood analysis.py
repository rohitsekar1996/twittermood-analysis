# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 15:38:50 2018

@author: rohit
"""
import tweepy
from textblob import TextBlob

consumer_key = 'PsCikMtznuKIEK4SXA6zMy0yP'
consumer_secret ='08qMdur199VsFFXIwyRLwgs5soJaz7gMboY5v4mWZDgwSwYcLC'

access_token = '775568863903842304-kqycajGfjXkBpaDK81ieBGf96r3wdEd'
access_token_secret= 'Wd0IybXk2Y4TO7NGTiBjzXzbUFgRnyZak6czV21W5zDdM'

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets = api.search('modi')

for tweet in public_tweets:
    print(tweet.text)
    analysis =TextBlob(tweet.text)
    print(analysis.sentiment)
    
    
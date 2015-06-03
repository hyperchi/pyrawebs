#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
import random
from random import randint
from time import sleep

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

def oauth_login(consumer_key, consumer_secret,access_key,access_secret):
  """Authenticate with twitter using OAuth"""
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  return tweepy.API(auth)

if __name__ == "__main__":
  api = oauth_login(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
  print "Authenticated as: %s" % api.me().screen_name

  l_tweets   = []
  l_targets  = []

  arg_tweets  = str(sys.argv[1])
  arg_target  = str(sys.argv[2])
  print arg_tweets
  print arg_target

  f_tweets     = open(arg_tweets,'r')
  f_targets  = open(arg_target,'r')

  s_tweets     = f_tweets.readlines()
  s_targets  = f_targets.readlines()
  

  # crear lista de targets
  for line in s_targets:
    l_targets.append(line.strip().decode('utf-8'))

  # crear lista de tweets
  for line in s_tweets:
    l_tweets.append(line.strip().decode('utf-8'))


  # crear y enviar tweets
  for tweet in l_tweets:
    actual_target = '@'
    for target in l_targets:
      tweet   = tweet.replace(actual_target, target)
      if target != '':
        actual_target = target
      print tweet
      
      try:
        api.update_status(status=tweet)
        espera = randint(4,20)
        time.sleep(espera)
        print 'espera: '+str(espera)+' segundos'
      except:
        print "Failed to tweet:", tweet
      
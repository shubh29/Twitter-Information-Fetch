# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:17:17 2015
@author: User
"""

from TwitterSearch import *

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Villanova', 'go cats']) # let's define all words we would like to have a look for
    tso.set_language('en')# we want to see tweets from english only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key ='7ovlnQDliiKXTkQSrVr5hKHgq',
        consumer_secret = 'WFTzfGhu8veWgm08rqywkJWR4lYXVZzGQOQ4Kb1MUElhezPCea',
        access_token = '3631252332-8Y6J9vXNlvGCvR4rNysCD5YtIk811NIWOYI16R6',
        access_token_secret = 'LrZiv6h8lyRU0L8vfHbFQKVUTmZr4jACpzU9ReAYKkG9B'
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
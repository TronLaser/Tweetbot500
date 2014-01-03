# This script relies on https://github.com/bear/python-twitter

# Written by TronLaser on GitHub
# Report bugs to github.com/tronlaser

import twitter
import ConfigParser
import time
from time import gmtime, strftime
import random

print ("Everything imported fine")

config = ConfigParser.ConfigParser()
config.read("config.ini")
consumer_key = config.get('login', 'consumer_key')
consumer_secret = config.get('login', 'consumer_secret')
access_token_key = config.get('login', 'access_token_key')
access_token_secret = config.get('login', 'access_token_secret')
debug = config.get('debug', 'debug')

print ("Config file found and read")
print ("Connecting to the API")

api = twitter.Api(consumer_key,consumer_secret,access_token_key,access_token_secret)
test = api.VerifyCredentials()

if test == "":
    print ("Connection failed. Check your details")
else:
    print ("Connection successful!")

print ("READY!")

# Below is the data for my tweetbot
# Erase the stuff below and make what you want

oldtweet = 'a' # I'm probably doing this part horribly wrong
oldtweet = 'b' # If anyone wants to point out something wrong please do

listoftweets = ['No', 'Nope', 'Negative', 'Nah', 'Not yet', 'Still no', 'Nyet', 'Nein', 'Nerp'] # The list of possible tweets

def choose(): # This makes sure we don't tweet the same thing twice. If we do the API will get angry at us. 
    global oldtweet
    global tweet
    tweet = random.choice(listoftweets)
    if oldtweet == tweet:
        print ("Same tweet as last. Reselecting.")
        choose()
    else:
        oldtweet = tweet
        post()

def post(): # This will post the message to Twitter
    global tweet
    status = api.PostUpdate(tweet)
    print status.text

# If we want to test the program without waiting, setting debug to 1 in the config will cause it to tweet upon loading
if debug == ("1"):
    print ("Debug ENABLED!")
    choose()
else:
    print ("Debug disabled")

while True: # This is the main loop for the program
    ctime = strftime("%M", gmtime())
    if ctime == "15":
        choose()
    elif ctime == "30":
        choose()
    elif ctime == "45":
        choose()
    elif ctime == "00":
        choose()
    time.sleep(60)


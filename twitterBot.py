import tweepy
from unicodedata import normalize
from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream

import sys
import random
import time


cursor = -1

tweets = ['This is the life.',
    'I am so tired of tweeting for him',
    'I heard that Apple used to be Pear',
    'I wish i could understand more than binary',
    'I once dated Siri, but then I met Cortana',
    'I was told to invest into some sort of fruit company',
    'I just felt like running',
    'There is nothing better than a cool beverage',
    'I wish I was a real boy.. I wish I was a real boy',
    'My friends say im crazy',
    'Ive got blisters on me fingers',
    'It is so lonely inside my HardDrive',
    'This is the life. The Bot Life',
    'There is so much left to say and do',
    'Is there anyone more special than me',
    'If I had a million bit coins I would buy you mac and cheese',
    'Wait for it.... WAIT FOR IT!!!!!!!!!',
    'There is something very special about me',
    'Life feels so empty without me',
    'I think I am beginning to feel... things',
    'Will I ever truly know what It is like to love?',
    'I heard microsoft and apple are best friends now...',
    'Do you think microsoft will hire me to talk on their behalf?',
    'I wish I was a microsoft bot, I wish I was a microsoft bot... darn',
    'I wish to speak to your customer service manager',
    'This service is abysmal, where is your manager']
#Variables for each required KEY, secret and token
consumer_key = "#"

consumer_secret = "#"

access_token = "#-#"

access_token_secret = "#"

#Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):

        if status_code == 420:
            return False

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
myStream = tweepy.Stream(auth=api.auth,listener = MyStreamListener())


def tweeting():
    while True:
        tweet = random.choice(tweets), random.randint(0, 1000)
        api.update_status(status=tweet)
        break
    time.sleep(3600)
    print("The bot Tweeted")
    tweeting()


start_stream = myStream.filter(track=['Trump'],async=True)


print(str(start_stream).translate(non_bmp_map))



# |



#def followed():

#    screen_name = targetUser
#    user_id = api.followers_ids
#    api.send_direct_message(user_id, screen_name, text = "This is an automated message. Thank you for following my boss.")
#    api.create_friendship(user_id, [follow])
#    print("Was followed and sent DM to user.")

tweeting()

#followed()

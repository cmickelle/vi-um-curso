from time import sleep
from os import getenv
from dotenv import load_dotenv
import tweepy #carregando as dependencias// importando os modulos


load_dotenv()
consumer_key = getenv('consumer_key')
consumer_secret = getenv('consumer_secret')
access_token = getenv('access_token')
access_token_secret = getenv('access_token_secret')
Query = getenv('Query')
Like = getenv('Like')
Follow = getenv('Follow')
SleepTime = int(getenv('SLEEP_TIME'))


if Like in ["True", 'TRUE', 'TrUe', 'Verdadeiro']: #statemant
    New_Like = True
else:
    New_Like = False

if Follow in ["True", 'TRUE', 'TrUe', 'Verdadeiro']:
    New_Follow = True
else:
    New_Follow = False


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


print("Twitter bot which retweets, like tweets and follow users")
print("Bot Settings")
print('Like Tweets: {}'.format(New_Like))
print('Follow users: {}'.format(New_Follow))
#print("Like Tweets :", like)
#print("Follow users :", Follow)


for tweet in tweepy.Cursor(api.search_tweets, q=Query).items(): #statemant
    try: #tratamento de exceção
        print('\nTweet by: @' + tweet.user.screen_name)
        #tweet.retweet()
        print(tweet)
        print('Retweeted the tweet')
        if New_Like:
            #tweet.favorite()
            print('Favorited the tweet')
        if New_Follow:
            if not tweet.user.following:
                #tweet.user.follow()
                print('Followed the user')
        sleep(SleepTime) #confirmar se isso é certo

    except tweepy.TweepyException as e:
        print(e)

    except StopIteration:
        break
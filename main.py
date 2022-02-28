from time import sleep
from os import getenv
from dotenv import load_dotenv
import tweepy  # carregando as dependencias// importando os modulos


load_dotenv()
Key = getenv('consumer_key')
Secret = getenv('consumer_secret')
Token = getenv('access_token')
TokenSecret = getenv('access_token_secret')
Query = getenv('QUERY')
Like = getenv('LIKE')
Follow = getenv('FOLLOW')
SleepTime = int(getenv('SLEEP_TIME'))
UserIdViUmCurso = 1646786510  # id de teste


if Like in ["True", 'TRUE', 'TrUe', 'Verdadeiro']:  # statemant
    NewLike = True
else:
    NewLike = False

if Follow in ["True", 'TRUE', 'TrUe', 'Verdadeiro']:
    NewFollow = True
else:
    NewFollow = False


auth = tweepy.OAuthHandler(Key, Secret)
auth.set_access_token(Token, TokenSecret)
api = tweepy.API(auth)


print("Twitter bot which retweets, like tweets and follow users")
print("Bot Settings")
print('Like Tweets: {}'.format(NewLike))
print('Follow users: {}'.format(NewFollow))
# print("Like Tweets :", like)
# print("Follow users :", Follow)


for tweet in tweepy.Cursor(api.search_tweets, q=Query).items():  # statemant
    RetweetStatus = tweet._json['in_reply_to_status_id']
    Id = tweet._json['id']
    CreationTime = tweet._json['created_at']
    Text = tweet._json['text']
    UserId = tweet._json['user']
    print(UserId['id'])

    if RetweetStatus != "null":
        tweet = api.get_status(RetweetStatus)
        RetweetStatus = tweet._json['in_reply_to_status_id']
        Id = tweet._json['id']
        CreationTime = tweet._json['created_at']
        Text = tweet._json['text']
        UserId = tweet._json['user']
        print(UserId['id'])

    if UserId['id'] == UserIdViUmCurso:
        break

    try:  # tratamento de exceção
        print('\nTweet by: @' + tweet.user.screen_name)
        # tweet.retweet()
        print(tweet)
        print('Retweeted the tweet')
        if NewLike:
            # tweet.favorite()
            print('Favorited the tweet')
        if NewFollow:
            if not tweet.user.following:
                # tweet.user.follow()
                print('Followed the user')
        sleep(SleepTime)

    except tweepy.TweepyException as e:
        print(e)

    except StopIteration:
        break

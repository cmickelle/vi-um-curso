from time import sleep
from os import getenv
from dotenv import load_dotenv
import tweepy


load_dotenv()
Key = getenv('consumer_key')
Secret = getenv('consumer_secret')
Token = getenv('access_token')
TokenSecret = getenv('access_token_secret')
Query = getenv('QUERY')
Like = getenv('LIKE')
SleepTime = int(getenv('SLEEP_TIME'))
UserIdViUmCurso = getenv('UserIdViUmCurso')
ListaDeExclusao = 'ListaDeExclusao'


if Like in ["True", 'TRUE', 'TrUe', 'Verdadeiro']:  # statemant
    NewLike = True
else:
    NewLike = False

auth = tweepy.OAuthHandler(Key, Secret)
auth.set_access_token(Token, TokenSecret)
api = tweepy.API(auth)


print("Twitter bot which retweets, like tweets and follow users")
print("Bot Settings")
print('Like Tweets: {}'.format(NewLike))


for tweet in tweepy.Cursor(api.search_tweets, q=Query).items():
    RetweetStatus = tweet._json['in_reply_to_status_id']
    Id = tweet._json['id']
    CreationTime = tweet._json['created_at']
    Text = tweet._json['text']
    print(type(Text))
    UserId = tweet._json['user']
    print(UserId['id'])

    if RetweetStatus != "null":
        try:
            tweet = api.get_status(RetweetStatus)
            RetweetStatus = tweet._json['in_reply_to_status_id']
            Id = tweet._json['id']
            CreationTime = tweet._json['created_at']
            Text = tweet._json['text']
            UserId = tweet._json['user']
            print(UserId['id'])
        except tweepy.errors.NotFound:
            pass

        if UserId['id_str'] == UserIdViUmCurso:
            continue


        with open(ListaDeExclusao, 'rb') as f:
            for Line in f:
                LineStr = str(Line)
                if Text not in LineStr:
                    run = True
                    continue
                else:
                    run = False
                    break



        if run:
            try:  # tratamento de exceção
                print('\nTweet by: @' + tweet.user.screen_name)
                tweet.retweet()
                print('Retweeted the tweet')
                if NewLike:
                    tweet.favorite()
                    print('Favorited the tweet')
                sleep(SleepTime)

            except tweepy.TweepyException as e:
                print(e)

            except StopIteration:
                break


import tweepy
import time
#from tweepy import OAuthHandler
auth = tweepy.OAuthHandler('eY9qQrIZaDuzkmg49NoXVThFX','hKO2UOmHJ68d00UF3YLU84bYV5f82aKPk8krpfxex7lp7jXJFo')
auth.set_access_token('1256632516397731841-nhHPnZD8nJHxyRwZrch3Mk0WCDMg5s','7vzEMP7eYTZVaznhTTnfPcmydk5DXO0Gebexbz3UD0jKW')

api =tweepy.API(auth, wait_on_rate_limit=True , wait_on_rate_limit_notify=True)

user = api.me()
#print(user.screen_name)

#search = 'Javascript'

#search = ('Javascript','python','programming','devcommunity','Coding','100DaysofCode','webdevelopment','codenewbie')

search = ('Javascript','python','programming','devcommunity','ChallengeAccepted','BigData', 
'Analytics', 'DataScience', 'AI', 'MachineLearning', 'RStats', 'TensorFlow', 'Java', 'ReactJS', 
'CloudComputing', 'Serverless', 'DataScientist','Coding','100DaysofCode','QuoteoftheDay','webdevelopment')
nrTweets = 1000 #number of tweets(nrTweets)

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('like ho gaya reeee')
        tweet.favorite()
        time.sleep(2)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
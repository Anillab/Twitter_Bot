import tweepy
consumer_key='X2NVAdwqSWeQmcApHaKaJOgfF'
consumer_secret='Pn8Yqv0aYXf4HgYFD0NePKbWHVEGBkXHfoToK4kzsWNo28Z2iT'
access_token='3073532904-Z0tOhYn1fQR8aR2EWrzAJCJWWKuXOkkIn2qeFqv'
access_token_secret='Qc09EWu90T4HkUtAhICUOjVK2XWfSWeYqO3YPXyDtT2jV'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user=api.me()
# public_tweets=api.home_timeline()
# for tweet in public_tweets:
#     print(tweet)
print(user.name)
def main():
    search=('alcohol','love')
    number_of_tweets=5
    for tweet in tweepy.Cursor(api.search,search).items(number_of_tweets):
        try:
            tweet.retweet()
            print('Tweet Retweeted')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

main()

import tweepy
import pandas as pd
from numpy import unicode
import os
from Twitter_Django.utils.Source_code import Path_file as pf

# The class to authenticate Twitter application to have twitter Application program interface(API)
# Step 1 to authenticate Twitter application to have twitter API
class authenticate:

    # Credentials for Twitter Application (The application created as twitter developer)
    consumer_key = "LXxius9VCSlVwJvhmWTDJeeCB" # Consumer key
    consumer_secret = "nf62aFl9u1SuqNpnfd2x5GAxYnmvXURicvsX2VkoQQtcGiaqRJ" # Consumer secrete
    access_token = "1160031453578612736-0ju1UkLD1i1nhUKVbmZ73b0E3nViX5" # access token
    access_token_secret = "thLz3nl3qxalUVikTFt7jYrP6xOx8xsKZqovd5hBxCKdO" # Access_token_secret

# The method authenticates the credentials of user in order to connect to Twitter
    def authenticator(self):

        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        # return authorization handler
        return auth

#Class to download tweets
class save_to_csv:

    def get_tweets(self,api,listOfTweets, keyword, numOfTweets):

        # iterate through all tweets containing the given word, api search mode
        for tweet in tweepy.Cursor(api.search, q=keyword, lang="en").items(numOfTweets ):

            # create column heads for storing details of tweet
            # Add tweets in this format
            dict1 = { 'Screen Name ': tweet.user.screen_name,
                     'User Name ': tweet.user.name,
                     'Tweet Created At': unicode(tweet.created_at),
                     'Tweet Text': tweet.text,
                     'User Location': unicode(tweet.user.location),
                     'Retweet Count': unicode(tweet.retweet_count),
                     'Retweeted': unicode(tweet.retweeted),
                     'Phone Type': unicode(tweet.source),
                     'Favorite Count':unicode(tweet.favorite_count),
                     'Favorited ':unicode(tweet.favorited),
                     'Replied': unicode(tweet.in_reply_to_status_id_str)
                     }
            # create list of dictionaries
            listOfTweets.append(dict1)

            #print(listOfTweets)
        return listOfTweets

#Class to save tweets in csv file
class Startpoint:
    def Access(self,Topic_name,No_Tweets):
        #Authenticate the user
        au =authenticate() # Creating the object of authenticate
        authentication=au.authenticator() # Function to authenticate and return authorization

        #API to manipulate data
        api = tweepy.API(authentication, wait_on_rate_limit = True, wait_on_rate_limit_notify= True )

        # Accept Topic,no of tweet,and csv name from use
        Topic=Topic_name
        subjectname=Topic
        Tweet_no=No_Tweets

        #creating object of
        STCSV=save_to_csv()

        # passing parameter to get_tweet method
        Tweet_list=STCSV.get_tweets(api,list(),Topic,Tweet_no)
        df = pd.DataFrame(Tweet_list) # the single tweet is saved as dictionary and saved it in list and this added into dataframe

        os.chdir(pf.DOWNLOAD_CSV)
        # created csv
        df.to_csv(Topic+'.csv')
        return Topic,subjectname






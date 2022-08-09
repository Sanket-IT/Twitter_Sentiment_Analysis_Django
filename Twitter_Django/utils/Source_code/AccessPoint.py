import os

from Twitter_Django.utils.Source_code.Cleaning_of_Tweets import cleaning
from Twitter_Django.utils.Source_code.Download_tweet import Startpoint
from Twitter_Django.utils.Source_code.Graphical_repre import DrawGraphs
from Twitter_Django.utils.Source_code.Naive_Bayse_Implementation import Train_algo

class Execution_Point:
    def __init__(self, topicname,tweetno):
        self.topicname=topicname
        self.tweetno=tweetno
        print(topicname)
        print(tweetno)


    def Start_Excution(self):
        #Call Download_tweet
        start=Startpoint()
        store_topic,subject=start.Access(self.topicname,self.tweetno)

        #Call cleaning_of_Tweets
        cln=cleaning(store_topic)
        cleaned_csv_tweet=cln.clean_Tweet(store_topic)

        #train model
        train=Train_algo(cleaned_csv_tweet)
        naive=train.train_naive(cleaned_csv_tweet,subject)

        #Generate Graph
        present = DrawGraphs(naive, subject)
        x=present.Graph_result(naive, subject)
        present.Wordcloud(cleaned_csv_tweet, subject)

        return x





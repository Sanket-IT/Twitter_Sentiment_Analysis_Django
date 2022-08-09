import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from Twitter_Django.utils.Source_code import Path_file as pf

import os
sw: object = stopwords.words("english")


#function for remove user
def remove_user(user):
    user = nltk.re.sub('@[^\s]+','',user)
    return user

#function for remove url
def remove_url(url):
    url = nltk.re.sub('https://[^\s]+','',url)
    return url

#function for remove rt
def remove_rt(rt):
    rt = "".join([char for char in rt if char not in 'RT'])
    rt = nltk.re.sub('[0-9]+','',rt)
    return rt

#function for remove punctuation
def remove_punc(punc):
    punc = "".join([char for char in punc if char not in string.punctuation])
    punc = nltk.re.sub('[0-9]+',"",punc)
    return punc

#function for remove stop words
def remove_stop(stop):
    list1=[]
    v = stop.split()
    for word in v:
        if word not in sw:
            list1.append(word)
    print(list1)
    return list1


#class for pass csv to the above mentioned function
class cleaning:

    #Constructor
    def __init__(self, topicname):
        self.topicname =topicname

    #methods for cleaning
    def clean_Tweet(self,topicname):

        os.chdir(pf.DOWNLOAD_CSV)#change directory to read csv of downloaded tweet

        #remove user
        df = pd.read_csv(topicname+'.csv', usecols=['Tweet Text'])
        df['Remove user'] = df['Tweet Text'].apply(lambda x: remove_user(x))

        os.chdir(pf.CLEANED_CSV)#Derectory to save clean tweets

        clean_csv = topicname + 'New.csv'
        df.to_csv(clean_csv,index=False)

        #remove url

        df = pd.read_csv(clean_csv)
        df['Remove url'] = df['Remove user'].apply(lambda x: remove_url(x))
        df.to_csv(clean_csv)

        #remove RT
        df['Remove RT'] = df['Remove url'].apply(lambda x: remove_rt(x))
        df.to_csv(clean_csv)

        #remove punctuation
        df['Remove pun'] = df['Remove RT'].apply(lambda x: remove_punc(x))
        df.to_csv(clean_csv)

        #remove stopwords
        df['Remove stop'] = df['Remove pun'].apply(lambda x: remove_stop(x))
        df.to_csv(clean_csv)

        return clean_csv


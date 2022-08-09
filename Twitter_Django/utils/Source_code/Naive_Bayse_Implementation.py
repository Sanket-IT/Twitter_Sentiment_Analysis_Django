import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from sklearn import naive_bayes
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import  accuracy_score
from sklearn.model_selection import train_test_split
from Twitter_Django.utils.Source_code import Path_file as pf
import os

#Class to train Naive Bayse
class Train_algo:
    os.chdir(pf.CWD)
    def __init__(self, cleantopicname):
        self.cleantopicname =cleantopicname

    def train_naive(self,topicname,subjectname):

        os.chdir(pf.CWD)
        df=pd.read_csv('train.csv',encoding='ISO-8859–1')

        os.chdir(pf.CLEANED_CSV)
        df2 = pd.read_csv(topicname, usecols=['Remove pun'])

        stopset = set(stopwords.words('english'))

        vectorizer=TfidfVectorizer(use_idf=True,lowercase=True,strip_accents='ascii',stop_words=stopset)

        y=df.Sentiment

        X=vectorizer.fit_transform(df.SentimentText)#attributes of tfidf vectorizer

        X_train, X_test,y_train, y_test=train_test_split(X, y, random_state=42)

        clf=naive_bayes.MultinomialNB() #Algorithm

        clf.fit(X_train,y_train)# Actual Training .Tell the model what should be the output of particular input

        datasize=df2.size

        selectcolumn=np.ndarray(datasize)

        selectcolumn.fill(0)
        predicts = clf.predict(X_test)
        print("Accuracy Rate, which is calculated by accuracy_score() is: ", accuracy_score(y_test, predicts))

        classfied=[]
        for i in range(0,datasize):
            print(datasize)
            sentence=np.array(df2.loc[i])
            reviews_vector=vectorizer.transform(sentence)
            polarity=clf.predict(reviews_vector)
            print(sentence,polarity)
            #catagory=list(polarity)

            tweets=list(sentence)

            dict = {'Sentiment': polarity, 'Tweets': sentence}
            print(dict)
            classfied.append(dict)
        df3 = pd.DataFrame(classfied)
        os.chdir(pf.POLARITY_CSV)

        polarityfile='Polarity'+topicname
        print(df3)
        df3.to_csv(polarityfile,index=False)

        return polarityfile
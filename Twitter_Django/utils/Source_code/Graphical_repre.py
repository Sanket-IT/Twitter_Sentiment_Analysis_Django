import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import os
from Twitter_Django.utils.Source_code import Path_file as pf
from wordcloud import WordCloud, STOPWORDS
from wordcloud import STOPWORDS
from nltk.corpus import stopwords
s1=set(stopwords.words('english'))
s2=set(STOPWORDS)
set3=s1.union(s2)
set3.add('rt')
set3.add('RT')

class DrawGraphs():

    result_data = None
    positive = 0
    negative = 0
    neutral = 0
    def __init__(self, polarityfile,subjectname):
        self.polarityfile = polarityfile
        self.subjectname = subjectname
        self.positive =0
        self.negative = 0
        self.neutral = 0

    def Graph_result(self,polarityfile,subjectname):
        os.chdir(pf.POLARITY_CSV)
        df=pd.read_csv(polarityfile,usecols=['Sentiment'])
        cnt0 = 0
        cnt4 = 0
        cnt2 = 0
        for x in df['Sentiment']:
            if x == '[4]':
                cnt4 += 1
            elif x == '[0]':
                cnt0 += 1
            elif x == '[2]':
                cnt2 += 1
        print('The no of positive tweets: ', cnt4)
        print('The no of negative tweets: ', cnt0)
        print('The no of neutral tweets: ', cnt2)
        sixe = df.size
        for i in range(0, sixe):
            value = df.loc[i]

        color = ['black', 'red', 'green']
        objects = ('Positive', 'Negative', 'Neutral')
        y_pos = np.arange(len(objects))
        performance = [cnt4, cnt0, cnt2]

        plt.clf()
        plt.bar(y_pos, performance, align='center', alpha=0.5, color=['black', 'red', 'green'])
        plt.xticks(y_pos, objects)
        plt.ylabel('Score')
        plt.xlabel('Sentiment')
        plt.title('Classification')
        os.chdir(pf.BAR_CHART)
        plt.savefig(subjectname+'.png')
        plt.clf()

        x=[cnt4,cnt0,cnt2]
        labs = ['Positive', 'Negative', 'Neutral']
        explode = (0.1,0.1,0.1)  # explode 1st slice
        plt.pie(x, labels=labs,explode=explode)

        os.chdir(pf.PIE_CHART)
        plt.savefig(subjectname+'.png')

        return x

    def Wordcloud(self,cleaned_csv,topic):
        os.chdir(pf.CLEANED_CSV)
        df = pd.read_csv(cleaned_csv, usecols=['Remove stop'])
        answer = [''.join(df.values[:, i]) for i in range(len(df.columns))]
        # answer.append(list())
        print(answer)

        # Python program to generate WordCloud
        # importing all necessery modules
        # Reads 'Youtube04-Eminem.csv' file
        comment_words = ' '
        stopwords = set(STOPWORDS)
        # iterate through the csv file

        for val in answer:
        # typecaste each val to string
            val = str(val)

        # split the value
        tokens = val.split()

        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        for words in tokens:
            comment_words = comment_words + words + ' '

        wordcloud = WordCloud(width=800, height=800,
        stopwords = set3,
        min_font_size = 20,
        max_font_size=200,background_color="black").generate(comment_words)

        # plot the WordCloud image
        plt.figure(figsize=(8, 8))
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)
        os.chdir(pf.WORD_CLOUD)
        plt.savefig(topic+'.png')
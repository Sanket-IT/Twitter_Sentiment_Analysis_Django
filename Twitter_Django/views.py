from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, request
# Create your views here.
from Twitter_Django.utils.Source_code.AccessPoint import Execution_Point
from  Twitter_Django.utils.Source_code.Graphical_repre import DrawGraphs
from django.contrib import messages

def index(request):
    return render(request,'Twitter_Django/login.html')

def topicrep(request):
    return render(request, 'Twitter_Django/Topic.html')

def topic(request):
    user = request.POST['userid']
    password = request.POST['pwd']
    if user == "":
        messages.error(request,'Enter UserName')
        return render(request,'Twitter_Django/login.html')
    elif password == "":
        messages.error(request,'Enter Password')
        return render(request,'Twitter_Django/login.html')
    elif user == "Twitter@999" and password == "django@999":
        messages.success(request,'User Login Successfull')
        return render(request,'Twitter_Django/Topic.html')
    else:
        messages.error(request, 'User Login unsuccessful')
        return render(request, 'Twitter_Django/login.html')


def result(request):
    topic_name= request.POST['topic']
    no_tweets = int(request.POST['no'])
    if no_tweets >500:
        messages.error(request,'No of Tweets Exceeds than 500')
        return render(request,'Twitter_Django/Topic.html')

    obj=Execution_Point(topic_name,int(no_tweets))

    sentiment_score=obj.Start_Excution()
    pos=sentiment_score[0]
    neg=sentiment_score[1]
    neu=sentiment_score[2]
    if pos>neg and pos>neu:
        maxtweet="Positive"
    elif neg>pos and neg>neu:
        maxtweet="Negative"
    else:
        maxtweet="Neutral"
    content = {
            'topic': topic_name, 'nom': no_tweets,'pos':pos, 'neg':neg,'neu':neu,'maxtweet':maxtweet,
        }
    messages.success(request,'Classification Success')
    return render(request,'Twitter_Django/Result.html',{'d1':content})


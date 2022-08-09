from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),#login page
    url(r'^Topic.html$',views.topic,name='topic'), #topic
    url(r'^Result.html$',views.result,name='result'),#result

]
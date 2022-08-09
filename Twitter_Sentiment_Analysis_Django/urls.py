from django.conf.urls import include
from django.urls import re_path as url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Twitter_Django/', include('Twitter_Django.urls')),
]

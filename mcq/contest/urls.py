from django.conf.urls import include, url 
from django.contrib import admin

urlpatterns = [
    url(r'^create$', 'contest.views.create', name = 'create-contest'),
]

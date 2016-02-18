from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'mcq.views.home', name='home'),
    url(r'^mcq/', include('Questions.urls')),
    url(r'^contest/', include('contest.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'Questions.views.find_questions_with_given_tags', name='home'),
    url(r'^mcq/', include('Questions.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

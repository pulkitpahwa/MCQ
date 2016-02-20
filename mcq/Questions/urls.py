from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^(?P<contest>[-\w]+)/create-pool$', 'Questions.views.count_questions_with_given_tags', name='questions-home'),
    url(r'^(?P<contest>[-\w]+)/save-pool$', 'Questions.views.save_questions_with_given_tags', name='questions-home'),
    url(r'^add_multiple$', 'Questions.views.add_questions_from_csv', name='csv-upload'),
]

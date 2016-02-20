from django.conf.urls import include, url 

urlpatterns = [
    url(r'^(?P<pool_name>[-\w]+)$', 'QuestionPool.views.pool_cache', name = 'pool_cache'),
]

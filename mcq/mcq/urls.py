from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import settings

urlpatterns = [
    url(r'^$', 'mcq.views.home', name='home'),
    url(r'^mcq/', include('Questions.urls')),
    url(r'^contest/', include('contest.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
]

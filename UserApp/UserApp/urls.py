from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^userapplication/admin/', include(admin.site.urls)),
    url(r'^userapplication/', include('userapplication.urls')),
)

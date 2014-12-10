from django.conf.urls import patterns, url

from userapplication import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
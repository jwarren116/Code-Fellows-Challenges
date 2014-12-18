from django.conf.urls import patterns, url

from userapplication import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^update/(?P<id>\d+)/$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
)

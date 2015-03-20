# coding=utf-8
from django.conf.urls import patterns, url
from fetchcar import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<car_id>\d+)', views.detail, name="detail"),
                       )

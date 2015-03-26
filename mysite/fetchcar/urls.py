# coding=utf-8
from django.conf.urls import patterns, url
from fetchcar import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^search', views.search, name="search"),
                       url(r'^(?P<car_id>\d+)', views.detail, name="detail"),
                       url(r'^_cartype_api', views.cartype_api,
                           name="cartype_api"),
                       url(r'^_brand_api', views.brand_api, name="brand_api")
                       )

from django.conf.urls import url, include
from django.shortcuts import render, get_object_or_404
from . import views

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^$',views.index, name = 'index'),
    url(r'^A/$',views.A, name = 'A'),
url(r'^AA/$',views.AA, name = 'AA'),
]

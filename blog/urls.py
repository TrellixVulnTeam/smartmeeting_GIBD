# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
app_name='dic'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^group_make/$',views.group_make,name='group_make'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post_list$', views.post_list, name='post_list'),
    url(r'^sign_up/$', views.signup, name='sign_up'),
    url(r'^sign_in/$', views.signin, name='sign_in'),
    url('^sign_out/$', auth_views.logout, {'next_page' : '/'}),
    
]
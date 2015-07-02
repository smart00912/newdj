#coding: utf8
__author__ = 'sean.li'

from django.conf.urls import include, url

urlpatterns = [
	url(r'^index/', 'Index', prefix='newapp.views'),
	url(r'^login/', 'Login', prefix='newapp.views'),
	url(r'^auth/$', 'Auth', prefix='newapp.views'),
	url(r'^region/', 'Menu', prefix='newapp.views'),
	# limit num_id from 1 to 99
	url(r'^artlist/(?P<num_id>\d{1,2})$', 'List', prefix='newapp.views'),
	# 把(\d[1,2])括号内的值作为参数传入到后端，后端需要设置额外一个接受参数
	url(r'^time/plus/(\d{1,2})/$', 'hours_ahead',prefix='newapp.views'),
#  url(r'^artlist/(\d[1,2])$',views.List,{'action':'index','userclass',9}),
]
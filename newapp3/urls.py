__author__ = 'sean.li'

from django.conf.urls import url

urlpatterns=[
	url(r'^login/$','Login',prefix='newapp3.views'),
	url(r'^loginform/','LoginF',prefix='newapp3.views'),
	url(r'^userinfo/','Details',prefix='newapp3.views'),
]
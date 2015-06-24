__author__ = 'sean.li'
from django.conf.urls import include,url

urlpatterns=[
    url(r'^index/','Index',prefix='newapp2.views'),
    url(r'^login/','Login',prefix='newapp2.views'),
    url(r'^auth/$','Auth',prefix='newapp2.views'),
    url(r'^region/','Menu',prefix='newapp2.views'),
    url(r'^addrow/','Exec',prefix='newapp2.views'),
	url(r'^(?P<pid>\d+)/query/$','Query',prefix='newapp2.views'),
	url(r'^queryall/','QueryAll',prefix='newapp2.views'),
    url(r'^artlist/(?P<num_id>\d*)$', 'List',prefix='newapp2.views'),
]

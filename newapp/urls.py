__author__ = 'sean.li'
from django.conf.urls import include,url

urlpatterns = [  
    url(r'^index/','Index',prefix='newapp.views'),
	url(r'^login/','Login',prefix='newapp.views'),
    url(r'^auth/$','Auth',prefix='newapp.views'),
    url(r'^region/','Menu',prefix='newapp.views'),
    url(r'^artlist/(?P<num_id>\d*)$','List',prefix='newapp.views'),
    #pass id to backend
#    url(r'^artlist/(\d*)$',views.List,{'action':'index','userclass',9}), 
] 

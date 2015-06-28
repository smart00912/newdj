__author__ = 'sean.li'

from django.conf.urls import url
from fms.AccountForm import LoginForm


urlpatterns=[
	url(r'^$','Index',prefix='newapp3.views'),
	url(r'^login/$','Login',prefix='newapp3.views'),
	url(r'^logout/$','Logout',prefix='newapp3.views'),
	url(r'^loginform/','LoginF',prefix='newapp3.views'),
	url(r'^userinfo/','Details',prefix='newapp3.views'),
	url(r'^accounts/login/$','django.contrib.auth.views.login',{'template_name':'newapp3/loginform.html','extra_context':{'model':LoginForm}},),
	
]
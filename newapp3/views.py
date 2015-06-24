#coding: utf-8

from django.shortcuts import render,redirect,render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from fms.AccountForm import LoginForm







# Create your views here.

def Login(req):
	data = {'loginstatus':''}
	if req.method == 'POST':
		postData = req.POST
		username = postData.get('user')
		password = postData.get('pwd')
		# in case user disabled js in broswer side need to check backend also
		if username and password:
			# using authencate method
			authobj = authenticate(username=username,password=password)
			if authobj is not None:
			#authobj = Auth.objects.get(uname=username,pwd=password)
				return redirect('/newapp3/userinfo/')
			data['loginstatus'] = 'username or password is incorrect'
	return render_to_response('newapp3/login.html',data,context_instance=RequestContext(req))

def LoginF(req):
	if req.method == 'GET':
		form = LoginForm()
		return render_to_response('newapp3/loginform.html',context_instance=RequestContext(req,{'model':form},))
	else:
		form = LoginForm(req.POST)
		if form.is_valid():
			'''
			username= req.POST.get('username','')
			password = req.POST.get('password','')
			'''
			'''
			 clean_data is a dic will store  all value that they are passed the authencate like 
			 {'username': u'admin', 'password': u'admin', 'email': u'qpz163_4444@163.com'}
			 如果验证通过，你可以通过form.clean_data访问这些验证通过的数据
			'''
		#	da = form.cleaned_data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username,password=password)
		#	是否允许用户登录, 设置为``False``，可以不用删除用户来禁止 用户登录
			if user is not None and user.is_active:
				
				return HttpResponse('OK')
			else:
				return render_to_response('newapp3/loginform.html',context_instance=RequestContext(req,{'model':form}))
		else:
			return render_to_response('newapp3/loginform.html',context_instance=RequestContext(req,{'model':form},))

def Details(req):
	return  HttpResponse('ok')
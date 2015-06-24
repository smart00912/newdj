from django.shortcuts import render,render_to_response,redirect
import json


# Create your views here.
from django.http import HttpResponse
from newapp2.models import *
from django.template import RequestContext


def Index(req):
	return HttpResponse('<H1>test2</H1>')


def Login(req):
	return render_to_response('index.html')

def LoginNew(req):
	data = {'loginStatus':''}
	if req.method == 'POST':
		postData = req.POST
		username = postData.get('username')
		password = postData.get('password')
		if username == 'sean' and password == '123':
			return redirect('index.html')
		else:
			data['loginStatus'] = 'username or password incorrect'
			return render_to_response('login.html',data,context_instance=RequestContext(req))

def Auth(req):
	user,passwd= req.GET['u'],req.GET['p']
	if user == 'sean':
		print 'handsome'
	else:
		print 'no'
	return  render_to_response('auth.html')


def Menu(req):
	region_dic = {
		'beijing':{'haidian':['haidian1','haidian2']},
		'shanghai':{'xuhui':['xuehui1','xuhui2']}
	}
	js_dic=json.dumps(region_dic)
	return HttpResponse(js_dic)

def List(req,num_id):
	family= ['sean','doudou','xiaoer']
	if num_id:
		num_id=int(num_id) 
		if num_id >=len(family):
			num_id=len(family)-1
	#	result = '</br>'.join(family[int(num_id)])
	else:
		num_id=0
	return HttpResponse('<H1>here is newapp 2 '+family[num_id]+'</H1>')


def Exec(req):
	add_row=Book (book_name='book-add-from-view')
	add_row.save()
	return HttpResponse(str(add_row.id)+'---add row seccussfuly to Book!')

def Query(req,pid):
	# Dont use req.GET when no dic parameter passed in
	result = Book.objects.get(id=int(pid))
	# In the model already defied __unicode__ return value for table book
	# so  can just place result here 

	#	return HttpResponse(result)
	return  render_to_response('test.html',{'bookname':result,'price':18,'pid':int(pid),'sean':'good guy'})

def QueryAll(req):
	result = Book.objects.all()
	# variable 'context_instance' try to avoid CSRF security issue (only post method need it)
	return  render_to_response('test.html',{'res':result},context_instance=RequestContext(req))



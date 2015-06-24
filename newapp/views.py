from django.shortcuts import render,render_to_response
import json

# Create your views here.
from django.http import HttpResponse

def Index(req):
	return HttpResponse('<H1>test</H1>')


def Login(req):
	return render_to_response('index.html')

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
	return HttpResponse('<H1>'+family[num_id]+'</H1>')



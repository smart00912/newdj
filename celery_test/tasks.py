__author__ = 'sean'
from celery.decorators import task

@task
def add(x,y):
	return x+y

@task
def listp(str):
	sum = 0
	for t in xrange(str):
		sum += t
	return sum
		


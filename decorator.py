__author__ = 'sean.li'
'''
def wrapper(func):
	def result():
		print 'before'
		func()
		print 'after'
	return  result

def foo():
	print 'foo'

de = wrapper(foo)
de()
'''

# exp1
def wrapper(func):
	def result():
		print 'before'
		func()
		print 'after'
	return  result

@wrapper
def foo():
	print 'foo'
	
foo()


#exp2

		

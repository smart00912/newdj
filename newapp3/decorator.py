#coding: utf-8
__author__ = 'sean.li'

def Before(arg1,arg2):
	if arg1>2:
		return None
	else:
		return arg1+arg2
	
def After(arg1,arg2):
	if arg2>2:
		return None
	else:
		return arg1+arg2

def Fileter(before_func,after_func):
	def outer(main_func):
		def wrapper(request,kargs):
			before_result = before_func(request,kargs)
			if(before_result != None):
				return before_result;
			
			main_result = main_func(request,kargs)
			if(main_result != None):
				return main_result;
			
			after_result = after_func(request,kargs)
			if(after_result != None):
				return after_result;
			
		return wrapper
	return outer

# 如果装饰器中的before先返回非none结果，那么将不会继续执行（main和after都不会执行）
@Fileter(Before,After)
# List函数相当于装饰器里的main_func
def Execute(arg1,arg2):
	return 1+2
#  return None 会得到不同的结果

print Execute(1,3)
print Execute(3,1)
print Execute(3,3)







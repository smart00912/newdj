__author__ = 'sean.li'

def Filter(before_func,after_func):
	def outer(main_func):
		def wrapper(request,kargs):
			
			before_result = before_func(request,kargs)
			if(before_result != None):
				return before_func
			
			main_result = main_func(request,kargs)
			if(main_result != None):
				return main_result
			
			after_result = after_func(request,kargs)
			if(after_result != None):
				return after_result
			
		return wrapper
	return outer

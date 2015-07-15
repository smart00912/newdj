__author__ = 'sean.li'

 #request and view will run before view module first 
 #exception and response will run view module after
class MiddleW(object):
    def process_request(self,request):
        pass
    def process_view(self, request, callback, callback_args, callback_kwargs):
        pass
    def process_exception(self, request, exception):
        pass
    
    def process_response(self, request, response):
        return response
    
class MiddleW2(object):
    def process_request(self,request):
        pass
    def process_view(self, request, callback, callback_args, callback_kwargs):
        pass
    def process_exception(self, request, exception):
        pass
    
    def process_response(self, request, response):
        return response

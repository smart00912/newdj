class Test(object):
	__slots__ = ('name', 'age')


test = Test()
test.name = 'sean.li'
test.age = '33'
# test.address='beijing' will have error

class Father(object):
	def __init__(self):
		print 'here is fathers class'


class Children(Father):
	def __init__(self):
		print 'here is childrens class'
		# call father class
		super(Children, self).__init__()
result = Children()

# show all father class for a children class
print  Children.__base__
print issubclass(Children,Father)


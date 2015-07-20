#coding: utf-8
__author__ = 'sean.li'


#动态为类添加方法
class Foo:
	def __init__(self):
		self.name='sean.li'
	def fun1(self):
		print 'fun1'

def Test(arg):
	print 'test'

# 动态添加的方法是动态的，必须要实例才能访问
Foo.fun2=Test
f=Foo()
f.fun2()

# 动态添加的属性是静态的
Foo.age=19
print Foo.age

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

# 新式类中限制自定义动态字段（__slots__）

class Foo(object):
	__slots__=('name','age')
# 限制实例只能添加指定的动态属性，否则将报错

#新式类和经典类关于执行父类构造函数的区别
'''经典类
Father.__init__(self) 
'''
'''新式类
super(children,self).__init__()
'''
'''
python和其他语言的区别，当执行子类构造函数时不会调用父类的构造函数！！
这样，当调用子类时如果需要初始化父类那么需要显式的调用父类的构造函数
'''
class Father(object):
	def __init__(self):
		print 'here is fathers class'


class Children(Father):
	def __init__(self):
		print 'here is childrens class'
		# call father class
		super(Children, self).__init__()
result = Children()

# 像是一个类的向上一级父类（多级继承只显示最近的上一级）
print  Children.__base__
print issubclass(Children,Father)

# 语法糖 call()




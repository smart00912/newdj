#coding: utf-8
__author__ = 'sean.li'

#exec and compile comand
code = "for i in range(10): print i"
cmpcode = compile(code,'','exec')
exec  cmpcode

code = "print 1"
cmpcode = compile(code,'','single')
exec cmpcode


# id command 显示内存地址，深拷贝浅拷贝
a=1
b=a
id(a)
id(b)

#reload
import os
reload(os)


#三元运算

a=raw_input('input')
b=raw_input('input')

a = 'equal' if a==b else 'unequal'
print a

#lambda

a= lambda x,y:x+y
print a(4,10)

#yield  迭代 生成器


#enumerate
a= [1,2,3,4]
for x,y in enumerate(a):
	print x,y

# format
a= 'my name is {0} i am {1} years old'
print a.format('sean',20)

#apply 方式执行函数
def func(arg):
	return arg

print apply(func,('aaaaa'))



#getatter 反射 
modeule = __import__('os')
#print all attributes and functions
dir(modeule)

func = getattr(modeule,"popen")
func()
#利用getattr制作自定义路由
#
# url('^(?p<view>(\w+))/(?p<action>(\w+)))$',Execute)
#上面把url里的值当作字典（{view:'testview',action:'add'}）传给Execute方法去解析出指定的view和action









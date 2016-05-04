#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

class MyClass(object):
	"""docstring for MyClass"""
	def __init__(self,):
		super(MyClass, self).__init__()
		print('init the class')

	i = 12345
	def f(self):
		return 'hello world'	

if __name__ == '__main__':
	x = MyClass()
	print(x.i)
	print(x.f())
	print(MyClass.i)
	print(MyClass.f)
	print(x.f)
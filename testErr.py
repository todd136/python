#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import sys

try:
	f = open('myfile.txt')
	s = f.readline()
	i = int(s.strip())
except OSError as err:
	print('OS error: {0}'.format(err))
except ValueError:
	print('could not convert data to an integer')
except:
	print('unexcepted error', sys.exc_info()[0])


try:
	raise Exception('spam', 'eggs')
except Exception as inst:
	print(type(inst))
	print(inst.args)
	print(inst)
	x, y = inst.args
	print('x = ', x)
	print('y = ', y)

try:
	raise NameError('a raise exception')
except NameError:
	print('a name error flew by')
	raise

class MyError(Exception):
	"""docstring for MyError"""
	def __init__(self, value):
		super(MyError, self).__init__()
		self.value = value
	def __str__():
		return repr(self.value)

try:
	raise MyError(2*2)
except MyError as e:
	print('my exception occurred, value :', e.value)

def divide(x, y):
	try:
		result = x/y
	except ZeroDivisionError:
		print('division by zero')
	else:
		print('result = ', result)
	finally:
		print('excuting finally')
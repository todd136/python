#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

def scope_test():
	def do_local():
		spam = 'local spam'
		print('in do_local, spam:', spam)

	def do_nonlocal():
		nonlocal spam
		spam = 'nonlocal spam'

	def do_global():
		global spam
		spam = 'global spam'

	spam = 'test spam'
	do_local()
	print('after local assignment:', spam)
	do_nonlocal()
	print('after nonlocal assignment:', spam)
	do_global()
	print('after global assignment:', spam)

if __name__ == '__main__':
	scope_test()
	print('in global scope:', spam)

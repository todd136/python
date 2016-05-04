#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

class Reverse(object):
	"""docstring for Reverse"""
	def __init__(self, data):
		super(Reverse, self).__init__()
		self.data = data
		self.index = len(data)

	def __iter__(self):
		return self

	def __next__(self):
		if  self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]

if __name__ == '__main__':
	rev = Reverse('spam')
	iter(rev)
	for char in rev:
		print(char)
		
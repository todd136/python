#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

class Mapping(object):
	"""docstring for Mapping"""
	def __init__(self, iterable):
		super(Mapping, self).__init__()
		self.items_list = []
		self.__update(iterable)

	def update(self, iterable):
		for item in iterable:
			self.items_list.appen(item)

	__update = update

class MappingSubclass(Mapping):
	"""docstring for MappingSubclass"""
	def __init__(self, arg):
		super(MappingSubclass, self).__init__()
		self.arg = arg
	
	def update(self, keys, values):
		for item in zipkeys, values):
			self.items_list.append(item)
		
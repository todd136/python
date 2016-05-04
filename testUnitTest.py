#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import unittest

from MyDict import MyDict

class TestMyDict(unittest.TestCase):
	"""
	docstring for TestMyDict
	"""
	def setUp(self):
		print('setUp, prepare to do unittest')

	def test_init(self):
		d = MyDict(a=1, b = 'test')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'test')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = MyDict()
		d['key'] = 'value'
		self.assertEqual(d.key, 'value')

	def test_attr(self):
		d = MyDict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'value')

	def test_keyerror(self):
		d = MyDict()
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		d = MyDict()
		with self.assertRaises(AttributeError):
			value = d.empty

	def tearDown(self):
		print('tearDown, prepare to destory unittest')

if __name__ == '__main__':
	unittest.main()
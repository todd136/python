#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		super(Student, self).__init__()
		self.name = name

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an int value')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100')
		self._score = value

	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self, birthday):
		self._birth = birthday

	@property
	def age(self):
		return 2016 - self._birth
s = Student('s1')
s.score=76
s.birth = 1982
print(s.score)
print(s.name)
print(s.birth)
# s.age = 35
print(s.age)


class Screen(object):
	"""docstring for Screen"""
	def __init__(self,):
		super(Screen, self).__init__()

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, width):
		if width < 0:
			raise ValueError("width can't less than  0")
		self._width = width

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		if height < 0:
			raise ValueError("height can't less than 0")
		self._height = height

	@property
	def resolution(self):
		return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

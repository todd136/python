#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		super(Student, self).__init__()
		self.name = name


def  print_score(self, score):
	print(': score = ' , score)

from types import MethodType
s = Student('s')
s.print_score = MethodType(print_score, s)
s.print_score(78)

s1 = Student('s1')
# s1.print_score(65)

Student.print_score = MethodType(print_score, Student)
s2 = Student('s2')
# # s1.print_score(65)
s2.print_score(75)


from types import MethodType
def set_age(self,age):
    self.age=age
class Stu(object):
    pass

Stu.set_age = set_age
# Stu.set_age=MethodType(set_age,Stu)
A=Stu()
B=Stu()
A.set_age(10)
B.set_age(15)
print(A.age,B.age)

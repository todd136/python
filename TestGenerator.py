#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

def reverse(data):
	for index in range(len(data)-1, -1, -1):
		yield(data[index])

for char in reverse('golf'):
	print(char)

print(sum(i*i for i in range(10)))

from math import pi, sin
sin_table = {x:sin(x*pi/180) for x in range(0,91)}
print(sin_table)

data = 'golf'
l = list(data[i] for i in range(len(data) - 1, -1, -1))
print(l)
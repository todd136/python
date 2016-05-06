#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

class Hello(object):
        """docstring for Hello"""
        # def __init__(self, name='world'):
        #         super(Hello, self).__init__()
        #         self.name = name

        def hello(self,name='world'):
                print('hello, %s' % name)

h = Hello()
h.hello()

print(type(Hello))
print(type(h))

def func(self, name = 'world'):
        print('hello, %s' % name)

Hello2 = type('Hello2', (object,), dict(sayHello=func))
h2 = Hello2()
h2.sayHello()
print(type(Hello2))
print(type(h2))

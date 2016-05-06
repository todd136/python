#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

class ListMetaClass(type):
        def __new__(cls, name, bases, attrs):
                attrs['add'] = lambda self, value: self.append(value)
                return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass = ListMetaClass):
        pass

l = MyList()
l2 = [1,2,3]
l.add(1)
print(l)
l2.insert(0,4)
l2.append(5)
print(l2)

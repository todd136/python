#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

class Chain(object):
        """docstring for Chain"""
        def __init__(self, path=''):
                super(Chain, self).__init__()
                self._path = path

        def __getattr__(self, path):
                return Chain('%s/%s' % (self._path, path))

        def users(self, userName):
                return Chain('%s/%s' % (self._path, 'users/' + userName))

        def __str__(self):
                return self._path

        __repr__ = __str__

print(Chain().status.user.timeline.list)
print(Chain().users('todd').repos)

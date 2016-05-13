#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

from collections import OrderedDict

class LastUpdatedOrderdDIct(OrderedDict):
        """docstring for LastUpdatedOrderdDIct"""
        def __init__(self, capacity):
                super(LastUpdatedOrderdDIct, self).__init__()
                self._capacity = capacity

        def __setitem__(self, key, value):
                containsKey = 1 if key in self else 0
                if len(self) - containsKey >= self._capacity:
                        last = self.popitem(last=False)
                        print('remove:', last)
                if containsKey:
                        pass

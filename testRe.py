#!/bin/usr/env python
# -*- encoding:utf-8 -*-

"""this python script is used to test regular expression"""

# __author__ ''

import re
s = '<h3>下一个你需要输入的数字是48950. </h3>'
pattern = '<h3>.*\d*.*</h3>'
numPattern = '\d+'
match = re.match(pattern, s)

if match:
    htmlItem = match.group(0)
    print(htmlItem)
    numList = re.findall(numPattern, htmlItem)
    if len(numList) > 0:
        numItem = numList[1]
        print(numItem)

# print(re.findall(pattern, s))
# print(re.findall('\d+','12 drummers drumming, 11 pipers piping, 10 lords a-leaping'))
# print(re.match('\d+','12 drummers drumming, 11 pipers piping, 10 lords a-leaping'))
# print(re.match('\d+','<h3>下一个你需要输入的数字是48950. </h3>'))

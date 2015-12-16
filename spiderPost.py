#!/usr/bin/env python3
# -*- encoding -*-

import urllib
import re
from urllib import request, parse

__author__ = 'todd'

regUrl = 'http://www.heibanke.com/lesson/crawler_ex01/'
pattern = '<h3>.*</h3>'
x = 0

data = {'csrfmiddlewaretoken': 'iPeR16hH6mSRdBALTHDJncvfiaVFWqRB',
      'username': 'name',
      'password': x}

while x < 31:
    data.update(password=x)
    encodeData = urllib.parse.urlencode(data).encode('ascii')
    with urllib.request.urlopen(regUrl, encodeData) as url:
        pageResponse = url.read()

        match = re.search(pattern, pageResponse.decode('utf-8'), re.S)
        if match:
            htmlItem = match.group(0)
            # print('htmlItem=', htmlItem)
            if htmlItem.find('恭喜') > 0:
                print(pageResponse.decode('utf-8'))
                exit()
            print(x)
    x += 1

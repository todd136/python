#!/usr/bin/env python3.4
# -*- encoding:utf-8 -*-

import re
import time
import urllib.request

__author__ = ''

regUrl = 'http://www.heibanke.com/lesson/crawler_ex00/'
pattern = '<h3>.*\d*.*</h3>'
numPattern = '\d+'
numItem = ''

while numItem is not None:
    regUrl = regUrl[0:regUrl.rfind('/')]+'/'+numItem
    print('regUrl =',regUrl)

    with urllib.request.urlopen(regUrl) as url:
        pageResponse = url.read()

    # print('page=', pageResponse.decode('utf-8'))

    match = re.search(pattern, pageResponse.decode('utf-8'), re.S)
    # print(content)
    if match:
        htmlItem = match.group(0)
        print('htmlItem=',htmlItem)
        numList = re.findall(numPattern, htmlItem)
        if len(numList) > 0:
            numItem = numList[1]
            # print(numItem)
    time.sleep(1)


# data = {'email':'test_134_134@sina.com', 'psw':'123!@#', 'imgvcode':'gdmm8', 
# 	'agreement':'true','forbin':'44bd3a8a153431f3d9db430549b8ea7b_1449040140', 
# 	'act':'1', 'extcode':'1fbab27ec2a0c1eeb0e8797399e62e1b'}

# params = urllib.urlencode(data)
# req = urllib2.Request(regUrl, params)
# response = urllib2.urlopen(req)
# html = response.read()

# print html
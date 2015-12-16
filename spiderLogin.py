#!/usr/bin/env python
# -*- encoding -*-

import urllib
import re
import requests
from urllib import request, parse
from http import cookiejar

__author__ = 'todd'

regUrl = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/'
pattern = '<h3>.*</h3>'
x = 0
cookie1 = ''

data = {'username': 'testspider', 'password': '123456'}

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'}

pageResponse = urllib.request.urlopen(regUrl)
# respHeaders = pageResponse.getheaders()

respHeader = pageResponse.getheader('Set-Cookie')

headerList = respHeader.split(';')
for header in headerList:
	if header.find('csrftoken') >= 0:
		cookie1 = header.split('=')[1]
		print(cookie1)

data['csrfmiddlewaretoken'] = cookie1

encodeData = urllib.parse.urlencode(data).encode('ascii')
req = urllib.request.Request(regUrl, encodeData, headers)

with urllib.request.urlopen(req) as url:
    pageResponse = url.read()
    print(pageResponse)

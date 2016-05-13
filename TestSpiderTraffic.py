#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

from urllib import request
from html.parser import HTMLParser
from html.entities import name2codepoint
import re

class MyHTMLParser(HTMLParser):
        def handle_starttag(self, name, attribute):
                pass

        def handle_endtag(self, name):
                pass

        def handle_startendtag(self, tag, attris):
                pass

        def handle_data(self, data):
            print(data)

        def handle_comment(self, data):
                pass #print('<!--', data, '-->')

        def handle_entityref(self, name):
                pass #print('&%s:' % name)

        def handle_charref(self, name):
                pass #print('&#%s:' % name)

def spiderData():
        req = request.Request('http://www.bjjtgl.gov.cn/')
        pattern = r'<div class="xianhao".*\d*.*?</div>'

        with request.urlopen(req) as f:
                print('status:', f.status, f.reason)
                if f.status == 200:
                        isMatch = re.search(pattern, f.read().decode('utf-8'), re.S)
                        if isMatch:
                                divData = isMatch.group(0)
                                print(divData)
                                # parser = MyHTMLParser()
                                # parser.feed(divData)

if __name__ == '__main__':
        spiderData()

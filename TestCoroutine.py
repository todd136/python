#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import time

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[Consumer] consuming %s...' % n)
        # time.sleep(2)
        r = '200 OK'

def produce(c):
    c.send(None)
    print(dir(c))
    n = 0
    while n < 5:
        n = n+1
        print('[Producer] Producing %s ...' % n)
        r = c.send(n)
        print('[Producer] Consumer returns: %s' % r)
    c.close()

c = consumer()
produce(c)

#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import socket,time, threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8888))

print('bind upd on 8888...')
while True:
        data, addr = s.recvfrom(1024)
        print('received from %s:%s' % addr)

        s.sendto(('hello, %s' % data.decode('utf-8')).encode('utf-8'), addr)

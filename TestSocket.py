#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
strBuffer = []
while True:
        d = s.recv(1024)
        if d:
             strBuffer.append(d)
        else:
                break
data = b''.join(strBuffer)
print(data)

#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import socket,time, threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'michael', b'tracy', b'sarah']:
        s.sendto(data, ('127.0.0.1', 8888))
        print(s.recv(1024).decode('utf-8'))
s.close()

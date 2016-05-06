#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import time, threading

local_school = threading.local()

def process_student():
        std = local_school.student
        print('hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
        local_school.student = name
        process_student()

t1 = threading.Thread(target = process_thread, args = ('alice',), name = 'thread-1')
t2 = threading.Thread(target = process_thread, args = ('bob',), name = 'thread-2')
t1.start()
t2.start()
t1.join()
t2.join()

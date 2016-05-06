#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import time, threading, multiprocessing

balance = 0
lock = threading.Lock()

def change_balance(n):
        global balance
        balance = balance + n
        balance = balance - n

def run_thread(n):
        for i  in range(100000):
                lock.acquire()
                try:
                        change_balance(n)
                except Exception as e:
                        raise e
                finally:
                        lock.release()

t1 = threading.Thread(target = run_thread, args = (1,))
t2 = threading.Thread(target = run_thread, args = (2,))

t1.start()
t2.start()
t1.join()
t2.join()
print('balance = ', balance)

def dead_loop():
        x = 0
        while True:
                x = x ^ 1

for x in range(multiprocessing.cpu_count()):
        t = threading.Thread(target = dead_loop)
        t.start()

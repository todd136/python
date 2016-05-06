#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

from multiprocessing import Process, Queue
import os, time, random

def write(q):
        print('process to write: %s' % os.getpid())
        for value in ['a', 'b', 'c']:
                print('put %s to queue...' % value)
                q.put(value)
                time.sleep(random.random()*2)

def read(q):
        print('process to read: %s' % os.getpid())
        while True:
                value = q.get(True)
                print('get %s from queue.' % value)

if __name__ == '__main__':
        q = Queue()
        pw = Process(target = write, args = (q,))
        pr = Process(target = read, args = (q,))

        pr.start()
        pw.start()
        pw.join()
        pr.terminate()

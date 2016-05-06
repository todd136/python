#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import os

print('Process (%s) start ...' % os.getpid())

pid = os.fork()

if pid == 0:
        print('I am child process (%s) , parent process = (%s)' % (os.getpid(), os.getppid()))
else:
        print('I am parent process(%s), child process = (%s)' % (os.getpid(), pid))

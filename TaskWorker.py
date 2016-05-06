#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

from multiprocessing.managers import BaseManager
import queue, time, sys

class QueueManager(BaseManager):
        pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('connecting to task manager server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
manager = QueueManager(address = (server_addr, 5000), authkey = b'abc')
# 从网络连接:
manager.connect()
# 获取Queue的对象:
task = manager.get_task_queue()
result = manager.get_result_queue()

# 从task队列取任务,并把结果写入result队列:
for x in range(20):
        try:
                n = task.get(timeout = 1)
                print('running task %dx%d ...' % (n, n))
                r = '%d x %d = %d' % (n, n, n*n)
                time.sleep(1)
                result.put(r)
        except Queue.Empty:
                print('task queue is empty.')

print('worker exit.')

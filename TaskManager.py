#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

from multiprocessing.managers import BaseManager
import queue, time, random

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

class QueueManager(BaseManager):
        pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable = lambda: task_queue)
QueueManager.register('get_result_queue', callable = lambda: result_queue)

# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address = ('', 5000), authkey = b'abc')
manager.start()

# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(20):
        n = random.randint(0, 10000)
        print('put task %d to taskqueue' % n)
        task.put(n)

# 从result队列读取结果:
print('try to get result...')
for x in range(20):
        r = result.get(timeout = 10)
        print('result %s ' % r)

manager.shutdown()
print('master exit')

#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import asyncio, threading

@asyncio.coroutine
def hello():
    print('hello, world! %s' % threading.currentThread())
    r = yield from asyncio.sleep(5)
    print('hello again! %s' % threading.currentThread())

@asyncio.coroutine
def hi():
    print('hi, world! %s' % threading.currentThread())
    r = yield from asyncio.sleep(2)
    print('hi again! %s' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hi()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost:%s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

# wgetLoop = asyncio.get_event_loop()
# wgetTasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# wgetLoop.run_until_complete(asyncio.wait(wgetTasks))
# wgetLoop.close()

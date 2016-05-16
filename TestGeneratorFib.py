#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

def fib(max):
    index, pre, result = 0, 0, 1
    while index < max:
        print(result)
        pre, result = result, pre + result
        index = index + 1
    return 'done'

fib(10)


def fibGen(max):
    index, pre, result = 0, 0, 1
    while index < max:
        yield result
        pre, result = result, pre + result
        index = index + 1
    return 'done'
f = fibGen(10)
print(next(f))
print(next(f))
print(next(f))

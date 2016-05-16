#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

def application(environ, start_response):
    start_response('200 OK', [('Context-Type', 'text/html')])
    body = '<h1>hello,%s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

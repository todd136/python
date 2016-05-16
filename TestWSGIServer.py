#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

from wsgiref.simple_server import make_server
from TestWSGI import application

httpd = make_server('', 8000, application)
print('Serving http on port 8000...')
httpd.serve_forever()

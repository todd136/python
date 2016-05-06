#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import subprocess

print('$nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('exit code:', r)

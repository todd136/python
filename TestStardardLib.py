#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import os
print(os.getcwd())
print(dir(os))
print(help(os))

from datetime import date
now = date.today()
print(now)

birthdate = date(1982,12,20)
age = now - birthdate

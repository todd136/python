#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import re
print(re.match(r'''\d{3}-\d{3,8}$''', '010-12345'))

print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))

re_telephone = re.compile(r'(\d{3})-(\d{3,8})')
print(type(re_telephone))
print(re_telephone.match('010-12345').groups())

# re_email = re.compile(r'^[0-9a-zA-Z]+[0-9a-zA-Z\.]+\@[a-zA-Z]+\.[a-zA-Z]+')
re_email = re.compile(r'(\w+)(\.?)(\w+)\@(\w+)\.(\w+)')
print(re_email.match('someone@gmail.com'))
print(re_email.match('someone@!@gmail.com'))
print(re_email.match('bill.gates@microsoft.com'))

re_name_email = re.compile(r'(\<\w+\s+\w+\>)\s+(\w+\.?\w+\@\w+\.\w+)')
print(re_name_email.match('<Tom Paris> tom@voyager.org').groups())

#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import hashlib

db = {
}

def calc_md5(password):
        md5 = hashlib.md5()
        md5.update((password + 'salt').encode('utf-8'))
        # print(md5.hexdigest())

def login(user, passwd):
        hexPasswd = calc_md5(passwd)
        if hexPasswd == db[user]:
                print('permit to login')
        else:
                print('name or password is not correct')

def register(userName, password):
        hexPassword = calc_md5(password + userName)
        db[userName] = hexPassword

if __name__ == '__main__':
        register('bob', '123456')
        login('bob', '123456')

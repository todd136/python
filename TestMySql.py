#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(user='root', password='123456', database='blog')
cursor = conn.cursor()

createSql = 'create table user(id varchar(20) primary key, name varchar(20))'
# cursor.execute(createSql)

# cursor.execute('insert into user(id, name) values (%s, %s)', ['1', 'todd'])

selectSql = 'select * from user'
cursor.execute(selectSql)
results = cursor.fetchall()
print(results)

conn.commit()
cursor.close()
conn.close()

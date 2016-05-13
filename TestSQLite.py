#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

createSql = 'create table user(id varchar(20) primary key, name varchar(20), score int) '
cursor.execute(createSql)

insertSql = 'insert into user(id, name, score) values (\'A-001\', \'todd\', 95)'
insertSql2 = 'insert into user(id, name, score) values (\'A-002\', \'Adam\', 62)'
insertSql3 = 'insert into user(id, name, score) values (\'A-003\', \'Lisa\', 78)'

cursor.execute(insertSql)
cursor.execute(insertSql2)
cursor.execute(insertSql3)
print('inserted into tables, rows = ', cursor.rowcount)

cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
        try:
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                selSql = 'select name from user where score >= ? and score <= ? order by score'
                cursor.execute(selSql, (low, high))
                values = cursor.fetchall()
                l = []
                for v in values:
                        l.append(v[0])
                print('score between %s and %s are:%s' % (low, high, l))


                deleteSql = 'drop table user'
                cursor.execute(deleteSql)
                print('deleted tables, count = ',cursor.rowcount)
        except Exception as e:
                raise e
        finally:
                cursor.close()
                conn.commit()
                conn.close()

if __name__ == '__main__':
        get_score_in(90, 100)

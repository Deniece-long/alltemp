#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

#连接mysql数据库，
#打开数据库链接
username ="root"
password ="070809"
databaseName="testdb"
db = MySQLdb.connect("localhost",username,password,databaseName)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

#插入语句第一种写法
# sql ="""INSERT INTO EMPLOYEE2(
#         FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)VALUES('kan','senE',49,'1',5000.0
# );"""

#插入语句第二种写法
sql ="INSERT INTO EMPLOYEE2(FIRST_NAME,\
      LAST_NAME,AGE,SEX,INCOME)\
      VALUES('%s','%s','%d','%c','%f')"%\
     ('new','em',21,'M',4000);
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()


# 关闭数据库连接
db.close()
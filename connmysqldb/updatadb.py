#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb


#连接mysql数据库，数据库更新
#打开数据库链接
username ="root"
password ="070809"
databaseName="testdb"
db = MySQLdb.connect("localhost",username,password,databaseName)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

#更新语句
sql ="UPDATE EMPLOYEE2 SET AGE = AGE +1 WHERE SEX ='%c'" % ('M')
try:
    #执行sql语句
    cursor.execute(sql)
    #提交到数据库
    db.commit()

except:
    #发生错误时回滚
    db.rollback()
# 关闭数据库连接
db.close()
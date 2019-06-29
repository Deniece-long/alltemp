#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb


#连接mysql数据库，删除数据库中的数据
#打开数据库链接
username ="root"
password ="070809"
databaseName="testdb"
db = MySQLdb.connect("localhost",username,password,databaseName)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

#更新语句
#sql ="DELETE FROM EMPLOYEE2 WHERE AGE >'%d'"%(20)
sql ="DELETE FROM EMPLOYEE2 WHERE FIRST_NAME='%s'"%('MON')
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
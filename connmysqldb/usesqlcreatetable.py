#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

#连接mysql数据库，删除存在的表，然后创建新表
#打开数据库链接
username ="root"
password ="070809"
databaseName="testdb"
db = MySQLdb.connect("localhost",username,password,databaseName)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句,如果数据库中已经存在表employee则删除
cursor.execute("DROP TABLE IF EXISTS employee2")

#穿件数据表的SQL语句
sql ="""CREATE TABLE EMPLOYEE2(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT
)"""
cursor.execute(sql)
sql2 ="""INSERT INTO EMPLOYEE2(
         FIRST_NAME,LASET_NAME,AGE,SEX,INCOME)VALUES('Mac','Jhone','20','1','5000'
)"""
try:
    cursor.execute(sql2)
    db.commit()
except:
    db.rollback()


# 关闭数据库连接
db.close()
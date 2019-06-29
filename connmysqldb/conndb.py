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

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()
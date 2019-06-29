#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

#连接mysql数据库，查询数据
#打开数据库链接
username ="root"
password ="070809"
databaseName="testdb"
db = MySQLdb.connect("localhost",username,password,databaseName)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

#查询语句
sql ="SELECT * FROM EMPLOYEE2\
     WHERE INCOME >'%d'" %(1000)


try:
    #执行sql语句
    cursor.execute(sql)
    #获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        #打印结果
        print("fname=%s,lname=%s,age=%d,sex=%s.income=%f"%\
              (fname,lname,age,sex,income))
except:
    print("error:unable to fecth data")


# 关闭数据库连接
db.close()
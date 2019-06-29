#让网页JS渲染数据加载完全了才开始解析

#1.分析JS源码 找出请求 自己模拟实现 难度比较高 麻烦
#2.模拟浏览器实现 三方库多 简单 但是效率会慢一点
#2Selenium是一个用于Web应用程序测试的工具
#Phantom JS是一个服务器端的 JavaScript API 的 WebKit

import csv
from selenium import webdriver
import urllib.request
import socket
import urllib3
import re
import requests
from bs4 import BeautifulSoup

#读取contenturl.csv文件，读取第二列的url进行爬虫，获取源代码

count =0
with open('test.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    #column = [row for row in reader] 所有列
    column = [row['url'] for row in reader] #取得只有url的列，这些url是放在列表中的
print(column)
print(column[0])
print(len(column))

for i in column:
    print(str(i))
    print(count)
    print(i)
    try:
        #urlopen()加载出来的都是还没有加载js数据之前的
        #beautifulsoup解
        page = urllib.request.urlopen(str(i), timeout=10)  # 响应时间为5秒
        content = page.read()
        # soup = BeautifulSoup(content)
        # print(soup.script.string)
        # polist = soup.findAll('src="(.*?)"')
        # print(polist[0].contents[0])

        # allcontent = str(content,encoding='utf-8')
        # print(type(allcontent))
        # file = open("E://phishtankdataset2//"+str(count)+'.text','wb')
        # pattern ="(.*?)+(\.)+js"
        # mat = re.compile(pattern)
        # print(mat.findall(allcontent,re.S))
        print('能找到')
        #else:
            #print('未能找到')
            #html = requests.get('')
        #file.write(content)

        pic_js = re.findall('script src="(.*?)"',content,re.S)
        n=0
        for each in pic_js:
            print('now downloading:'+each)
            pic = requests.get(each)
            fp = open(''+str(n)+'.js','wb')
            fp.write(pic.content)
            fp.close()
            n += 1
    except socket.timeout as e:
        print(type(e))
    except:
        print("404 or time out")  # 请求超时或者未能链接
    count += 1
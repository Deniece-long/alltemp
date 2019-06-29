import csv
from selenium import webdriver
import urllib.request
import socket
import urllib3

#读取contenturl.csv文件，读取第二列的url进行爬虫，获取源代码

count =0
with open('contenturl.csv','r') as csvfile:
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
        page = urllib.request.urlopen(str(i), timeout=10)  # 响应时间为5秒
        content = page.read()
        print("---")
        file = open("E://data//phishtankdata//"+str(count)+'.text','wb')
        file.write(content)
    except socket.timeout as e:
        print(type(e))
    except:
        print("404 or time out")  # 请求超时或者未能链接
    count += 1



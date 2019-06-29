#coding:utf-8
import os
import urllib.request

#没用
def getContent():
    #获取url所对应的内容，并进行异常的捕获
    i=0
    url=open("test.text")
    next(url)
    for urlcontent in url:
        try:
            page = urllib.request.urlopen(urlcontent,timeout=5)
            i +=1
            contents = page.read()
            f = open("TestContent"+str(i)+".text","w+")
            f.write(contents)
            print(i)
        except:
            print("404 or time out")

if __name__ == '__main__':
    getContent()
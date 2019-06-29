import urllib.request
import os

#从phishtank网站中获取恶意的url链接，
#其中72f150fd2e4e8cb77257e0ccf8c4e02af0eae7f4bc9366160fb7e4fc9e362e79是自己在phishtank登录申请的API key
#参考链接：https://blog.csdn.net/Danielntz/article/details/52535879

url = "http://data.phishtank.com/data/72f150fd2e4e8cb77257e0ccf8c4e02af0eae7f4bc9366160fb7e4fc9e362e79/online-valid.csv"
page = urllib.request.urlopen(url)
content = page.read()
print(content)
print(type(content))
f = open("contenturl.csv","wb") #wb是二进制的写入
f.write(content)
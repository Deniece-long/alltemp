# coding=UTF-8
import safebrowsing
import json
import xlwt
apikey = 'AIzaSyDtw1Gcp36xSOiCveF0Dt-bqU8WhrYT4Yk'
sb = safebrowsing.LookupAPI(apikey)
resp = sb.threat_matches_find('ihaveaproblem.info')
# resp=json.dumps(resp)
a = []
for i in resp["matches"]:
    #print i['threat']  只截取url这一块
    a.append(i['threat'])#把url放入列表中
print(a)#可以不要这句，只作为测试
try:
    f = open('Alexa500.txt','w')
    for item in a :
        if(str(item)!="{u'url': u'ihaveaproblem.info'}"):#去掉单独的url信息
            f.write(str(item)+'\n')
    f.close()
except IOError:
    print("fail to open file")
print(resp) #可以去掉，只是整体的JSON对象
import hashlib
import filecmp
#比较同目录下的<script> txt文本是否相同，把不同写出来
# def getHash(f):
#     line = f.readline()
#     hash = hashlib.md5()
#     while(line):
#         hash.update(line)
#         line = f.readline()
#     return hash.hexdigest()
# def IsHashEqual(f1,f2):
#     str1 = getHash(f1)
#     str2 = getHash(f2)
#     return str1==str2
# if __name__ == '__main__':
#
#     f1=open("f://dataset//Javascriptsolosample//test//1.txt","rb")
#     f2=open("f://dataset//Javascriptsolosample//test//2.txt","rb")
#     print(IsHashEqual(f1,f2))
print(filecmp.cmp('f://dataset//Javascriptsolosample//test//1.txt','f://dataset//Javascriptsolosample//test//2.txt'))
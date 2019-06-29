import numpy
from PIL import Image
import binascii
import os

#读取txt文件，将其转为二进制矩阵和数值

allFileNum =0 #所有文件数
a1 =[]
def printPath(level,path):
    global allFileNum
    dirList =[]  #文件夹列表
    fileList =[]  #文件列表 
    files = os.listdir(path)
    dirList.append(str(level)) # 先添加目录级别
    for f in files:
        if(os.path.isdir(path+'/'+f)):
            if(f[0]=='.'): # 排除隐藏文件夹。因为隐藏文件夹过多
                pass
            else:
                dirList.append(f)# 添加非隐藏文件夹
        if(os.path.isfile(path+'/'+f)):
            fileList.append(f)# 添加文件
    i_dl =0# 当一个标志使用，文件夹列表第一个级别不打印 
    for dl in dirList:
        if(i_dl==0):
            i_dl=i_dl+1
        else:
            print('_'*(int(dirList[0])),dl)# 打印至控制台，不是第一个的目录
            printPath((int(dirList[0])+1),path+'/'+dl)# 打印目录下的所有文件夹和文件，目录级别+1
    for fl in fileList:
        # print('_'*(int(dirList[0])),fl)
        a1.append(fl)
        allFileNum = allFileNum+1



#函数来自于文献，把文件转成图像
def getMatrixfrom_bin(filename,width):
    with open(filename,'rb') as f:
        content = f.read()
        # print(content)   #测试打印输出
    hexst = binascii.hexlify(content)   #将二进制文件转换为十六进制字符串
    # print(hexst)       #测试打印输出
    fh = numpy.array([int(hexst[i:i+2],16)for i in range(0,len(hexst),2)])   #按字节分割
    # print(fh)            #测试打印输出
    rn = len(fh)//width
    # print(rn)            #测试打印输出
    fh = numpy.reshape(fh[:rn*width],(-1,width))    #根据设定的宽度生成矩阵
    # fh = numpy.uint8(fh)
    # numpy.savetxt("fh.txt",fh)   #测试
    # print(fh.shape)
    return fh


#当转换后文件的行数小于512时，给矩阵补零至512行输出，然后保存为矩阵数的形式
def gudingWidth(fh,m):
    b = numpy.zeros((1, 28))  # 当矩阵函数不足512时，补零至512行
    # print(b)             #测试打印输出
    # 为矩阵的行数不足512行补零
    while m <28:
        fh = numpy.row_stack((fh, b))  # 循环补零，即为矩阵增行
        # print(fh.shape)  #测试打印输出
        m = m + 1
    fh = numpy.uint8(fh)
    # 存储字节少的矩阵的数值，是科学计算表示方法
    filename = 'E:/ceshi/test/zhuanhoutxt/'+h+'.txt'#保存txt的目录
    numpy.savetxt(filename, fh)
    return fh

#当转换后文件的行数大于512时，按照512的倍数进行截取，余数不足512行的为矩阵补零，最后for循环保存为矩阵数文本
def jieQu(fh,m):
    n=m//28+1
    y=28-m%28
    print ("y",y)    #测，得出有几个512的矩阵
    c = numpy.zeros((1, 28))
    #取余后补足512行才可截取
    for i in range(0,y):
        fh = numpy.row_stack((fh, c))  # 循环补零，即为矩阵增行
    # print("测",fh.shape)  #测试打印输出
    for i in range(0,n):
        arry=fh[i*28:(i+1)*28,]
        # print(arry.shape)  #测试打印输出
        # print(type(arry))  #测试打印输出

        # print(arry)        #测试打印输出
        sa = numpy.uint8(arry)  #将矩阵变成无符号整形

        # print(sa)            #测试打印输出
        out = Image.fromarray(sa) #保存为图片
        out.save('E:/ceshi/test/attackimage/browser_vulnerabilities/'+h+'_'+str(i)+'.png')
        #保存矩阵的数值，用科学技术法表示
        filename = 'E:/ceshi/test/zhuanhoutxt/'+h + '_'+str(i) + ".txt"
        numpy.savetxt(filename, arry)


#主函数
if __name__ == '__main__':
    dir1='E:/soloscripttest/benginJS/1_1/'#之前的实验数据
    dir2 = 'E:/soloscripttest/29k/'#之前的实验数据目录
    #str='E:/maldatasettxt/90hang/'

    printPath(1, 'E:/ceshi/test/codefile/browser_vulnerabilities/')#读取目录下的字符文件
    print('文件数=', allFileNum)
    for h in a1:
        filename = 'E:/ceshi/test/codefile/browser_vulnerabilities/' + h #代码文件所在目录
        fh = getMatrixfrom_bin(filename,28)
        # 确定矩阵的高度为512
        arry = numpy.shape(fh)  # 取得矩阵的高度和宽度，矩阵宽度512
        print(arry)          #测试打印输出
        m = arry[0]  # arry两个参数，arry[0]取得矩阵行数，arry[1]取得矩阵列数
        if m <= 28:
            out=gudingWidth(fh,m)
            im = Image.fromarray(out)
            im.save('E:/ceshi/test/attackimage/browser_vulnerabilities/'+h+'.png')#小于224图像的保存
            print(out)
        else:
            jieQu(fh,m)
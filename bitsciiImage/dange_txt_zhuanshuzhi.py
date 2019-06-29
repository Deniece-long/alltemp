import numpy
from PIL import Image
import binascii
#读取单个文件(文件格式可以是txt)，将文件转矩阵后的数值保存为txt文件

#文件所在目录
filename = 'F:/pycharm/shiyan/Pro_py3.5/bitsciiImage/codefile/20160307_a99dd01bce1b27ebd84e464d74081c17.txt'

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
    fh = numpy.uint8(fh)
    # numpy.savetxt("fh.txt",fh)   #测试
    # print(fh.shape)
    return fh


#当转换后文件的行数小于512时，给矩阵补零至512行输出，然后保存为矩阵数的形式
def gudingWidth(fh,m):
    b = numpy.zeros((1, 512))  # 当矩阵函数不足512时，补零至512行
    # print(b)             #测试打印输出
    # 为矩阵的行数不足512行补零
    while m < 512:
        fh = numpy.row_stack((fh, b))  # 循环补零，即为矩阵增行
        # print(fh.shape)  #测试打印输出
        m = m + 1
        # 当矩阵的行数大于512行时，只截取512行的矩阵内容
    #转矩阵后txt文件保存的位置
    filename='F:/pycharm/shiyan/Pro_py3.5/bitsciiImage/image/20160307_a99dd01bce1b27ebd84e464d74081c17.txt'
    numpy.savetxt(filename,fh)

#当转换后文件的行数大于512时，按照512的倍数进行截取，余数不足512行的为矩阵补零，最后for循环保存为矩阵数文本
def jieQu(fh,m):
    n=m//512+1
    y=512-m%512
    print ("y",y)
    c = numpy.zeros((1, 512))
    #取余后补足512行才可截取
    for i in range(0,y):
        fh = numpy.row_stack((fh, c))  # 循环补零，即为矩阵增行
    print("测",fh.shape)  #测试打印输出
    for i in range(0,n):
        arry=fh[i*512:(i+1)*512,]
        print(arry.shape)
        #转矩阵后txt文件保存的位置
        filename = 'F:/pycharm/shiyan/Pro_py3.5/bitsciiImage/image/20160307_a99dd01bce1b27ebd84e464d74081c17' + str(i) + ".txt"

        numpy.savetxt(filename,arry)


#主函数
if __name__ == '__main__':
    fh = getMatrixfrom_bin(filename, 512)
    # 确定矩阵的高度为512
    arry = numpy.shape(fh)  # 取得矩阵的高度和宽度，矩阵宽度512
    print(arry)          #测试打印输出
    m = arry[0]  # arry两个参数，arry[0]取得矩阵行数，arry[1]取得矩阵列数
    if m <= 512:
        gudingWidth(fh,m)
    else:
        jieQu(fh,m)
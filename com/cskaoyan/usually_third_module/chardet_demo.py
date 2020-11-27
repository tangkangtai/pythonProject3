#如果安装了Anaconda，chardet就已经可以用了,
#否则pip安装    pip install chardet

#当我们拿到一个bytes 就可以检测编码
import chardet

x = chardet.detect(b'hello world')
print(x) #编码是ascii      confidence字段 表示检测的概率是1.0(100%)


x = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(x))

x = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(x))

import codecs


f = codecs.open('e:/pytest.txt')

#放文件不存在时 open()函数会抛出IOError


#当文件打开成功,f.read()方法可以一次读取文件的全部内容  str对象表示

str = f.read()

f.close()

print(str)

#---------------------------
print('---------------------')
#---------------------------

#with后面接的对象返回的结果赋值给f
#with后面的返回对象要求必须两 __enter__()/__exit__()这两个方法
with codecs.open(r'e:/pytest.txt') as f:
    data = f.read()

print(data)
#-----------------------------------
#调用read()会一次性读取文件的全部内容 如果文件太大，内存爆了
#可以反复调用 read(size)方法
#readline()可以每次读取一行内容  并按行返回list

#不确定文件大小 反复调用read(size)
#配置文件 readlin()最方便
f = codecs.open('e:/pytest.txt')
for line in f.readline():
    print(line.strip())
f.close()
#可能遇到UnicodeDecodeError error参数 表示直接忽略
f = codecs.open('e:/pytest.txt',errors='ignore')
f.close()
#===========写文件==========================
f = codecs.open('e:/pytest.txt','w')
f.write('Hello world, 你好呀')
#写文件务必调用f.close()来关闭文件
#因为写文件时 操作系统不会立即把数据写入磁盘 而是放到内存缓存起来 空闲慢慢写入

f.close()
#用with语句比较保险
with codecs.open('e:/pytest.txt','a') as f:
    f.write('Hello world!')


#

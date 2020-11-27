#操作文件和目录
#内置os函数
import os
#posix 系统是Linux Unix Mac OS X
print(os.name) #nt  windows

#详细系统信息
# print(os.uname)  #windows不提供

#环境变量
print(os.environ)
print('-----------------------')
print(os.environ.get('PATH'))

print('-----------------')
print(os.environ.get('x','default'))

#操作文件和目录

#察看当前目录的绝对路径

print(os.path.abspath('.'))

#在某个目录下创建一个新目录，

#注意:  把两个路径合成一个时 不要拼接字符串 而要通过os.path.join()函数 这样可以正确处理
#不同操作系统的路径分隔符，     同样，当需要拆分字符串时，而要通过os.path.split()函数
# 这样可以把一个路径拆分为两部分 后一部分总是最后级别的目录或文件名
print(os.path.join('e:/','testdir'))

#拆分
print(os.path.split('E:\PycharmProjects\pythonProject\com\cskaoyan\IOProgramming'))

#os.path.splittext()可以直接让你得到文件扩展名
print(os.path.splitext('e:/pytest.txt'))
#新建目录
# os.mkdir('e:/testdir')
#删除目录
# os.rmdir('e:/testdir')


#对文件重命名
# os.rename('test.txt','test.py')
#删除文件
# os.remove('test.py')

print('-------------------')
print(os.listdir('.'))
print(os.listdir('e:/'))
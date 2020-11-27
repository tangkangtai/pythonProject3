#进程之间的通信
#python的multiprocessing模块包装了底层的机制 提供了Queue,Pipes 多种方式来交换数据

#我们已Queue为例子  在父进程中创建两个子进程  一个往Queue里写数据  一个从Queue里读数据

from multiprocessing import Process,Queue
import os, time, random


#写数据进程执行的代码
def write(q):
    print('Process to write: %s' %os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

#读数据进程执行的代码
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read, args=(q,))

    #启动子线程pw,写入
    pw.start()
    #启动子线程pr 读取
    pr.start()

    pw.join()
    #pr进程里面有死循环 无法等待结束 强行终止
    pr.terminate()
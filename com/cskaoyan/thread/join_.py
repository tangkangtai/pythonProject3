#join()函数
#在进程中可以阻塞主进程的执行 直到等待所有子进程全部完成之后 才继续运行主线程后面的代码
import threading
import time

def test(num):
    time.sleep(1)
    print(num)

#定义一个用来装子线程的列表
threads = []
for i in range(5):
    #target指定子线程要执行的 函数 ， args指定该函数 需要传入的参数
    thread = threading.Thread(target=test,args=[i])
    threads.append(thread)

for i in threads:
    #for 循环执行 threads 列表里面的全部线程 没有用join()线程是无序执行的
    # 连最后一句 print('end') 可能比所有子线程都要先执行
    #不加join 主线程先执行完 完全没有等待子线程全部执行完之后再执行，而且子线程都是无序执行完毕的
    i.start()
    i.join()

print('END')
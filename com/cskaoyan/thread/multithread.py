#Lock
#多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
#而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改

import time, threading

balance = 0
lock = threading.Lock()
def change_it(n):
    #先存后取
    global balance
    balance = balance + n
    balance = balance - n

# def run_thread(n):
#     for i in range(2000000):
#         change_it(n)

#---------------------------------
def run_thread(n):
    for i in range(100000):
        #先获取锁
        lock.acquire()
        try:
            #放心的改吧
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

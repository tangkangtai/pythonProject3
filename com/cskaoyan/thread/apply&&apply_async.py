import time
import multiprocessing

def doIt(num):
    print("Process num is : %s" %num)
    time.sleep(1)
    print('process %s end ' % num)

if __name__ == '__main__':

    print('mainProcess start')

    #记录一下开始执行的时间
    start_time = time.time()

    #创建三个子进程
    pool = multiprocessing.Pool(3)
    print('child start')
    for i in range(3):
        # pool.apply(doIt,[i])
        pool.apply_async(doIt,[i])

    pool.close()

    #join()的文章可以知道他可以阻塞主进程, 等待所有子进程结束之后再运行
    #需要在前面加上 close()
    pool.join()
    print('mainProcess done time:%s s' %(time.time() - start_time))
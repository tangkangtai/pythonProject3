# 分布式进程

# 在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，
# 而Thread最多只能分布到同一台机器的多个CPU上

# Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。
# 一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信
import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass


if __name__ == '__main__':

    # 把两个Queue都注册到网络上 callable参数都关联了Queue对象
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)

    # 绑定端口5000   设置验证码 'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    # 启动Queue
    manager.start()

    # 获得通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    # 从 result队列读取结果
    print('Try get results...')

    for i in range(10):
        # 阻塞timeout秒
        r = result.get(timeout=10)
        print('Result: %s' % r)

    # 关闭
    manager.shutdown()
    print('master exit.')

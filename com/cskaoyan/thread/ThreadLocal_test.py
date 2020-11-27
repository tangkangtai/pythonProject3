# 在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，
# 因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁
class Student(object):
    pass

# def process_student(name):
#     std = Student(name)
#
#     do_task_1(std)
#     do_task_2(std)

# def do_task_1(std):
#
#     do_subtask_1(std)
#     do_subtask_2(std)
#
# def do_task_2(std):
#
#     do_subtask_2(std)
#     do_subtask_2(std)

#------------------------------------------

#-----------------------------------------
#用一个全局dict存放所有的student对象
# 然后以thread自身作为key获得线程对应的Student
import threading
global_dict = {}




def std_thread(name):
    std = Student(name)
    #把std放到全局变量global_dict中
    global_dict[threading.current_thread()]
    do_task_1()
    do_task_2()

def do_task_1():
    #不传入std 而是根据当前线程直接查找
    std = global_dict[threading.current_thread()]

def do_task_2():
    std = global_dict[threading.current_thread()]

#----------------------------------------------
#----------------------------------------------
#全局变量local_school就是一个ThreadLocal对象
#每个Thread对它都可以读写student属性 但互不影响
local_school = threading.local()

def process_student():
    #获取当前线程关联的student
    std = local_school.student
    print('Hello,%s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocal的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread, args = ('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
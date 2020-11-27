#debug
import logging
#四个指定记录信息的级别 有debug,info,warning ,error
logging.basicConfig(level=logging.INFO)


def foo(s):
    n = int(s)
    # print('>>>n = %d' %n)
    #n != 0 应该为True 否则 后面代码会报错
    #断言失败 assert语句本身就会跑出AssertionError:
    assert n != 0 ,'n is zero!'
    return 10 / 0

def main():
    foo('0')

s = '0'
n = int(s)
logging.info('n= %d' %n)
print(10/n)


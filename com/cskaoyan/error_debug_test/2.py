
#记录错误
import logging
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        #日志类打印错误
        logging.exception(e)

main()
print('END')
#抛出错误

#因为错误时class 捕获一个错误时捕获该类的一个实例

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)

    return 10 / n

# foo('0')
def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError')
        #raise语句如果不带参数 就会把当前错误原样抛出
        raise

bar()
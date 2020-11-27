#错误处理

def foo():
    r = some_function()

    if r == (-1):
        return (-1)

    return r

def bar():
    r = foo()
    if r == (-1):
        print("Error")
    else:
        pass

try:
    print('try.....')
    # r = 10 / 0
    r = 10 / int('a')

    print('result: ', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('except:', e)
else:
    print('no error')
finally:
    print('finally....')
print('END')



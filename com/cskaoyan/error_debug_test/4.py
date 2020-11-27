from functools import reduce

def str2num(s):
    try:
        return int(s)
    except:
        return float(s)

def calc(exp):
    ss = exp.split('+') #['99','88','7.6']
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

# ss = '99+88+7.6'.split('+')
# print(ss)
# ns = map(str2num,ss)
# print(list(ns))

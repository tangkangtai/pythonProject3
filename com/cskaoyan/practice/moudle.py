
#import math
from math import pow, sin, log

#print(math.pow(2, 0.5))
print(pow(2,0.5))
#print(math.pi)

print(sin(3.14))

#模块方法同名冲突
import math,logging
print(math.log(10))
print(logging.log(10,'something'))


#导入模块不存在时 解释器会报错
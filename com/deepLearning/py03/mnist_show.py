import sys, os

# sys.path是个列表，所以在末尾添加目录是很容易的，
# 用sys.path.append就行了。当这个append执行完之后，新目录即时起效，
# 以后的每次import操作都可能会检查这个目录

#os.pardir  获取当前目录的父目录字符串名：('..')
#---------------------------------------------
#sys.path 动态改变python搜索路径
#  sys.path是个列表，所以在末尾添加目录是很容易的，用sys.path.append就行了。
#  当这个append执行完之后，新目录即时起效，以后的每次import操作都可能会检查这个目录
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    #image 转换成 array  img = np.asarray(image)
    #-------------------
    # 实现array到image的转换
    #img.flags.writeable = True   更改文件的读写
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

img = x_train[0]
label = t_train[0]
print(label)

print(img.shape)
img = img.reshape(28, 28)#把图像的形状变为原来的尺寸
print(img.shape)

img_show(img)
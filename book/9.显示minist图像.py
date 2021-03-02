import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
# PIL(Python Image Library) 图像显示模块
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

# flatten=True 时读入的图像是以一列（一维）NumPy 数组的形式保存的
# 因此，显示图像时，需要把它变为原来的28像素 × 28
# 像素的形状。可以通过 reshape() 方法的参数指定期望的形状，更改NumPy
# 数组的形状。此外，还需要把保存为NumPy数组的图像数据转换为PIL用
# 的数据对象，这个转换处理由 Image.fromarray() 来完成

#
(x_train,t_train),(x_test, t_test) = load_mnist(flatten=True, normalize=False)
img = x_train[0]
label = t_train[0]
print(label)

print(img.shape)    #(784,)
img = img.reshape(28, 28)   # 把图像的形状变成原来的尺寸
print(img.shape)    # (28,28)

img_show(img)






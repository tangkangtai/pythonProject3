#pillow
#PIL:python imaging Library ，python平台事实上的图像处理标准库
#功能强大 API简单易用
from PIL import Image , ImageFilter

#打开一个jpg图像文件 注意是当前路径
im = Image.open('C:/Users/tang/Pictures/test.jpg')
#
w,h = im.size

print('Original image size:%sx%s' %(w,h))

#resize()方法可以缩小也可以放大 而thumbnail方法只能缩小
#缩放到50%
im.thumbnail((w//2,h//2))
print('Resize image to: %sx%s' %(w//2,h//2))

#把缩放后的图像用jpeg格式保存
im.save('thumbnail.jpg','jpeg')


#模糊效果
im1 = Image.open('C:/Users/tang/Pictures/test.jpg')
#应用模糊滤镜
im2 = im1.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')
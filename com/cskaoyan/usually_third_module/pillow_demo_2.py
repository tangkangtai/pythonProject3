from PIL import Image,ImageDraw,ImageFont,ImageFilter

import random
#随机字母
def rndChar():
    # 0-9   =》 48-57
    # a-z   =>  97-122
    # A-Z   =>  65-90
    # chr()用一个整数作参数, 返回一个对应的字符
    return chr(random.randint(65,90))

#随机颜色1
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

#随机颜色2
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

#240*60
width = 60 * 4
height = 60
#RGB(0,0,0)黑色   (255,255,255)白色
#Image.new('RGB','')  颜色不传默认是黑色
image = Image.new('RGB',(width,height),(255,255,255))
#image.show()
#创建字体对象
font = ImageFont.truetype('arial.ttf',36)

#创建draw对象 ,新建画布绘画对象
draw = ImageDraw.Draw(image)

#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())

#输出文字
for t in range(4):
    #在坐标为(60*t+10,10) 处开始画
    #左上角为画布（0,0）点
    draw.text((60*t + 10,10),rndChar(),font=font,fill=rndColor2())

#模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')

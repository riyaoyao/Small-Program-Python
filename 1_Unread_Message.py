# 程序说明：为微信头像右上角添加未读信息个数
from PIL import Image, ImageDraw, ImageFont
# PIL为python的图像处理库
# 读入图像
im = Image.open('./Imag/博客的头像.jpeg', 'r')
# 获取宽度 高度
w, h = im.size
# 创建一个字体对象
font = ImageFont.truetype('C:\\WINDOWS\\Fonts\\SIMYOU.ttf', int(h/7))
# 在指定位置（text里头为左上角位置，内容，颜色）绘制图像(pieslice里头 x y start end)
ImageDraw.Draw(im).pieslice([(w-h/5, 0),(w, h/5)],0,360,fill='red')
ImageDraw.Draw(im).text( (w*0.88, h*0.02), '3', fill='white',font= font)

im.show()
#im.save('./Imag/博客的头像_1.jpeg')

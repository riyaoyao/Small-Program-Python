# 程序说明：将目录下的所有照片的分辨率统一
from PIL import Image
import os

def ResizeImag(filename, w, h):
    for i in os.listdir(filename):                 #遍历文件夹
        if os.path.splitext(i)[1]=='.jpeg':        #找到图片
            im = Image.open(os.path.join(filename, i))
            im.thumbnail((w, h))
            im.save(filename + 'new'+i)


ResizeImag("./File/", 300, 300)



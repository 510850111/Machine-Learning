#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
showHideMessage.py

在之前的信息隐藏后,肉眼观察载体图像,仍无法察觉与之前相比有任何变化.
解密信息与隐藏信息相反,是隐藏信息的逆过程
图像隐藏信息解密原理:
    提取载体文件中蓝色像素值为奇数的像素点
@author: Oscar
"""

import cv2
import numpy as np

fn = "saveImg/secretImg.png"
if __name__ == "__main__":
    print(u"正在读取文件......")
    img = cv2.imread(fn)
    height = img.shape[0]
    width = img.shape[1]
    imgInfo = np.zeros((height,width,3),np.uint8)
    for j in range(0,height):
        for i in range(0,width):
            if (img[j,i,0] % 2) == 1:
                #如果蓝色值为奇数,则该像素点为文字
                imgInfo[j,i,1] = 255
        print(u"正在解密......",round(100*j / height),"%")
    cv2.imshow('imgInfo',imgInfo)
    #cv2.imwrite(fn,imgInfo)
    cv2.waitKey()
    cv2.destroyAllWindows()













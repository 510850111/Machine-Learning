#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
平铺图片

@author: Oscar
"""
import cv2
import numpy as np

fn = "img/6.1.jpg"
if __name__ == '__main__':
    print('loading %s...' %fn)
    img = cv2.imread(fn)
    height = img.shape[0]
    width = img.shape[1]
    
    #横向平铺5个像素
    sz1 = width * 5
    #纵向平铺2像素
    sz0 = height * 2
    #创建空白图像,然后接将图片排列
    myimg = np.zeros((sz0,sz1,3),np.uint8)
    #逐个图像复制
    img_x = 0
    img_y = 0
    for now_y in range(0,sz0):
        #增加行数
        for now_x in range(0,sz1):
            #复制对应位置的图像像素点
            myimg[now_y,now_x,0] = img[img_y,img_x,0]
            myimg[now_y,now_x,1] = img[img_y,img_x,1]
            myimg[now_y,now_x,2] = img[img_y,img_x,2]
            #增加列数
            img_x += 1
            if img_x >= width:
                img_x = 0
        img_y += 1
        if img_y >= height:
            img_y = 0
        print(round((now_y * 100) / (height * 2)),'%')
    cv2.namedWindow('img1')
    cv2.imshow('img', myimg)
    cv2.waitKey()
    cv2.destroyAllWindows()
            
    
    
# -*- coding: utf-8 -*-
# 随机生成像素
"""
    首先产生空图像矩阵,
    然后确定矩阵的2000个随机位置
    最后将随机位置处的像素值设置为随机数组
"""
import numpy as np
import cv2

if __name__ == '__main__':
    #行数
    sz1 = 200
    #列数
    sz2 = 300
    print('产生的空图像矩阵为(%s,%s)' % (sz1,sz2))
    img = np.zeros((sz1,sz2,3),np.uint8)
    pos1 = np.random.randint(200,size = (5000,1)) #行位置随机数组
    pos2 = np.random.randint(300,size = (5000,1)) #列位置随机数组
    #在随机位置设置像素点值
    for i in range(5000):
        img[pos1[i],pos2[i],[0]] = np.random.randint(0,255)
        img[pos1[i],pos2[i],[1]] = np.random.randint(0,255)
        img[pos1[i],pos2[i],[2]] = np.random.randint(0,255)
    #显示图像
    cv2.imshow('preview...',img)
    #等待按键
    cv2.waitKey()
    #销毁窗口
    cv2.destroyAllWindows()
    
    
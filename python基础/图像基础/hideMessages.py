#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
hideMessages.py

图像隐藏信息的原理:
    首先从源图中提取文字图像信息
    记录这个文字图像信息像素点在图像矩阵的位置
    对载体文件进行预处理,将蓝色像素值全部设为偶数
    最后将记录的文字信息像素点在载体文件对应位置的蓝色像素值设为奇数
图像隐藏信息解密原理:
    提取载体文件中蓝色像素值为奇数的像素点
    
@author: Oscar
"""

import cv2

#含有文字的图像
fnMessageImg = "img/test1.jpg"
#载体文件
fnBaseImg = "img/test2.jpg"
#包含隐藏信息的载体文件
fnSecretImg = "img/secret.jpg"

#注意是(b,g,r),而不是(r,g,b)
redColor=(0,0,255)
if __name__ == "__main__":
    print(u"正在处理中......")
    #图像大小
    messageImg = cv2.imread(fnMessageImg)
    baseImg = cv2.imread(fnBaseImg)
    height = messageImg.shape[0]
    width = messageImg.shape[1]
    
    #加上要隐藏的信息
    cv2.putText(messageImg,"Hello World!",(20,300),cv2.FONT_HERSHEY_PLAIN,2.0,redColor,thickness = 2)
    
    cv2.namedWindow('messageImg')
    cv2.imshow('messageImg',messageImg)
    cv2.namedWindow('baseImg')
    cv2.imshow('baseImg',baseImg)
    
    #处理隐藏信息载体图
    #将所有蓝色值变成偶数
    for j in range(0,height):
        for i in range(0,width):
            if (baseImg[j,i,0] % 2) == 1:
                baseImg[j,i,0] -= 1
        print("changing......",round(50*j / height),"%")
        mirror_w = width /2
    
    #读取源图,将信息写人目标图,将有信息的像素点的蓝色值设为奇数
    for j in range(0,height):
        for i in range(0,width):
            if(messageImg[j,i,0],messageImg[j,i,1],messageImg[j,i,2]) == redColor:
                baseImg[j,i,0] += 1
        print("writing.......",round(50*j / height)+50,"%")
    
    #保存修改后的目标图,并显示
    cv2.namedWindow('secretImg')
    cv2.imshow('secretImg',baseImg)
    cv2.imwrite(fnSecretImg,baseImg)
    cv2.waitKey()
    cv2.destroyAllWindows()
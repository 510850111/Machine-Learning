# -*- coding: utf-8 -*-
"""
图像的日落效果
将蓝色值和绿色值设为原来的70%,红色值不变
"""
import cv2
import numpy as np
fn="img/test1.jpg"

if __name__ == '__main__':
    img = cv2.imread(fn)
    w=img.shape[1]
    h=img.shape[0]    
    ii=0
    #生成日落效果
    #b[:,:] = img[:,:,0]  
    #g[:,:] = img[:,:,1]  
    #r[:,:] = img[:,:,2]  
    for xi in range(0,w):
        for xj in range (0,h):
            img[xj,xi,0]= int(img[xj,xi,0]*0.7)
            img[xj,xi,1]= int(img[xj,xi,1]*0.7)
        if  xi%10==0 :print('.'),          
    cv2.namedWindow('img')     
    cv2.imshow('img', img) 
    cv2.waitKey()
    cv2.destroyAllWindows()

#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
负片效果

@author: Oscar
"""

import cv2
import numpy as np

fn = "img/test1.jpg"
if __name__ == '__main__':
    print('loading %s...' %fn)
    img = cv2.imread(fn)
    height = img.shape[0]
    width = img.shape[1]
    ii = 0
    #生成负片
    #通道分离，顺序BGR不是RGB
    b,g,r = cv2.split(img)
    b = 255 - b
    g = 255 - g
    r = 255 - r
    #直接通过索引改变色彩分量
    img[:,:,0] = b
    img[:,:,1] = g
    img[:,:,2] = r
    #加上水印
    cv2.putText(img,"第一个水印效果",(20,20),cv2.FONT_HERSHEY_PLAIN,2.0,(0,0,0),thickness=2)
    cv2.namedWindow('负片+水印')
    cv2.imshow('负片+水印',img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
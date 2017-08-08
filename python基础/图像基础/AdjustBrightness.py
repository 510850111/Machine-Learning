# -*- coding: utf-8 -*-
"""
Adjust brightness
调整图像亮度
"""

import cv2
fn = 'img/test1.jpg'
if __name__ == '__main__':
    print('loading %s ...' %fn)
    print(u'处理中....')
    status = 'dark'
    if status == 'light':
        value = 1.2
    elif status == 'dark' :
        value = 0.2
    else:
        value = 1
    img = cv2.imread(fn)
    #第二维度长度
    w = img.shape[1]
    #第一维度长度
    h = img.shape[0]
    ii = 0
    #将全部色彩变暗
    for xi in range(0,w):
        for xj in range(0,h):
            #将像素值整体减少,设为原像素的20%
            img[xj,xi,0] = int(img[xj,xi,0] * value)
            img[xj,xi,1] = int(img[xj,xi,1] * value)
            img[xj,xi,2] = int(img[xj,xi,2] * value)
        #显示进度条
        if xi % 10 == 0:
            print('当前状态:',status,'当前进度:' , round(xi * 100 / w) ,'%')
    cv2.namedWindow('img')
    cv2.imshow('img' + status,img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
            
    
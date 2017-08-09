# 机器学习实践指南  
	案例应用解析,第二版,机械工业出版社,ISBN:978-7-111-54021-2 


***
#以下是python图像基础
***
* **平铺图片:**
```python
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
```
-	**运行后如下图:**  <br />
![def](https://github.com/510850111/Machine-Learning/blob/master/python%E5%9F%BA%E7%A1%80/%E5%9B%BE%E5%83%8F%E5%9F%BA%E7%A1%80/saveImg/TileImgpy.png)  

***
* **图片的负片+水印效果:**
```python
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
```
-	**运行后如下图:**  <br />
![def](https://github.com/510850111/Machine-Learning/blob/master/python%E5%9F%BA%E7%A1%80/%E5%9B%BE%E5%83%8F%E5%9F%BA%E7%A1%80/saveImg/negativeImg.png)  


***
* **图像的日落效果:**
```python
# -*- coding: utf-8 -*-
"""
图像的日落效果
将蓝色值和绿色值设为原来的70%,红色值不变
"""
import cv2
import numpy as np #在python3中,xrange被移除,我这里使用的是range,这句话便没有用到
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
```
-	**运行后如下图:**  <br />
![def](https://github.com/510850111/Machine-Learning/blob/master/python%E5%9F%BA%E7%A1%80/%E5%9B%BE%E5%83%8F%E5%9F%BA%E7%A1%80/saveImg/sunset.png)  

***
* **调整图像亮度:**  
```python
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
```
-	**运行后如下图(dark):**  <br />
![def](https://github.com/510850111/Machine-Learning/blob/master/python%E5%9F%BA%E7%A1%80/%E5%9B%BE%E5%83%8F%E5%9F%BA%E7%A1%80/saveImg/AdjustBrightness_dark)  
-	**运行后如下图(light):**  <br />
![def](https://github.com/510850111/Machine-Learning/blob/master/python%E5%9F%BA%E7%A1%80/%E5%9B%BE%E5%83%8F%E5%9F%BA%E7%A1%80/saveImg/AdjustBrightness_light)  

***
* **图像基础,读取图像:**
```python
# -*- coding: utf-8 -*-

import cv2 as cv2
fn = "img/test1.jpg"

if __name__ == '__main__':
    print ('loading %s... ' % fn)
    img = cv2.imread(fn)
    cv2.imshow('preview...',img)
    cv2.waitKey()
    cv2.destroyAllWindows()
```
-	**运行后如下图:**  <br />
![def](https://github.com/510850111/Machine-Learning/blob/master/python%E5%9F%BA%E7%A1%80/%E5%9B%BE%E5%83%8F%E5%9F%BA%E7%A1%80/saveImg/imageBase.png)  


***
* **随机生成像素:**
```python
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
```
-	**运行后如下图:**  <br />
![def](https://github.com/510850111/Machine-Learning/blob/master/python%E5%9F%BA%E7%A1%80/%E5%9B%BE%E5%83%8F%E5%9F%BA%E7%A1%80/saveImg/randomXY.png)  

***
* **正余弦图像的绘制:**   
```python  
#coding:utf-8
"""
Numpy_pylab_matplotlib.py
"""
import numpy as np
import matplotlib.pyplot as plt

#sin函数绘制
x = np.arange(-8,8,0.01)
y = np.sin(x)

plt.plot(x,y)
plt.show()

#余弦函数绘制
y = np.cos(x)
plt.plot(x,y)
plt.show()
```
-	**运行后如下图(sin):**  <br />
![def](https://github.com/510850111/Machine-Learning/blob/master/python%E5%9F%BA%E7%A1%80/%E5%9B%BE%E5%83%8F%E5%9F%BA%E7%A1%80/saveImg/Numpy_pylab_matplotlib_sin.png)  

-	**运行后如下图(cos):**  <br />
![def](https://github.com/510850111/Machine-Learning/blob/master/python%E5%9F%BA%E7%A1%80/%E5%9B%BE%E5%83%8F%E5%9F%BA%E7%A1%80/saveImg/Numpy_pylab_matplotlib_cos.png)

***
* **异常的主动抛出:**
```python
#coding:utf-8
try:
	raise NameError("主动抛出异常:NameError")
except NameError:
	print("异常被抛出!原因是:NameError")
	raise
```
-	**运行后如下图:**  <br />
![def](https://github.com/510850111/Machine-Learning/blob/master/python%E5%9F%BA%E7%A1%80/%E5%9B%BE%E5%83%8F%E5%9F%BA%E7%A1%80/saveImg/tryExceptRaise.png)

***
* **异常的捕获:**
```python
#coding:utf-8
while True:
	try:
		x = int(input("请输入一个数字:"))
		break
	except ValueError:
		print("异常被抛出!")
		break
```  
-	**运行后如下图:**  <br />
![def](https://github.com/510850111/Machine-Learning/blob/master/python%E5%9F%BA%E7%A1%80/%E5%9B%BE%E5%83%8F%E5%9F%BA%E7%A1%80/saveImg/tryExcept.png)

***
* **自定义class的学习:**  
```python
class Complex:
	"""docstring for Complex"""
	r = 0 
	i = 0
	def __init__(self, realPart,imagePart):
		self.r,self.i = realPart,imagePart
x= Complex(3.0,-4.5)
print(x.r,x.i)
```
-	**运行后如下图:**  <br />
![def](https://github.com/510850111/Machine-Learning/blob/master/python%E5%9F%BA%E7%A1%80/%E5%9B%BE%E5%83%8F%E5%9F%BA%E7%A1%80/saveImg/class.png)

***

* **自定义函数的学习:**  
```python
#coding:utf-8
def fib(n):
	"""fibonacci series"""
	a,b = 0,1
	while a < n:
		print(a)
		a,b = b, a+b
fib(2000)
```
- 	**运行后如下图:**  <br />
![def](https://github.com/510850111/Machine-Learning/blob/master/python%E5%9F%BA%E7%A1%80/%E5%9B%BE%E5%83%8F%E5%9F%BA%E7%A1%80/saveImg/def.png)

***


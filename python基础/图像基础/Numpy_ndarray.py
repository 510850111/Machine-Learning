#coding:utf-8
#ndarray数组对象
import numpy as np
#定义一个二维数组,大小为(2,3)
a = np.array([[1.,7.,0.],[-2.,1.,2.]])
"""
	二维数组结构
	1	7 	0
   -2   1 	2
"""
#使用array()创建(2,3)大小的数组变量x
from numpy import *
x = array([[1.,7.,0.],[-2.,1.,2.]])

print "数组的维度数 x.ndim = " , x.ndim

#ndarray.shape 数组的维度数,返回的格式为(n,m),n是行数,m是列数
print "数组的维度数 x.shape = " , x.shape

print "数组元素的总数 x.size = " , x.size

print "元素数组的类型 x.dtype = " , x.dtype

print "数组中每个元素占有字节的大小 x.itemsize = " , x.itemsize

print "数组元素的缓冲区 x.data = " , x.data

#ndarray数组的基本操作:
"""
	首先,创建c(3,5)和d(1,2)两个数组对象.
	a对象使用Numpy的arange函数产生等差序列数组,并reshape函数创建指定形状的新数组
"""
c = arange(15).reshape(3,5)
"""	
	c的数组结构
[	
	[ 0  1  2  3  4]
	[ 5  6  7  8  9]
	[10 11 12 13 14]
]
"""

d = array([6,7,8])
"""
	d的数组结构
	[6 7 8]
"""

print "数组的维度数 c.ndim = " , c.ndim

#ndarray.shape 数组的维度数,返回的格式为(n,m),n是行数,m是列数
print "数组的维度数 c.shape = " , c.shape

print "数组元素的总数 c.size = " , c.size

print "元素数组的类型 c.dtype = " , c.dtype

print "数组中每个元素占有字节的大小 c.itemsize = " , c.itemsize

print "数组元素的缓冲区 c.data = " , c.data

#矩阵的创建
e = matrix('1.0 2.0;3.0 4.0')
"""	e的矩阵
[	
	[ 1.  2.]
 	[ 3.  4.]
]
"""

f = matrix([[1.0,2.0],[3.0,4.0]])
"""	f的矩阵
[
	[ 1.  2.]
	[ 3.  4.]
 ]
"""

print "f的原矩阵:" , f

print "转置 f.T = ",f.T

print "矩阵乘法 f * e = " ,f*e

print "逆矩阵  f.I = " ,f.I

print "解线性方程组 solve(e,f) = " , np.linalg.solve(e,f)


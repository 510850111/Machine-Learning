#coding:utf-8
#ndarray�������
import numpy as np
#����һ����ά����,��СΪ(2,3)
a = np.array([[1.,7.,0.],[-2.,1.,2.]])
"""
	��ά����ṹ
	1	7 	0
   -2   1 	2
"""
#ʹ��array()����(2,3)��С���������x
from numpy import *
x = array([[1.,7.,0.],[-2.,1.,2.]])

print "�����ά���� x.ndim = " , x.ndim

#ndarray.shape �����ά����,���صĸ�ʽΪ(n,m),n������,m������
print "�����ά���� x.shape = " , x.shape

print "����Ԫ�ص����� x.size = " , x.size

print "Ԫ����������� x.dtype = " , x.dtype

print "������ÿ��Ԫ��ռ���ֽڵĴ�С x.itemsize = " , x.itemsize

print "����Ԫ�صĻ����� x.data = " , x.data

#ndarray����Ļ�������:
"""
	����,����c(3,5)��d(1,2)�����������.
	a����ʹ��Numpy��arange���������Ȳ���������,��reshape��������ָ����״��������
"""
c = arange(15).reshape(3,5)
"""	
	c������ṹ
[	
	[ 0  1  2  3  4]
	[ 5  6  7  8  9]
	[10 11 12 13 14]
]
"""

d = array([6,7,8])
"""
	d������ṹ
	[6 7 8]
"""

print "�����ά���� c.ndim = " , c.ndim

#ndarray.shape �����ά����,���صĸ�ʽΪ(n,m),n������,m������
print "�����ά���� c.shape = " , c.shape

print "����Ԫ�ص����� c.size = " , c.size

print "Ԫ����������� c.dtype = " , c.dtype

print "������ÿ��Ԫ��ռ���ֽڵĴ�С c.itemsize = " , c.itemsize

print "����Ԫ�صĻ����� c.data = " , c.data

#����Ĵ���
e = matrix('1.0 2.0;3.0 4.0')
"""	e�ľ���
[	
	[ 1.  2.]
 	[ 3.  4.]
]
"""

f = matrix([[1.0,2.0],[3.0,4.0]])
"""	f�ľ���
[
	[ 1.  2.]
	[ 3.  4.]
 ]
"""

print "f��ԭ����:" , f

print "ת�� f.T = ",f.T

print "����˷� f * e = " ,f*e

print "�����  f.I = " ,f.I

print "�����Է����� solve(e,f) = " , np.linalg.solve(e,f)


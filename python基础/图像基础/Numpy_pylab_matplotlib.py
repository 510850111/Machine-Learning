#coding:utf-8
"""
Numpy_pylab_matplotlib.py
"""
import numpy as np
import matplotlib.pyplot as plt

#sin函数绘制
x = np.arange(0,5,0.1)

y = np.sin(x)
print(type(y))
plt.plot(x,y)
plt.show()

#余弦函数绘制
y = np.cos(x)
plt.plot(x,y)
plt.show()
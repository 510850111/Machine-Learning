#coding:utf-8
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
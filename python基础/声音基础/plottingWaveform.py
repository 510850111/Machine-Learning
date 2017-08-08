#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
绘制波形图

plottingWaveform.py

This is a temporary script file.
"""

import wave
import pylab as pl
import numpy as np
print('working')
#打开wav文档
file = wave.open(r"wav/back.wav","rb")

#读取格式信息
#(nchannels,sampwidth,framerate,nframes,comptype,compname)
params = file.getparams()
nchannels,sampwidth,framerate,nframes = params[:4]
#读取波形数据
str_data = file.readframes(nframes)
file.close()
#将波形数据装换成数组gt
wave_data = np.fromstring(str_data,dtype=np.short)
wave_data.shape = -1,2

wave_data = wave_data.T
time = np.arange(0,nframes) * (1.0 / framerate)
#h绘制波形
"""
subplot(mnp) / (m,n,p)是将多个图画到一个平面上的工具。
其中，m表示是图排成m行，n表示图排成n列，也就是整个figure中有n个图是排成一行的，一共m行，
如果m=2就是表示2行图。p表示图所在的位置，p=1表示从左到右从上到下的第一个位置。
"""
pl.subplot(2,1,1)
pl.plot(time,wave_data[0])
pl.subplot(2,1,2)

pl.plot(time,wave_data[1],c="g")
pl.xlabel("time (seconds)")
pl.show()
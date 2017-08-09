#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
放大音量
LouderVolume.py.
为包证声音质量,需要对音量调节范围,设置上限和下限(以原声音为基准,计算上限和下限),
为此编写waveChange(x,dwmax,dwmin)函数,计算调整后的数据,x为每次采样的波形数据,
dwmax为上限,dwmin为下限,该函数仅仅会将上限和下限之间的区域内的数据放大为原来的1.5倍,
在此区域外的数据设置为上限和下限
@author: Oscar
"""
import wave
import pylab as pl
import numpy as np
def waveChange(x,dwmax,dwmin):
    """
        x -- 每次采样的波形数据
        dwmax -- 上限
        dwmin -- 下限
    """
    if x != 0:
        if abs(x) > dwmax:
            x = x / abs(x) * dwmax
        elif abs(x) < dwmin:
            x = x / abs(x) * dwmin
        else:
            x = x * 1.5
    return x
#打开wav文档
file = wave.open(r"wav/speak.wav","rb")
fileOUT = wave.open(r"wav/OUT.wav","wb")
#(nchannels,sampwidth,framerate,nframes,comptype,compname)
params = file.getparams()
nchannels,sampwidth,framerate,nframes = params[:4]
print("reading wav file......")
str_data = file.readframes(nframes)
#将波形数据转换为数组,并更改
print("changing wav file......")
wave_data = np.fromstring(str_data,dtype=np.short)
#---start---
#我不知道为什么要重复这几句话,但是是书上的例子,我还是写下来了
params = file.getparams()
nchannels,sampwidth,framerate,nframes = params[:4]
str_data = file.readframes(nframes)
#---end---

#放大音量
"""
为保证放大后不失真,可采用以原声音为基准的放大策略,声音波形图像内室正弦函数图像,
再以时间轴为X轴,采样数据为Y轴的坐标系中,波形数据可正可负,上下波动
因此,以原声音数据的最大值为依据计算上下限,上限为原声音数据最大值的88%,下限为原声音数据最大值的14%
"""
change_dwmax = wave_data.max() / 100 * 88
change_dmin = wave_data.max() / 100 * 14
"""
frompyfunc，把Python里的函数（可以是自写的）转化成ufunc，
用法是frompyfunc(func, nin, nout)，其中func是需要转换的函数，nin是函数的输入参数的个数，nout是此函数的返回值的个数。
注意frompyfunc函数无法保证返回的数据类型都完全一致,
因此返回一个中间类型object，需要再次obj.astype(np.float64)之类将其元素类型强制调齐。
"""
wave_change = np.frompyfunc(waveChange,3,1)
new_wave_data = wave_change(wave_data,change_dwmax,change_dmin)
new_wave_data = new_wave_data.astype(wave_data.dtype)
new_str_data  = new_wave_data.tostring()

#写波形数据参数,配置声道数、量化位数和取样频率
print("saving new wav file ...")
fileOUT.setnchannels(nchannels)
fileOUT.setframerate(framerate)
fileOUT.setsampwidth(sampwidth)

#将new_str_data转换为二进制数据写入文件
fileOUT.writeframes(new_str_data)

#绘制原声音声音波形
wave_data.shape = -1,2
wave_data = wave_data.T
time = np.arange(0,nframes) * (1.0 / framerate)
pl.subplot(2,2,1)
pl.plot(time,wave_data[0])
pl.subplot(2,2,2)
pl.plot(time,wave_data[1],c="g")
pl.xlabel("time (seconds)")

#绘制放大声音声音波形
new_wave_data.shape = -1,2
new_wave_data = new_wave_data.T
new_time = np.arange(0,nframes) * (1.0 / framerate)
pl.subplot(2,2,3)
pl.plot(new_time,new_wave_data[0])
pl.subplot(2,2,4)
pl.plot(new_time,new_wave_data[1],c="g")
pl.xlabel("time (seconds)")

file.close()
fileOUT.close()

pl.show()












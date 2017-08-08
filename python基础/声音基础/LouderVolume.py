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
file1 = wave.open(r"wav/jg.wav","wb")
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
change_dmin = wave_data.min() / 100 * 14

















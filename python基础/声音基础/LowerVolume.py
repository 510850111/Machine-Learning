#1/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 08:55:09 2017

LowerVolume.py

减低音量的算法
音量降低可通过将采样波形变小来实现,具体来说,就是把每个采样数据按一定比例缩小
同时将缩小的幅度控制在合理的范围内,保证音量降低后声音仍然清晰
@author: Oscar
"""

import wave 
import numpy as np
import pylab as pl

print("working.....")
def waveChange(x,dwmax,dwmin):
    if x != 0:
        if abs(x) < dwmax and abs(x) > dwmin:
            x *= 0.5
        else:
            x *= 0.2
    return x

#打开wav文件
file = wave.open(r"wav/speak.wav","rb")
fileOUT = wave.open(r"wav/lowerVolumeSpeak.wav","wb")

#读取波形数据
"""
笔记:
    getparams：一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：
    声道数,      量化位数（byte单位）, 采样频率,  采样点数,  压缩类型,  压缩类型的描述。
    nchannels   sampwidth            framerate  nframes  comptype   compname
    wave模块只支持非压缩的数据，因此可以忽略最后两个信息：
"""
#(nchannels,sampwidth,framerate,nframes,comptype,compname)
params = file.getparams()
nchannels,sampwidth,framerate,nframes = params[:4]
str_data = file.readframes(nframes)

#将波形数据转换为数组,并更改:
print("changing wav data......")
wave_data = np.fromstring(str_data,dtype=np.short)
#------start----
#我不知道为什么要重复下面这几句话,但是是书上的例子,我还是写下来了
params = file.getparams()
nchannels,sampwidth,framerate,nframes = params[:4]
str_data = file.readframes(nframes)
#------end------

#降低音量
"""
与放大音量相似,以原声音波形的最大值为基准,计算上限和下限,以waveChange为回调函数,降低音量
"""
change_dwmax = wave_data.max() / 100 * 1
change_dwmin = wave_data.max() / 100 * 0.5
"""
frompyfunc，把Python里的函数（可以是自写的）转化成ufunc，
用法是frompyfunc(func, nin, nout)，其中func是需要转换的函数，nin是函数的输入参数的个数，nout是此函数的返回值的个数。
注意frompyfunc函数无法保证返回的数据类型都完全一致,
因此返回一个中间类型object，需要再次obj.astype(np.float64)之类将其元素类型强制调齐。
"""
wave_change = np.frompyfunc(waveChange,3,1)
out_wave_data = wave_change(wave_data,change_dwmax,change_dwmin)
out_wave_data = out_wave_data.astype(wave_data.dtype)
out_str_data = out_wave_data.tostring()

#把波形参数写入磁盘
print("saving new wav file......")
fileOUT.setnchannels(nchannels)
fileOUT.setframerate(framerate)
fileOUT.setsampwidth(sampwidth)
fileOUT.writeframes(out_str_data)
print("new wav file saved!")

#绘制原声音波形图
wave_data.shape = -1,2
wave_data = wave_data.T
time = np.arange(0,nframes) * (1.0 / framerate)

pl.subplot(2,2,1)#亦可写作pl.subplot(221)
pl.plot(time,wave_data[0],c="b")
pl.xlabel("time (seconds)")
pl.ylabel("Original volume")
pl.subplot(222)#亦可写作pl.subplot(2,2,2)
pl.plot(time,wave_data[1],c="b")
pl.xlabel("time (seconds)")

#绘制降低后音量的波形图
out_wave_data.shape = -1,2
out_wave_data = out_wave_data.T
time = np.arange(0,nframes) * (1.0 / framerate)

pl.subplot(2,2,3)#亦可写作pl.subplot(223)
pl.plot(time,out_wave_data[0],c="r")
pl.xlabel("time (seconds)")
pl.ylabel("Lower volume")
pl.subplot(224)#亦可写作pl.subplot(2,2,4)
pl.plot(time,out_wave_data[1],c="r")
pl.xlabel("time (seconds)")

#关闭打开的文件
file.close()
fileOUT.close()
#显示图形
pl.show()

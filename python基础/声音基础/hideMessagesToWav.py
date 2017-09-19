#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
hideMessagesToWav.py

这里的隐藏策略是:
    首先产生一段正弦波的噪声,
    然后在这一段噪声中隐藏一段文本文件的内容.
    这里使用简单的加密算法:
        字符的ASCII码乘以自动的整数后,
        减去64与该整数的乘积
        信息隐藏格式:
            ----------------------------------------------------------------------------
            |  区域  |  随机噪声区  |  加密字符区  | 随机噪声区  | 加密字符区  |  ......  |
            ----------------------------------------------------------------------------
            |  长度  |   interval   |     1       |  interval  |    1       |          |
            ----------------------------------------------------------------------------
@author: Oscar
"""
import wave
import pylab as pl
import numpy as np

print(u"正在将文件编码到声音.....")
print(u"正在打开文件.....")
fileOpen = wave.open(r"wav/pltest.wav","wb")
messageFile  = open("messages.txt")
try:
    #读取文件内容
    text = messageFile.read()
finally:
    #读取完毕关闭文件
    messageFile.close()
# map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
# ord()函数主要用来返回对应字符的ascii码
# map(func,*iterables)
wordDataAsAscii = list(map(ord,text))#这里我发现直接使用map是有问题的,所以使用list进行转换
# 这里是以list类型的变量为参数产生数组,这里wordDataAsASCII成为了一维数组
wordDataAsAscii = np.array(wordDataAsAscii)
wordDataAsAsciiLength = len(wordDataAsAscii.tolist())
#设置波形参数
#采样率
framerate = 44100
#声道数
nchannels = 2
#每位宽度
sampwidth = 2
#长度
nframes = framerate *4
#振幅
base_amplitude = 200;
max_amplitude = base_amplitude * 128
#每个字符的间隔
interval = (nframes -10 ) / wordDataAsAsciiLength;
#每周期样本数
wave_data = np.zeros((nframes),dtype=np.short)

count = 0

#写噪声数据和隐藏文字的字符
randomNum = np.random.rand(nframes)#rand(d0, d1, ..., dn)	Random values in a given shape.
for currentPos in range(0,nframes):
    if currentPos % interval ==0 and count < wordDataAsAsciiLength:
        #将隐藏文字的字符通过一定的变化写入噪声数据
        posSamp = (wordDataAsAscii[count] * base_amplitude) - (64*base_amplitude)
        count += 1
    elif currentPos % 60 == 0:
        #生成随机噪声数据
        posSamp = int((randomNum[currentPos] * max_amplitude) - (max_amplitude / 2))
    else:
        posSamp = 0
    wave_data[currentPos] = posSamp

#写波形数据参数
print("wiriting wav file......")
str_data = wave_data.tostring()
fileOpen.setnchannels(nchannels)
fileOpen.setframerate(framerate)
fileOpen.setsampwidth(sampwidth)
fileOpen.setnframes(nframes)
fileOpen.writeframes(str_data)
print("file has been saved!")

#绘制图形
wave_data.shape = -1,2
wave_data = wave_data.T
time = np.arange(0,nframes / 2)
pl.subplot(211)
pl.plot(time,wave_data[0],c="r")
pl.xlabel("time (seconds) L")
pl.subplot(212)
pl.plot(time,wave_data[0],c="g")
pl.xlabel("time (seconds) R")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
showMessagesFromWav.py
Created on Tue Sep 19 14:10:24 2017

信息的解码
先读取噪声载体文件以及相关格式信息
找到字符区,将其中的字符解密并还原成字符串
整理字符串,将它们写入文件

@author: Oscar
"""
import wave
import pylab as pl
import numpy as np
wordData = []
print(u"正在打开声音文件......")
file = wave.open(r"wav/pltest.wav","rb")
"""
笔记:
    getparams：一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：
    声道数,      量化位数（byte单位）, 采样频率,  采样点数,  压缩类型,  压缩类型的描述。
    nchannels   sampwidth            framerate  nframes  comptype   compname
    wave模块只支持非压缩的数据，因此可以忽略最后两个信息：
"""
params = file.getparams()
nframes = params[3]
str_data = file.readframes(nframes)
#将波形数据转换为数组
wave_data  = np.fromstring(str_data,dtype=np.short)
base_amplitude = 200

count = 0
interval= 6299.642857142857#从加密中得到的数据
wordDataAsAsciiLength= 28#从加密中得到的数据

for currentPos in range(0,nframes):
    if currentPos % interval ==0 and count < wordDataAsAsciiLength:
        #将隐藏文字的字符通过一定的变化写入噪声数据
        posSamp = (wave_data[currentPos] + 64*base_amplitude) // base_amplitude
        print(posSamp)
        wordData.append(posSamp)
        count += 1
print(wordData)
text = "".join(map(chr,wordData))
print(text)
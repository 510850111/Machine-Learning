#coding:utf-8
try:
	raise NameError("主动抛出异常:NameError")
except NameError:
	print("异常被抛出!原因是:NameError")
	raise
 #coding:utf-8
while True:
	try:
		x = int(input("请输入一个数字:"))
		break
	except ValueError:
		print("异常被抛出!")
		break

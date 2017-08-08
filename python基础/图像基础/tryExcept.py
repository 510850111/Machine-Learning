 #coding:utf-8
while True:
	try:
		x = int(raw_input("请输入数字:"))
		break
	except ValueError:
		print "哎呀,你输入的不是字符呢!"
		break

 #coding:utf-8
while True:
	try:
		x = int(raw_input("����������:"))
		break
	except ValueError:
		print "��ѽ,������Ĳ����ַ���!"
		break

 #coding:utf-8
def fib(n):
	"""fibonacci series"""
	a,b = 0,1
	while a < n:
		print a 
		a,b = b, a+b
fib(2000)
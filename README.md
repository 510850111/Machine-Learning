# 机器学习实践指南  
	案例应用解析,第二版,机械工业出版社,ISBN:978-7-111-54021-2  

***
* **自定义函数的学习:**  
```python
#coding:utf-8
def fib(n):
	"""fibonacci series"""
	a,b = 0,1
	while a < n:
		print(a)
		a,b = b, a+b
fib(2000)
```
- 	**运行后如下图:**  <br />
![def](https://github.com/510850111/Machine-Learning/blob/master/python%E5%9F%BA%E7%A1%80/%E5%9B%BE%E5%83%8F%E5%9F%BA%E7%A1%80/saveImg/def.png)

***

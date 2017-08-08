class Complex:
	"""docstring for Complex"""
	r = 0 
	i = 0
	def __init__(self, realPart,imagePart):
		self.r,self.i = realPart,imagePart
x= Complex(3.0,-4.5)
print(x.r,x.i)
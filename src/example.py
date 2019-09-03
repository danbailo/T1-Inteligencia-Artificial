theta = 2
m = 3

	'def h(x):
		return theta*x

	def J(x,y):
		J=0
		divisor = 2*m
		for i in range(m):
			J += ((h(x[i])-y[i])**2)/divisor
		return J	'	

print(J([1,2,3],[1,2,3]))
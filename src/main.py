import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_input(file_name):
	with open('../inputs/'+file_name) as file:
		return np.array(file.read().split(), dtype=np.float32)	

def h(x, theta):
	return theta*x

def J(x, y, m, theta):
	J=0
	divisor = 2*m
	for i in range(m):
		J += ((h(x[i], theta)-y[i])**2)/divisor
	return J	

if __name__ == "__main__":
	x = get_input('entradas_x.txt')
	y = get_input('saidas_y.txt')


	print(x)
	print(y)

	theta=0
	print(J(x,y,len(x),theta))
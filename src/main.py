import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_input(file_name):
	with open('../inputs/'+file_name) as file:
		return np.array(file.read().split(), dtype=np.float32)	

def e(H_theta, y):
	return H_theta - y

def J(m,e):
	return (np.transpose(e)*e)/2*m


if __name__ == "__main__":
	x = get_input('entradas_x.txt')
	y = get_input('saidas_y.txt')

	m = len(x)

	x.re

	print(x.shape)

	print(np.ones(m))
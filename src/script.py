import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['figure.figsize'] = (10, 7) #(width,height)
plt.rcParams['axes.grid'] = True
# plt.rcParams['text.usetex'] = True

def linear_regression(num_it, alpha, theta):
    J = np.zeros(num_it)
    for i in range(num_it):
        H_theta = np.dot(X,theta)
        E = H_theta-y
        J[i] = (np.dot(E.T,E)/(2*m))
        theta = theta - ((alpha/m)*np.dot(X.T,E))
    return J, H_theta


if not os.path.exists(os.path.join('..','imgs')):
    os.makedirs(os.path.join('..','imgs'))
x = np.loadtxt('../inputs/entradas_x.txt')
y = np.loadtxt('../inputs/saidas_y.txt')
m = len(x)
x = x.reshape(m,1)
y = y.reshape(m,1)

X = np.ones((len(x),2))
X[:,-1:] = x
theta = np.array([0,0]).reshape(2,1)

NUM_IT = 1000

J, H_theta = linear_regression(NUM_IT,  0.07, theta)

plt.figure()
plt.plot(J)
plt.show()

plt.figure()
plt.scatter(x,y, c='red', marker='x')
plt.plot(x,H_theta)
plt.show()

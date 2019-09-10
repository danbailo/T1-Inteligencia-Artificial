#!/usr/bin/env python
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['figure.figsize'] = (10, 7) #(width,height)
plt.rcParams['axes.grid'] = True
plt.rcParams['text.usetex'] = True

def linear_regression(num_it, alpha, theta):
    err = np.zeros(num_it)
    for i in range(num_it):
        h = np.dot(X,theta)
        e = h-y
        J = (np.dot(e.T,e)/(2*m))
        err[i] = J
        theta = theta - ((alpha/m)*np.dot(X.T,e))
    return err, theta

if not os.path.exists(os.path.join('..','imgs')):
    os.makedirs(os.path.join('..','imgs'))
x = np.loadtxt('../inputs/entradas_x.txt')
y = np.loadtxt('../inputs/saidas_y.txt')
m = len(x)
x = x.reshape(m,1)
y = y.reshape(m,1)

X = np.ones((len(x),2))
X[:,-1:] = x
initial_theta = np.array([0,0]).reshape(2,1)

NUM_IT = 100

err, theta = linear_regression(num_it=NUM_IT, alpha=0.1, theta=initial_theta)
plt.plot(range(NUM_IT),err, label=r'$\alpha$ = 0.1')
plt.xlabel('Iterações')
plt.ylabel(r'J($\theta$)')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.savefig(os.path.join('..','imgs/')+'first_insight.pdf', bbox_inches='tight')

plt.scatter(x,y, label= 'Data', s=30, marker='x', c='r')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.savefig(os.path.join('..','imgs/')+'data.pdf', bbox_inches='tight')

plt.scatter(x,y, label= 'Data', s=30, marker='x', c='r')
plt.plot(x, [theta[0]+(theta[1]*i) for i in x], label= 'Predicted', c='orange')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.savefig(os.path.join('..','imgs/')+'first_predicted.pdf', bbox_inches='tight')

plt.yscale('log')
alpha_values = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07,0.08,0.09,0.1]
theta_values = {}
err_values = {}

for alpha in alpha_values:
    err, theta = linear_regression(num_it=NUM_IT, alpha=alpha, theta=initial_theta)
    theta_values[alpha] = theta
    err_values[alpha] = err
    plt.plot(range(NUM_IT), err, label=fr'$\alpha$ = {alpha}')
plt.xlabel('Iterações')
plt.ylabel(r'J($\theta$)')    
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.axis(ymax=10e2,ymin=8e-4)
plt.savefig(os.path.join('..','imgs/')+'overflow_insights.pdf', bbox_inches='tight')

plt.yscale('log')
alpha_values = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
theta_values = {}
err_values = {}

for alpha in alpha_values:
    err, theta = linear_regression(num_it=NUM_IT, alpha=alpha, theta=initial_theta)
    theta_values[alpha] = theta
    err_values[alpha] = err
    plt.plot(range(NUM_IT), err, label=fr'$\alpha$ = {alpha}')
plt.xlabel('Iterações')
plt.ylabel(r'J($\theta$)')    
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.savefig(os.path.join('..','imgs/')+'lr_100it.pdf', bbox_inches='tight')

plt.yscale('log')
for alpha,err in err_values.items():
    plt.plot(range(NUM_IT),err, label=fr'$\alpha$ = {alpha}')
plt.axis(xmin=-0.5,xmax=8,ymin=20e-3)
plt.xlabel('Iterações')
plt.ylabel(r'J($\theta$)')    
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.savefig(os.path.join('..','imgs/')+'lower_interval.pdf', bbox_inches='tight')


plt.yscale('log')
for alpha,err in err_values.items():
    plt.plot(range(NUM_IT),err, label=fr'$\alpha$ = {alpha}')
plt.axis(xmin=90,xmax=100)
plt.xlabel('Iterações')
plt.ylabel(r'J($\theta$)')    
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.savefig(os.path.join('..','imgs/')+'higher_interval_100it.pdf', bbox_inches='tight')

plt.yscale('log')
NUM_IT = 1000

for alpha in alpha_values:
    err, theta = linear_regression(num_it=NUM_IT, alpha=alpha, theta=initial_theta)
    theta_values[alpha] = theta
    err_values[alpha] = err
    plt.plot(range(NUM_IT), err, label=fr'$\alpha$ = {alpha}')
plt.xlabel('Iterações')
plt.ylabel(r'J($\theta$)')    
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.savefig(os.path.join('..','imgs/')+'lr_1000it.pdf', bbox_inches='tight')

plt.yscale('log')
for alpha,err in err_values.items():
    plt.plot(range(NUM_IT),err, label=fr'$\alpha$ = {alpha}')
plt.axis(xmin=990,xmax=1000)
plt.xlabel('Iterações')
plt.ylabel(r'J($\theta$)')    
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.savefig(os.path.join('..','imgs/')+'higher_interval_1000it.pdf', bbox_inches='tight')

plt.yscale('log')
for alpha,err in err_values.items():
    plt.plot(range(NUM_IT),err, label=fr'$\alpha$ = {alpha}')
plt.axis(xmin=990,xmax=1000, ymax=10.6e-4, ymin=9.8e-4)
plt.xlabel('Iterações')
plt.ylabel(r'J($\theta$)')    
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.savefig(os.path.join('..','imgs/')+'max_zoom.pdf', bbox_inches='tight')

plt.scatter(x,y, label= 'Data', s=30, marker='x', c='r')
for k,v in theta_values.items():
    plt.plot(x, [v[0]+(v[1]*i) for i in x], label= r'Predicted; $\alpha$ = '+str(k))
plt.xlabel('X')
plt.ylabel('y')    
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.savefig(os.path.join('..','imgs/')+'all_predictions.pdf', bbox_inches='tight')

alpha = 0.07
_, new_theta = linear_regression(num_it=NUM_IT, alpha=alpha, theta=initial_theta)

plt.scatter(x,y, label= 'Data', s=30, marker='x', c='r')
plt.plot(x, [new_theta[0]+(new_theta[1]*i) for i in x], label= r'Predicted; $\alpha$ = '+str(k), c='orange')
plt.xlabel('X')
plt.ylabel('y')    
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.savefig(os.path.join('..','imgs/')+'FINAL_predicted.pdf', bbox_inches='tight')
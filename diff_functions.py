"""
File: diff_functions.py
Copyright (c) 2016 Andrew Malfavon
License: MIT
Exercise B.8
Description: Plot functions and their derivatives.
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.log(x + (1 / float(100)))

def g(x):
    return np.cos(np.exp(10 * x))

def h(x):
    return x**x

def f_prime(x):
    return 1 / (x + (1 / float(100)))

def g_prime(x):
    return -10 * np.exp(10 * x) * np.sin(np.exp(10 * x))

def h_prime(x):
    return (np.log(x)) * x**x + x * x**(x - 1)

#computes the discrete derivative
def diff(func, a, b, n):
    x = np.linspace(a, b, n+1)
    y = np.zeros(len(x))
    z = np.zeros(len(x))
    h = (b-a)/float(n)
    for i in xrange(len(x)):
        y[i] = func(x[i])
    for i in xrange(len(x)-1):
        z[i] = (y[i+1] - y[i])/h
    z[n] = (y[n] - y[n-1])/h
    return y, z

#plots the approximated derivative
def plot(func, a, b, n):
    x = np.linspace(a, b, n + 1)
    y_approx = diff(func, a, b, n)[1]
    plt.plot(x,y_approx)
    plt.title('Approximation of the derivative')
    plt.xlabel('x')
    plt.ylabel('y')

#plots the approximations and the analytical derivatives
def modified_plot(func, func_prime, a, b, n):
    x = np.linspace(a, b, n + 1)
    y_approx = diff(func, a, b, n)[1]
    y_exact = func_prime(x)
    plt.plot(x, y_approx)
    plt.plot(x, y_exact)
    plt.title('Approximation and exact derivative')
    plt.xlabel('x')
    plt.ylabel('y')
"""
File: interpolate_exp_cos.py
Copyright (c) 2016 Andrew Malfavon
License: MIT
Exercise B.2
Description: Interpolate a discrete function.
"""

import numpy as np
import matplotlib.pyplot as plt

#plots the given function for eps>0 and n nodes.
def plot(eps, n):
    x = np.linspace(0, 1, n + 1)
    y = np.sin(1 / (x + (eps)))
    plt.plot(x, y)
    plt.axis([-0.2, 1.1, -1.1, 1.1])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('f(x)')

#plots for n and n+10
def plot_refined(eps, n1):
    n2 = n1 + 10
    x1 = np.linspace(0, 1, n1 + 1)
    y1 = np.sin(1 / (x1 + (eps)))
    x2 = np.linspace(0, 1, n2 + 1)
    y2 = np.sin(1 / (x2 + (eps)))
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.axis([-0.2, 1.1, -1.1, 1.1])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('f(x)')

#Find how large n should be for the difference between the two functions to be less than 0.1
def find_large_n(eps):
    n1 = 1
    n2 = n1 + 10
    x1 = np.linspace(0, 1, n1 +1)
    x2 = np.linspace(0, 1, n2 + 1)
    f1 = np.sin(1 / (x1 + (eps)))
    f2 = np.sin(1 / (x2 + (eps)))
    while (abs(max(f2) - max(f1)) >= 0.1):
        n1 += 1
        n2 += 1
        x1 = np.linspace(0, 1, n1 +1)
        x2 = np.linspace(0, 1, n2 + 1)
        f1 = np.sin(1 / (x1 + (eps)))
        f2 = np.sin(1 / (x2 + (eps)))
    return n1

#test that for each eps the difference of the max values of the functions is less than 0.1
def test():
    eps_array = [0.1, 0.2, 0.05]#each eps value to be tested
    difference_array = []
    for elem in eps_array:#use the n1 calculated in find_large_n
        n1 = find_large_n(elem)
        n2 = n1 + 10
        x1 = np.linspace(0, 1, n1 +1)
        x2 = np.linspace(0, 1, n2 + 1)
        f1 = np.sin(1 / (x1 + (elem)))
        f2 = np.sin(1 / (x2 + (elem)))
        difference_array.append(abs(max(f1) - max(f2)))#make an array of each difference
    for i in range(len(difference_array)):
        assert difference_array[i] < 0.1#check the resulting difference is less than 0.1
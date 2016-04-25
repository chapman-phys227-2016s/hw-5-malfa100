"""
File: integrate_exp.py
Copyright (c) 2016 Andrew Malfavon
License: MIT
Exercise B.6
Description: approximate an integral with the Trapezoidal method.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#graphs the function to visually see the symmetry
def plot(n):
    x = np.linspace(-10, 10, n)
    y = np.exp(-x**2)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('$e^{-x^2}$')

#trapezoidal method to approximate the integral
def T(n, L):
    x = np.linspace(0, L, n)#takes just the positive x-values
    y = np.exp(-x**2)
    h = L / float(2*n)
    endpoints = y[0] + y[n - 1]
    f = 0
    for i in range(1, n - 1):
        f +=  2 * y[i]
    approx = h * (endpoints + f)
    return 2 * approx#multiplies by two to account for the negative x-values

def table():
    L_array = np.array(['L = 2', 'L = 4', 'L = 6', 'L = 8', 'L = 10'])#used to label the table
    n_array = np.array(['n = 100', 'n = 200', 'n = 300', 'n = 400', 'n = 500'])#used to label the table
    n = [100, 200, 300, 400, 500]
    L = [2, 4, 6, 8, 10]
    T_matrix = np.zeros([5, 5])#a five-by-five matrix with all zeros
    array = []
    counter = 0
    for elem_n in n:
        for elem_L in L:
            array.append(T(elem_n, elem_L))#plugs in each value of n and L and puts them in an array
    for i in range(5):
        for j in range(5):
            T_matrix[i, j] = array[counter]#arranges the array into a five-by-five matrix
            counter += 1
    table = pd.DataFrame(T_matrix, index = n_array, columns = L_array)#puts the matrix into a table and lables the axes
    return table

#same thing as before except it displays the error
def error_table():
    L_array = np.array(['L = 2', 'L = 4', 'L = 6', 'L = 8', 'L = 10'])
    n_array = np.array(['n = 100', 'n = 200', 'n = 300', 'n = 400', 'n = 500'])
    n = [100, 200, 300, 400, 500]
    L = [2, 4, 6, 8, 10]
    T_error_matrix = np.zeros([5, 5])
    array = []
    counter = 0
    for elem_n in n:
        for elem_L in L:
            array.append(np.sqrt(np.pi) - T(elem_n, elem_L))#error from the known analytic solution
    for i in range(5):
        for j in range(5):
            T_error_matrix[i, j] = array[counter]
            counter += 1
    error_table = pd.DataFrame(T_error_matrix, index = n_array, columns = L_array)
    return error_table

#Test for each value of n and L the error between the known solution and the approximation is less than 0.1
def test():
    n = [100, 200, 300, 400, 500]
    L = [2, 4, 6, 8, 10]
    test_array = []
    for elem_n in n:#creates an array with the error for each combination of n and L
        for elem_L in L:
            test_array.append(abs(np.sqrt(np.pi)- T(elem_n, elem_L)))
    for i in range(len(test_array)):#tests each spot in the array
        assert test_array[i] < 0.1
"""
File: interpolate_exp_cos.py
Copyright (c) 2016 Andrew Malfavon
License: MIT
Exercise B.1
Description: Interpolates a discrete function
"""

import numpy as np

#calculates the interpolated function value at x
def interpolate_exp_cos(q, x):
    mesh = np.linspace(-1, 1, q + 1)
    f = np.exp(-mesh**2) * np.cos(2 * np.pi * mesh)
    exact = np.exp(-x**2) * np.cos(2 * np.pi * x)
    mesh2 = [i for i in mesh if i <= x]#deletes the values in the mesh greater than x
    x1 = mesh[len(mesh2) - 1]#the value in the mesh right before x
    y1 = f[len(mesh2) - 1]
    x2 = x1 + 1#value in mesh right after x
    y2 = f[len(mesh2)]
    m = (y2 - y1) / (x2 - x1)#slope formula
    b = y2 - (m * x2)
    interp = (m * x) + b
    error = exact - interp
    return interp, error

def test():
    assert interpolate_exp_cos(8, -0.45)[1] < 0.1#tests if error is low
    assert interpolate_exp_cos(2, 0)[0] == 1.0#value at x=0 is 1. approximation is accurate for small q
    assert interpolate_exp_cos(16, 0)[0] == 1.0#approximation is also accurate for larger q
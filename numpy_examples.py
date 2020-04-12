"""
simple NumPy Examples

"""

import numpy as np

def f(x):
    return x**2


def integrate(f, a, b, N):
    dx = (b-a)/N
    x = np.linspace(a+dx/2, b-dx/2, N)
    fx = f(x)
    area = np.sum(fx)*dx
    return area

print(integrate(np.sin, 0, np.pi/2, 100))
print(integrate(np.sin, 0, np.pi*2, 100))

print(integrate(f, 0, 3, 100))

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(f(a))



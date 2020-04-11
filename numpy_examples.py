"""
simple NumPy Examples

"""

import numpy as np


# a = np.array([[1, 2],
#               [5, 6]])
#
# b = np.array([[3, 7],
#               [4, 8]])
#
# print(a*2)
# print(b+5)
# print(a+b)
# print(a*b)
# print(a>b)


c = np.array([[1, 2, 5, 7],
              [8, 3, 6, 2],
              [9, 8, 4, 8]])


print(c.sum())
print(c.sum(axis=0))
print(c.sum(axis=1))

print(c.max())
print(c.max(axis=0))
print(c.max(axis=1))

d = np.unique(c)
print(d)
d, e = np.unique(c, return_counts=True)
print(d)
print(e)

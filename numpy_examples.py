"""
simple NumPy Examples

"""

import numpy as np


a1 = np.array([[1, 1, 1],
               [2, 2, 2],
               [3, 3, 3]])

b1 = np.array([[2, 2, 2],
               [2, 2, 2],
               [2, 2, 2]])
#
# c1 = a1*b1
# print(c1)
# print(c1.shape)
#
# c1 = np.dot(a1, b1)
# print(c1)
# print(c1.shape)

ma1 = np.mat(a1)
mb1 = np.mat(b1)

c1 = ma1 * mb1
print(c1)
print(c1.shape)



a2 = np.array([[3, 2, 1, 5],
               [9, 1, 3, 0]])

b2 = np.array([[2, 9, 0],
               [1, 3, 5],
               [2, 4, 7],
               [8, 1, 5]])

ma2 = np.mat(a2)
mb2 = np.mat(b2)

c2 = ma2 * mb2
print(c2)
print(c2.shape)

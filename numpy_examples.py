"""
simple NumPy Examples

"""

import numpy as np


# a = np.array([[1, 2],
#               [3, 4]])
#
# b = np.array([[10, 20],
#               [30, 40]])
#
# c = np.hstack((a, b))
# print(c)
#
# d = np.vstack((a, b))
# print(d)
#
# a1 = np.array([1, 2, 3, 4])
# a2 = np.array([11, 22, 33, 44])
# a3 = np.array([111, 222, 333, 444])
#
# e = np.column_stack((a1, a2, a3))
# print(e)

a = np.array([[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]])

b, c, d = np.hsplit(a, 3)
print(b)
print(c)
print(d)
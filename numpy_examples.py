"""
simple NumPy Examples

"""

import numpy as np


# a = np.array([[ 0,  0,  0],
#               [10, 10, 10],
#               [20, 20, 20],
#               [30, 30, 30]])
#
# b = np.array([ 1, 2, 3])
#
# c = a + b
# print(c)


# a = np.array([ 0,  10,  20, 30])
# a = a[:, np.newaxis]
# print(a)
#
# b = np.array([[ 1, 2, 3],
#               [ 1, 2, 3],
#               [ 1, 2, 3],
#               [ 1, 2, 3]])
#
# c = a + b
# print(c)

a = np.array([ 0,  10,  20, 30])
a = a[:, np.newaxis]
print(a)

b = np.array([ 1, 2, 3])

c = a + b
print(c)
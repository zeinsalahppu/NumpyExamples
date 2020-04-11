"""
simple NumPy Examples

"""

import numpy as np


# a_np = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(a_np)
#
# lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a_np = np.array(lst)
# print(a_np)
#
# lst = [i for i in range(10)]
# a_np = np.array(lst)
# print(a_np)

# lst_2d = [[0, 1, 2, 3],
#          [4, 5, 6, 7],
#          [8, 9, 10, 11]]
# a_2d = np.array(lst_2d)
#
# print(a_2d)
# print(a_2d.shape)
# print(a_2d.ndim)
# print(a_2d.dtype)
# print(a_2d.itemsize)
# print(a_2d.size)
# print(type(a_2d))
#
#
# lst_3d = [[[0,  1], [2,  3]],
#           [[4,  5], [6,  7]],
#           [[8,  9], [10,11]] ]
# a_3d = np.array(lst_3d)
# print(a_3d)
# print(a_3d.shape)

a1 = np.zeros(4)
print(a1)
a2 = np.ones((2, 3))
print(a2)
a3 = np.empty(5)
print(a3)
a4 = np.arange(2, 5, 0.5)
print(a4)
a5 = np.linspace(0, 10, 5)
print(a5)
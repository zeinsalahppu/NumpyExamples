"""
simple NumPy Examples

"""

import numpy as np


# a = np.arange(24)
# print(a)
# print(a.shape)
#
# b = a.reshape((4, 6))
# print(b)
# print(b.shape)
#
# c = a.reshape((3, 2, 4))
# print(c)
# print(c.shape)
# print(c[2, 0, 3])


a = np.arange(5)
print(a)
print(a.shape)

b = np.expand_dims(a, axis=0)
print(b)
print(b.shape)

c = a[np.newaxis, : ]
print(c)
print(c.shape)

d = np.expand_dims(a, axis=1)
print(d)
print(d.shape)

e = a[: , np.newaxis]
print(e)
print(e.shape)
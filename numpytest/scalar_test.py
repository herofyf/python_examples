# http://www.python-course.eu/matrix_arithmetic.php

import numpy as np

x = np.array([1,2,3])
y = np.array([-7, 8, 9])

# a.b = a1b1 + a2b2 + a3b3
z = np.dot(x, y)
print(z)

# and a.b= |a|.|b|.cos(x)
# so
x_length = np.sqrt((x* x).sum())
y_length = np.sqrt((y* y).sum())

cosXVal = z / x_length / y_length

# base on cosx value to arc value
angle_arc = np.arccos(cosXVal)

# to based on arc value to calculate angle
angle = angle_arc * 360 / 2 / np.pi
print(angle)
# http://www.python-course.eu/matplotlib_contour_plot.php

import numpy as np

xlist = np.linspace(-3.0, 3.0, 3)
ylist = np.linspace(-3.0, 3.0, 4)
X, Y = np.meshgrid(xlist, ylist)
Z = np.sqrt(X ** 2 + Y **2)

import matplotlib.pyplot as plt
plt.figure()

# 0.5一个间隔，将相同的[(x + 0.5, y), (x + 0.5, y+ 0.5), (x+1, y), (x+1, y+1)...] 算出的值Z,将相同的值各自连接成一条线
# 也就是说算z值方法决定了等值线的形状，因为只有相同z值的才会在一个线上，比如上面的x **2, y ** 2,就是一个圆
cp = plt.contour(X, Y, Z)
plt.clabel(cp, inline=True, fontsize = 10)
plt.title('Contour Plot')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.show()
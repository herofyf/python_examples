__author__ = 'Land'

# http://blog.csdn.net/u013634684/article/details/49646311
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax1 = fig.add_subplot(221)
N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
ax1.scatter(x, y, color="blue", s =7, edgecolor='none')

# plot 1
ax1_daratio = ax1.get_data_ratio()
ax1.set_aspect(1./ ax1_daratio)

# plot 2
ax2 = fig.add_subplot(222)
x = np.arange(1, 10)
y = x
sVal = x * 10
ax2.scatter(x, y, s = sVal, c='r', marker='x')
plt.legend('x1')

# plot 3
ax3 = fig.add_subplot(223)
clist= ['r', 'g', 'b']

cVal = [clist[i] for i in np.random.randint(0, 3, len(x))]
ax3.scatter(x,y,c=clist,marker='s')


ax4 = fig.add_subplot(224)
props = dict(alpha=0.5, edgecolors='none')
ax4.scatter(x, y, **props)

plt.show()
__author__ = 'Land'


import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np


fig = plt.figure(1)

ax = fig.add_subplot(111, autoscale_on=False, xlim=(-1, 5), ylim= (-4,3))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=3, color='purple')
'''
ax.annotate('test', (1,1), xycoords='data', xytext=(2, 2),
            textcoords='offset points', arrowprops=dict(arrowstyle="->"))
'''
ax.annotate('arc', xy=(1., 1), xycoords='data',
                xytext=(-40, 30), textcoords='offset points',
                arrowprops=dict(arrowstyle="->",
                                connectionstyle="arc,angleA=0,armA=30,rad=10"),
                bbox = dict(boxstyle='round', fc = '0.5', color='g'),
                color = 'r'
                )


plt.show()
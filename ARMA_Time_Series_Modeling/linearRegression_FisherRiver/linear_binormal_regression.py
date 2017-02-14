import numpy as np
import matplotlib.pyplot as plt

k = 1
m = -5

# linear regression
y = lambda x: k * x + m

# sigmod regression
p = lambda x: 1 / (1 + np.exp(-1 * (k * x + m)))

xx = np.linspace(0, 10)
plt.plot(xx, y(xx), label='linear')
plt.plot(xx, p(xx), label='logistic')

# to draw one line
plt.plot([0, abs(m)], [0.5, 0.5], dashes= (4, 4), color='.7')
#draw another line
plt.plot([abs(m), abs(m)], [0, 0.5], dashes= (4, 4), color='.7')

plt.ylim(-.1, 1.1)
plt.show()
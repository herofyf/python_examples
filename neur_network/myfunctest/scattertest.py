import numpy as np
import matplotlib.pyplot as plt
import math

N = 50
x = np.linspace(1, N, N)
y = np.linspace(20, 20 + N, N)
colors = np.random.rand(N)
#area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses
area =[(math.pow(x[i], 2) + math.pow(y[i], 2)) for i in range(N)]

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
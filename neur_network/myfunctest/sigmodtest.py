import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 256)

# start, stop, interval
Xaxis = np.arange(-10., 10., 0.2)
# Xaxis is an one-dimensional array with 100 elements
# begin from -10.0 to 10.0, with interval of 0.2 for each two elements

# start, stop, number
Yaxis = np.linspace(0, len(Xaxis), len(Xaxis))
# Yaxis is also an one-dimensional arry with 100 elements
# begin from 0 to 100


import math
def sigmoid(x):
    a = []
    for item in x:
        a.append( 1 / (1 + math.exp(-item)))
    return a

sig = sigmoid(Xaxis)
plt.plot(Xaxis, sig)
plt.show()
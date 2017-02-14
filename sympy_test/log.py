
__author__ = 'Land'

# http://mattpap.github.io/scipy-2011-tutorial/html/basics.html

# http://reverland.org/python/2012/08/30/sympy-tutorial/
# in windows console to input isympy
import numpy as np
import matplotlib.pyplot as plt

x= np.arange(-4, 4, 0.5)
f = 1 / (1 +  pow(np.e, -x))
print(x)


fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x, f)

x = np.linspace(-2*np.pi, 2*np.pi, 100)
xx = x + 1j * x[:, np.newaxis]
out = np.exp(xx)
print(out)
axes[1].imshow(np.abs(out),
               extent=[-2 * np.pi, 2 * np.pi, -2 * np.pi, 2 * np.pi])

plt.show()


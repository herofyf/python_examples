__author__ = 'Land'
# http://people.duke.edu/~ccc14/pcfb/numpympl/MatplotlibBarPlots.html

# http://blog.csdn.net/ywjun0919/article/details/8692018
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

# 0-1 has 1000
#x = np.random.normal(0,1,1000)

# [0, 10) to get 30
#x = np.random.randint(0, 10, 30)


#x = np.linspace(0, 10, 11)
# seperate with 5 part index


x= [1, 1, 1, 2, 3,3,5, 5, ]
numBins = 3
ax.hist(x, numBins, color='green', alpha =0.8)
print(x)
counts, bins = np.histogram(x, numBins)
print(counts)
print(bins)
#counts_n = counts / (sum (counts * np.diff(len(bins))))

plt.show()

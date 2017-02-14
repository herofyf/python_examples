
from sklearn import datasets

'''
In[19]: type(digits.data)
Out[19]: numpy.ndarray
In[20]: digits.data.shape
Out[20]: (1797, 64)
In[21]: type(digits.images[0])
Out[21]: numpy.ndarray
In[22]: digits.images[0].shape
Out[22]: (8, 8)
'''
from  sklearn import svm

digits = datasets.load_digits()
clf = svm.SVC(gamma=0.001, C = 100)

# USE THE COUND -10 to train
X, y = digits.data[:-10], digits.target[:-10]
clf.fit(X, y)
print(clf.predict(digits.data[-7]))

import matplotlib.pyplot as plt
plt.imshow(digits.images[-7], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
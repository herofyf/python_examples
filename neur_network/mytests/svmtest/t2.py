import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm
x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]


X = np.array(list(zip(x, y)))
z = [0,1,0,1,0,1]

clf = svm.SVC(kernel='linear', C = 1.0)
clf.fit(X, z)
#print(clf.predict())

w = clf.coef_[0]
print(w)

a = -w[0] / w[1]
xx = np.linspace(0, 12)
yy = a * xx - clf.intercept_[0] / w[1]
h0 = plt.plot(xx, yy, 'k-', label = 'non wighted div')
plt.scatter(x,y)
plt.show()
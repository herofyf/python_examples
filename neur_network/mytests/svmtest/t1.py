# https://www.analyticsvidhya.com/blog/2015/10/understaing-support-vector-machine-example-code/

from sklearn import svm, datasets
import numpy as np
import matplotlib.pyplot as plt

#import some data to play with
iris = datasets.load_iris()
# take first two feature
X = iris.data[:, :2]
# avoid this ugly slicing by using a two-dim dataset
y = iris.target

# Assumed you have, X(predictor) and Y(target) for training data set and x_test(predictor)
# of test_dataset

# create SVM classification object
svc = svm.SVC(kernel = 'rbf', C =1, gamma = 0)

# there is various option associated with it, like changing kernel, gamma and C value.
# Will discuss more about it in next section.
# Train the model using the training sets and check score
svc.fit(X, y)
svc.score(X, y)

# feature1 as x, feature 2 as y
x_min, x_max = X[:, 0].min() -1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() -1, X[:, 1].max() + 1
step = (x_max / x_min) / 100
xx, yy = np.meshgrid(np.arange(x_min, x_max, step),
                np.arange(y_min, y_max, step))

plt.subplot(1,1,1)
# xx.ravel: 将ndarray展开成一维数组
# np.c_ : numpy.c_?
Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, cmap = plt.cm.Paired, alpha = 0.8)

# X[..0] is x, X[..1] is y. c is color.
plt.scatter(X[:, 0], X[:, 1], c = y, cmap=plt.cm.Paired)
plt.xlabel('sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.title('SVC with linear kernel')
plt.show()

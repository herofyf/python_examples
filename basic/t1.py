import numpy as np

X = np.linspace(0, 1)
Y = 3 *X + 5
X1 = [[x - 0.1] for x in X]
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, linear_model

lr = linear_model.LinearRegression()
lr.fit(X1, Y)
print(lr.coef_)
print(lr.intercept_)
def show_lr_plot():
    # show scatter
    plt.scatter(X1, Y)

    X2 = [[1.1], [1.3], [1.5], [1.11]]
    plt.plot(X2, lr.predict(X2), color ='red')

    plt.show()

show_lr_plot()




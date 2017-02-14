import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from MasteringPythonDataAnalysis.mydespine import despine
co2_gr = pd.read_csv('co2_gr_gl.txt', delim_whitespace=True,
                     skiprows=62, names=['year', 'rate', 'err'])

def showOrigin():
    fig, ax = plt.subplots(1,1)
    ax.errorbar(co2_gr['year'],
                co2_gr['rate'],
                yerr= co2_gr['err'],
                ls = 'None',
                elinewidth=1.5,
                capthick=1.5,
                marker = '.',
                ms = 8)
    despine(ax)
    plt.minorticks_on()
    #plt.show()

from sklearn.linear_model import LinearRegression, Lasso
from sklearn import cross_validation
x_test, x_train, y_test, y_train =\
cross_validation.train_test_split(
    co2_gr['year'], co2_gr['rate'],
    test_size= 0.75, random_state=0
)
X_train = x_train[:, np.newaxis]
X_test = x_test[:, np.newaxis]
line_x = np.array([1955, 2025])

est_lin = LinearRegression()
est_lin.fit(X_train, y_train)
temp = line_x.reshape(-1, 1)
lin_pred = est_lin.predict(temp)

def printStuff(estimator, A, b):
    name = estimator.__str__()
    name = name.split('(')[0]
    print('+'*6, name, '+'* 6)
    print('Slope: {0:.3f} Intercept:{1:.2f} '.format(
        estimator.coef_[0], estimator.intercept_))
    predTest = estimator.predict(A)
    print("Mean squared residuals: {0:.2f}".format(
        np.mean(predTest - b) ** 2
    ))
    print("Variance score: {0:.2f}".format(
        estimator.score(A, b)
    ))

printStuff(est_lin, X_test, y_test)



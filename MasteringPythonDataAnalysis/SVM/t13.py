import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from MasteringPythonDataAnalysis.mydespine import *




X_best = SelectKBest(chi2, k = 2).fit_transform(X_pre, labels)

fig = plt.figure()

# 从上面的select kbest得到的最佳匹配属性为A, asym
def showBestFitProperties(fig):
    ax = fig.add_subplot(111)
    ax.scatter(seeds.A[gr1], seeds.asym[gr1], color='LightCoral')
    # put x,y =seeds.P[gr1].mean(), seeds.lgro[gr1].mean()
    ax.text(seeds.P[gr1].mean(), seeds.asym[gr1].mean(), '1',
            bbox=dict(color='w', alpha=0.7, boxstyle='Round'))
    ax.scatter(seeds.A[gr2], seeds.asym[gr2], color='SteelBlue', marker = 's')
    ax.text(seeds.A[gr2].mean(), seeds.asym[gr2].mean(), '2',
            bbox=dict(color='w', alpha=0.7, boxstyle='Round'))
    ax.scatter(seeds.A[gr3], seeds.asym[gr3], color ='Green', marker='<')
    ax.text(seeds.A[gr3].mean(), seeds.asym[gr3].mean(), '3',
            bbox=dict(color='w', alpha=0.7, boxstyle='Round'))


from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
res = 0.01
X, y = X_best, labels


#showBestFitProperties(fig)
from MasteringPythonDataAnalysis.SVM.plot_svmresult import *

linearSvm = LinearSvm(X , y, 'linear SVM')
linearSvm.plotSvmResult()
#plt.show()
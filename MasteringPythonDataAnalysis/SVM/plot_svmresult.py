from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

class SvmCalculator:
    def __init__(self):
        pass

    def loadDataset(self):
        seeds = pd.read_csv('seeds_dataset.txt', delim_whitespace=True,
                            names=['A', 'P', 'C', 'lkern', 'wkern',
                                   'asym', 'lgro', 'gr'])
        self.seeds = seeds

    def selectBestAttribs(self, k = 2):
        # return narray[[], []]
        X_raw = self.seeds.as_matrix()
        # LABLE 就是最后一列， x_pre就是除最后一列的，-1就是最后一列，用在slice当中就是不包括
        X_pre, labels = X_raw[:, :-1], X_raw[:, -1]
        self.attribNum = k
        gr1 = seeds.gr == 1
        gr2 = seeds.gr == 2
        gr3 = seeds.gr == 3

    def plotSvmResult(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.subplots_adjust(wspace = 0.2, hspace = 0.4)
        x_min, x_max = self.xy[:, 0].min() - 1, self.xy[:, 0].max() + 1
        y_min, y_max = self.xy[:, 1].min() - 1, self.xy[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, self.steps),
                             np.arange(y_min, y_max, self.steps))
        xxyy = np.vstack((xx.flatten(), yy.flatten())).T
        Z = self.svc.predict(xxyy)
        Z = Z.reshape(xx.shape)


class LinearSvm(SvmCalculator):
    def __init__(self):
        SvmCalculator.__init__(self)
        self.svc = svm.SVC(kernel='linear', C = 1.).fit(self.xy, self.label)

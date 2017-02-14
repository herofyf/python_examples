import pandas as pd
import numpy as np
from MasteringPythonDataAnalysis.mydespine import *

seeds = pd.read_csv('seeds_dataset.txt', delim_whitespace=True,
                    names=['A', 'P', 'C', 'lkern', 'wkern',
                           'asym', 'lgro', 'gr'])
gr1 = seeds.gr == 1
gr2 = seeds.gr == 2
gr3 = seeds.gr == 3
pars = ['A', 'C', 'P', 'asym', 'lgro', 'lkern', 'wkern']
# adjust coloumn position and filter the records with gr1
data = seeds[pars][gr1]
# 每一列对应一图，因为hist只需要一个序列，而不像plot需要两个序列(X,Y)来对应一个点
axes = data.hist(figsize = (8, 6))
flat_axes = axes.flatten()
list_flat_axes = list(flat_axes)
despine(list_flat_axes)
_ = [ax.grid() for ax in list_flat_axes]
_ = [ax.locator_params(axis = 'x', nbins = 4) for ax in
     list_flat_axes]
_ = [ax.locator_params(axis= 'y', nbins = 2) for ax in
     list_flat_axes]
plt.subplots_adjust(wspace = 0.5, hspace=0.7)
plt.show()
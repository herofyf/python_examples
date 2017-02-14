import pandas as pd
import csv
from statsmodels.tsa.stattools import adfuller
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import statsmodels.tsa.stattools as stt
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib
from seaborn import despine

def is_stationary(df, maxlag = 15, autolag = None, regression = 'ct'):
    """
        Run the Augmented Dickey-Fuller test from Statsmodels
         and print output
    """
    outpt = stt.adfuller(df, maxlag = maxlag, autolag= autolag,
                         regression=regression)
    print('adf\t\t {0:.3f}'.format(outpt[0]))
    print('p\t\t {0:.3g}'.format(outpt[1]))
    print('crit. val. \t:{0:.3f},\
           5%: {1:.3f}, 10%: {2:.3f}'.format(outpt[4]["1%"],
                    outpt[4]['5%'], outpt[4]['10%']))
    print('stationary?\t {0}'.format(['true', 'false']\
                                     [outpt[0] > outpt[4]['5%']]))
    return outpt

carsales = pd.read_csv('monthly-car-sales-in-quebec-1960.csv',
                        parse_dates=['Month'],
                        index_col= 'Month',
                        date_parser= lambda d: pd.datetime.strptime(d, "%Y-%m"))
#print(carsales)
#convert to Series
carsales = carsales.iloc[:, 0]
is_stationary(carsales)

import matplotlib.pyplot as plt

def change_plot(ax):
    despine()
    ax.locator_params(axis='y', nbins = 7)
    plt.setp(ax.get_xticklabels(), rotation= 90, ha='center')

carsales_decomp = seasonal_decompose(carsales, freq= 12)
carsales_trend = carsales_decomp.trend
carsales_seasonal = carsales_decomp.seasonal
carsales_residual = carsales_decomp.resid
plt.figure(figsize=(9, 4.5))
plt.subplot(221)
plt.plot(carsales, color='Green')
change_plot(plt.gca())
plt.title('Sales', color='Green')
x1 = plt.xlim()
y1 = plt.ylim()

plt.subplot(222)
plt.plot(carsales.index, carsales_trend, color = 'Coral')
change_plot(plt.gca())
plt.title('Trend', color = 'Coral')
plt.xlim(x1)
plt.ylim(y1)

plt.subplot(223)
plt.plot(carsales.index, carsales_seasonal,
         color ='SteelBlue')
change_plot(plt.gca())
plt.gca().xaxis.tick_bottom()
# now show any xlabel, becuase NullFormatter is to show null
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())
plt.xlabel('Seasonality', color='SteelBlue', labelpad = -20)
plt.xlim(x1)
plt.ylim((-8000, 8000))

plt.subplot(224)
plt.plot(carsales.index, carsales_residual,
         color = 'IndianRed')
change_plot(plt.gca())
plt.xlim(x1)
plt.gca().yaxis.tick_right()
plt.gca().yaxis.set_label_position('right')
plt.gca().xaxis.tick_top()
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())
plt.ylim((-8000, 8000))
plt.xlabel('Residuals', color='IndianRed', labelpad = -20)

plt.tight_layout()
plt.subplots_adjust(hspace = 0.6)
plt.show()





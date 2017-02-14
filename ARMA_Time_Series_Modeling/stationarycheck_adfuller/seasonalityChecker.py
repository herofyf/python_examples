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
import matplotlib.pyplot as plt

carsales = pd.read_csv('monthly-car-sales-in-quebec-1960.csv',
                        parse_dates=['Month'],
                        index_col= 'Month',
                        date_parser= lambda d: pd.datetime.strptime(d, "%Y-%m"))
#print(carsales)
#convert to Series
carsales = carsales.iloc[:, 0]

carsales_decomp = seasonal_decompose(carsales, freq= 12)
carsales_trend = carsales_decomp.trend
carsales_seasonal = carsales_decomp.seasonal
carsales_residual = carsales_decomp.resid

fig = plt.figure(figsize = (7, 1.5))
ax1 = fig.add_axes([0.1, 0.1, 0.6, 0.9])
ax1.plot(carsales_trend, color = 'Green', label='Detrended data')
ax1.plot(carsales_seasonal, color='Coral', label='Seasonal component')
kwrds = dict(lw=1.5, color='0.6', alpha = 0.8)
d1 = pd.datetime(1960, 9, 1)
dd = pd.Timedelta('365 Days')
d2 = pd.datetime(1960, 5, 1)
[ax1.axvline(d1 + dd * i, dashes=(3,5), **kwrds) for i in range(9)]
plt.show()


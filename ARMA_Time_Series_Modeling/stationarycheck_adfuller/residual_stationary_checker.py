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
import scipy.stats as st

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

loc, shape = st.norm.fit(carsales_residual)
x = range(-3000, 3000)
y = st.norm.pdf(x, loc, shape)
n, bins, patches = plt.hist(carsales_residual, bins= 5,
                            normed= True)
plt.plot(x, y, color ='Coral')
plt.title('Residuals')
plt.xlabel('Value')
plt.ylabel('Counts')
plt.show()

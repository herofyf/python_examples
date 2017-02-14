import pandas as pd
import numpy as np
import matplotlib.pylab as plt

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

data = pd.read_csv('AirPassengers.csv')
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
data = pd.read_csv('AirPassengers.csv',  index_col='Month', date_parser=dateparse)
ts = data[u'#Passengers']

ts_log = np.log(ts)


from ARMA_Time_Series_Modeling.airpassenders_test.test_stationarity import *

#draw_ts(ts_log)

draw_trend(ts_log, 10)

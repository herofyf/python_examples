# -*- coding:utf-8 -*-
from statsmodels.tsa.stattools import adfuller
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def draw_ts(ts):
    f = plt.figure(facecolor='white')
    ts.plot(color ='blue')
    plt.show()

def draw_trend(ts, size):
    f = plt.figure(facecolor='white')
    ts.plot(color='blue')
    # to calculate the mean of the ts
    rol_mean = ts.rolling(window= size).mean()
    rol_mean.plot(color ='red')
    # calculate weighted average
    #rol_weighted_mean = pd.ewma(ts, span= size)
    rol_weighted_mean = ts.ewm(min_periods= 0, span= size).mean()
    rol_weighted_mean.plot(color='black')
    plt.show()
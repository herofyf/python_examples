import pandas as pd
from seaborn import despine
import matplotlib.pyplot as plt

dateparse = lambda d: pd.datetime.strptime(d, '%Y-%m-%d')

temp = pd.read_csv('mean-daily-temperature-fisher-ri.csv',
parse_dates=['Date'],
index_col='Date',
date_parser=dateparse)

def show1():
    # TO CONVERT SERIES
    x = temp.iloc[:, 0]
    x.plot(lw = 1.5)
    despine()
    plt.gcf().autofmt_xdate()
    plt.show()

def show2():
    temp['1988-01'][temp > 15].plot(ls='dotted', marker='.')
    despine()
    plt.gcf().autofmt_xdate()
    plt.ylabel('Temperature')
    plt.show()



#show1()
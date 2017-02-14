# http://www.10tiao.com/html/284/201608/2652390079/1.html

import pandas as pd

discfile = 'Book1.xlsx'
data = pd.read_excel(discfile, index_col=u'日期')
#print(data)

forecastnum = 5




import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] =  False


# 自相关图
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import  plot_pacf

# 平稳性检测
from statsmodels.tsa.stattools import adfuller as ADF

# 白噪音检测
from statsmodels.stats.diagnostic import acorr_ljungbox

D_data = data.diff().dropna()
D_data.columns = [u'销售差分']

def showResult():
    #data.plot()
    #print(u'原始序列的ADF检验结果为:', ADF(data[u'销量']))
    #plot_acf(data).show()

    plot_pacf(D_data).show()
    print(u'销售差分ADF检验结果为:', ADF(D_data[u'销售差分']))
    print(u'差分序列白噪音检测结果为:', acorr_ljungbox(D_data, lags=1))
    plt.show()

from statsmodels.tsa.arima_model import ARIMA

def predictARIMA():
    n = type(data)
    print(n)


#showResult()

predictARIMA()
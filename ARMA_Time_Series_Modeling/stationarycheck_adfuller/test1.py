
import pandas as pd
import csv
from statsmodels.tsa.stattools import adfuller
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import statsmodels.tsa.stattools as stt
from statsmodels.tsa.seasonal import seasonal_decompose

# to select 0 colum that is sale number
# because month is index column

'''

def read_csv(fileName):
    f = open(fileName, 'rt')
    reader = csv.reader(f)

    headers = reader.__next__()
    column = {}
    for h in headers:
        column[h] = []
    for row in reader:
        for h,v in zip(headers, row):
            column[h].append(v)
    return column

x = read_csv('monthly-car-sales-in-quebec-1960.csv')
x["Month"] = [pd.datetime.strptime(d, "%Y-%m") for d in x['Month']]
print(x['Month'])
'''
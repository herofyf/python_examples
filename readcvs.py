__author__ = 'Land'

import os, sys
import csv

file_name = os.path.dirname(sys.argv[0]) + '/test1.cvs'

data=[]

with open(file_name) as cvsfile:
    readCVS = csv.reader(cvsfile, delimiter=',')

    for row in readCVS:
        ele= []

        ele.append(row[0])
        ele.append(row[1])
        ele.append(row[2])
        ele.append(row[3])
        data.append(ele)

print(data)

count = 0

def Fib(val):
    global count
    if (val < 0):
        return count


    count = val + Fib(val-1)
    val -= 1
    return count
print(Fib(4))

import numpy as np
cond= [[True, False], [True, True]]

x= [[1, 2], [3, 4]]
y= [[9, 8], [7, 6]]

res = np.where(cond, x, y)
print(res)

import pylab as pl
import numpy as np
from scipy import stats

import math

val1 = math.factorial(3)
print(val1)


class Works:
    def __init__(self):
        pass

    def __getitem__(self, key):
        if isinstance(key, tuple):
            for item in key:
                if  isinstance(item, slice):
                    print("%d , %d" % (item.start, item.stop))
                else:
                    print(item)


val = Works()
var = val[2:2,3]


def test_reduce():
    x = [1,2,3,4,5,56,7]
    y = reduce(lambda x, y: x + y, x)
    return y


import pandas as pd
import numpy as np

x = pd.DataFrame({
    'x': pd.Series([1, 2]),
    'y': pd.Series(['m', 'n'])})

def show(x):
    print('****')
    print(x)
    return x

c = x.apply(show)
print(c)
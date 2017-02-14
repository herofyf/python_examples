import pandas as pd
import numpy as np

import pprint as pp

df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])

df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])

df3 = df + df2
print(df)
print(df2)
print(df3)

#pp = pp.PrettyPrinter(indent=4)
pp.pprint(df)


dates = pd.date_range('1/1/2000', periods=2)

df = pd.DataFrame(np.random.randn(2, 2), index=dates, columns=list('AB'))
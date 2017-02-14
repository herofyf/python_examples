
# http://chrisalbon.com/#Python
import pandas as pd

data = {'score': [1,1,1,2,2,2,3,3,3]}
df = pd.DataFrame(data)

# Calculate the moving average. That is, take
# the first two values, average them,
# then drop the first and add the third, etc.
pd.rolling_mean(df, 2)
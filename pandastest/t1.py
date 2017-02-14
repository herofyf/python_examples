import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, 6, np.nan, 44, 1])
print(type(s))

dates = pd.date_range('20160101', periods= 2)
print(dates)

# method 1
fg = pd.DataFrame(np.arange(8).reshape(2, 4),
                    index= dates,
                    columns=('a','b','c','d'))
print(fg)

# method 2
dates = pd.date_range('20160101', periods= 5)
fg1 = pd.DataFrame(
    {   'a': 1,
        'b': pd.date_range('20160101', periods= 5),
        'name': np.arange(5),
        'c': pd.Series(1, index = list(range(5)), dtype = 'float32'),
        'd': np.array([3] * 5, dtype = 'int32'),
        'e': pd.Categorical(['t1', 't2', 't3', 'sdf', 'dddds']),
        'f': 'foo'
    },
    index= dates    # if not define, 0-4 will be used
)

print(fg1.index)
print(fg1)

fg1.sort_index(axis=0, ascending= False)
fg1.sort_values(by='e')

# two methods are same. to show column a
print(fg1['a'])
print(fg1.a)

# to show the rows with position
print(fg1['2016-01-03':'2016-01-05'],
      #only show 'a','b' two columns
      fg1[0:3]
      )
'''
select a column: df['dep'] or df.dep
select the first 3 row(ahead): df[:2]
to use label to select data, df.loc[row label, column label]
select the first 2 columns: df.loc[:,('one','two')] or to use df.loc[:,df.columns[:2]]
to use position to select data: df.iloc[row position, column position]
df.iloc[:,:2]
auto choose the slice type: df.ix[row position or label, column position or label]

'''

# select by label
print(fg1.loc['2016-01-03':'2016-01-05'])

print(fg1.iloc[1:2,1:3])
print(fg1.ix[:3, :])

print(fg1[fg1.e =='t1'])

# to set value

# to set all of columns when the row value satisfies conditions
#fg1.name[fg1.name >1] = 4
print(fg1)

#add now f column
fg1['g'] = 2
print(fg1)

# insert new column (column name i)with column position =1, and its value
fg1.insert(1, 'i', fg1['g'])
print(fg1)

del fg1['a']

# combine
s1= pd.Series([1, 2])
s2 = pd.Series([3, 4])
# when axis is 1, means s1 and s2 is column-origin,
#   1    3
#   2    4
s3 = pd.concat([s1, s2], axis =1)

# rename column name from a= again
fg_tmp = fg1.rename({'a': 'again'}, inplace=True)

print(fg1)
# remove "again" column, inplace means just replace current fg1
fg1.drop(labels=['f'], axis= 1, inplace= True)

# 1: index, 0: columns
fg1.drop(labels=[pd.Timestamp('2016-01-02')], axis = 0, inplace = True)
print(fg1)
fg1 = fg1[fg1.e == 't1']
print(fg1)

# to drop rows which values has none value
# because axis =1 means column to be dropped
print('test drop')
fg2 = fg1.dropna(axis = 1, how='any') # how {'any', 'how'}
print(fg2)
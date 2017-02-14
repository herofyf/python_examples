
## map 对每一个元素进行操作
a=['a', 'b', 'c']

b = map(lambda x: x + ";", a)
print([item for item in b])


## filter对每个元素进行操作，filter 函数返回的是True/False
# filter function returns true or false
def filter_func(x):
    if (x == 'a'):
        return True

    return False

c = filter(filter_func , a)
print([item for item in c])

import functools

## x1 x2 x3 x4
# Reduce input(x1, x2) 结果放在x2中，然后再(x2, x3)
# x , y is input, and y also is result
'''
    1 * 2 -> 3
then (3, 4) -> 12
'''
c = functools.reduce(lambda x, y: x * y, [1,3,4])
print( c)


## apply there have :
'''
①
apply(a_function, a_list_of_args)
a_function(*a_list_of_args)
②
apply(a_function, a_list_of_args, a_dictionary_of_named_args)
a_function(*a_list_of_args, **a_dictionary_of_named_args)
③
apply(a_function, a_list_of_args + z)
a_function(*a_list_of_args + z)
④
apply(aModule.a_function, a_list_of_args)
aModule.a_function(*a_list_of_args)

in python 3 it is function instead of apply
'''

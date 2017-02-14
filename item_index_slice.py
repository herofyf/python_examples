import  numpy as np
import matplotlib.pyplot as plt

class A:
    def __init__(self):
        pass

    def __getitem__(self, item):
        if  isinstance(item, tuple):
            itemslice = item[1]
            if  isinstance(itemslice, slice):
                print(itemslice)


a = A()
x = a[1,2:3]
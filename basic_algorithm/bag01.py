import random
import numpy as np
class Product:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight

    def __str__(self):
        ret = 'price=' + str(self.price) + ', weight =' + str(self.weight)
        return ret

NUM=10
products = []
for i in range(10):
    product = Product(random.randint(1, 100), random.randint(10, 50))
    products.append(product)

MW = np.array([product.weight for product in products]).mean() * NUM * 0.5

def showProducts():
    for product in products:
        print(product)

selectedBags = [0] * len(products)

'''
  从bag中选择一个满足weight的最大值
'''
def FindMaxWorth(curWegith):
    maxPrice = 0
    selectedIdx = -1
    for i in range(len(products) - 1):
        if selectedBags[i] == 0:
            if (products[i].weight + curWegith < MW):
                if (products[i].price > maxPrice):
                    maxPrice = products[i].price
                    selectedIdx = i
    return selectedIdx

import math
'''
当前是否选择idx背包，根据当前的S重量
'''
def searchMostValuable(idx, accumW):
    if (accumW > MW):
        return 0
    if idx >= len(products):
        return 0

    return max(searchMostValuable(idx + 1, accumW + products[idx].weight) + products[idx].price,
               searchMostValuable(idx + 1, accumW))

result = searchMostValuable(0, 0)
print(result)

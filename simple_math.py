__author__ = 'Land'

import operator

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1

    sortedClassCount = sorted(classCount.iteritems(), key= operator.itemgetter(1), reverse = True)
    print(sortedClassCount)

classList = [1, 3, 1, 4]
majorityCnt(classList)

class op:
    def __init__(self, init):
        pass

    def set(self, val):
        print("fdfd")
        return True

def myname(val):
    print(val)

x1 = myname
x1(2)
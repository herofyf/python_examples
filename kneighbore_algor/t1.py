
# http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

# read csv
import csv
import sys
import random


def loadDataset(fileName, split, trainingSet=[], testSet = []):
    with open('iris.data', 'rt') as f:
        try:
            # lines is iterator, so can be convert to list
            lines = csv.reader(f)

            dataSet = list(lines)

            # each row is list type, but the element is str type
            for i in range(len(dataSet) -1):
                for j in range(4):
                    # convert to str to float
                    dataSet[i][j] = float(dataSet[i][j])

                    if (random.random() < split):
                        trainingSet.append(dataSet[i])
                    else:
                        testSet.append(dataSet[i])


        finally:
            f.close()

# import package. if package include "all" definition. all definition libraries would be loaded
# otherwise from package.library import * / from package import library. you should know which package's library
import math
def euclideanDistance(pt1, pt2, dimen):

    distance = 0
    for i in range(dimen):
        distance += math.pow((pt1[i] - pt2[2]), 2)

    return math.sqrt(distance)


import operator
# 测试数据与training的数据相差最近的就是那个类别
# k is the proboblity neighbors, from high probolity to low
def getNeighbors(trainingSet = [], testSet = [], k = 0):
    neighbors = []

    distances = []
    length = len(testSet)
    for i in range(len(trainingSet)):
        distance = euclideanDistance(testSet, trainingSet[i], 3)
        distances.append((trainingSet[i], distance))

    # base on distance
    distances.sort(key = operator.itemgetter(1))
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

# neighbors 可能有不同的可能结果类型，有些是重复的，重复最多的获胜
def getResponse(neighbors):

    classResp = {}
    neigNum = len(neighbors)

    for x in range(neigNum):
        neig = neighbors[x][-1]
        if neig in classResp:
            classResp[neig] += 1
        else:
            classResp[neig] =  1

    # classResp.items to convert to (key, value)
    sortedClassResp = sorted(classResp.items(), key = operator.itemgetter(1), reverse = True)

    return sortedClassResp[0][0]

def getAccuracy(testSet, predict):
    tstSetCount = len(testSet)
    predictOkCount = 0
    for i in range(tstSetCount):
        if (testSet[i][-1] == predict[i]):
            predictOkCount += 1

    return (predictOkCount / float(tstSetCount)) * 100.0

'''
trainingSet = []
testSet = []
loadDataset('iris.data', 0.66, trainingSet, testSet)
x = pow(2,2)

trainingSet = [[2,2,2, 'a'], [5, 5, 5, 'b']]
testSet = [3,3,3]
neighbors = getNeighbors(trainingSet, testSet, 1)

neighbors = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
response = getResponse(neighbors)
print(response)


testSet = [[1,1,1, 'a'], [2,2,2, 'a'], [3,3,3, 'b']]
predict = ['a', 'a', 'a']
accuracy = getAccuracy(testSet, predict)
print(accuracy)
'''

def main():
    # prepare data
    trainingSet = []
    testSet = []
    loadDataset('iris.data', 0.67, trainingSet, testSet)
    predictions = []
    k = 3
    for i in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[i], k)
        response = getResponse(neighbors)
        predictions.append(response)
        print('> predictions:', response, ", actually=", testSet[i][-1])

    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy:' + repr(accuracy) + "%")

main()
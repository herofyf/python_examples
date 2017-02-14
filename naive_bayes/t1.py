# http://machinelearningmastery.com/naive-bayes-classifier-scratch-python/

import csv
import random
import math

def loadCsv(filename):
    rf = open(filename, "r")
    # lines is iterator object, not list object
    lines = csv.reader(rf)
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]

    return dataset

filename = 'pima-indians-diabetes.csv'
dataset = loadCsv(filename)
print('Loaded data file {0} with {1} rows'.format(filename, len(dataset)))

def splitDataset(dataset, splitRatio):
    # how many training item
    trainSize = int( (len(dataset)) * splitRatio)

    trainSet = []
    copy = list(dataset)

    while (len(trainSet)) < trainSize :
        # range is return list , but random
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
        # we need to pop the elemant, the rest is test data

    return [trainSet, copy]

dataset = [[1], [2], [3], [4], [5]]
splitRatio = 0.67
train, test = splitDataset(dataset, splitRatio)
print('Split {0} rows into train with {1} and test with {2}'.format(len(dataset), train, test))

def separateByClass(dataset):
    separated = {}

    for item in dataset:
        if item[-1] not in separated:
            separated[ item[-1] ] = [item]
        else:
            separated[ item[-1] ].append(item)

    return separated
dataset = [[1, 20, 1], [2, 21, 0], [3, 22, 1]]
separated = separateByClass(dataset)
print('Separated instance<separateByClass>:{0}'.format(separated))

# zip 就是将
for item in zip(*dataset):
    print("zip dataset {0}".format(item))

def mean(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def stdev(numbers):

    avg = mean(numbers)

    stddev = sum([ pow(x - avg, 2) for x in numbers]) / float(len(numbers) - 1)
    return math.sqrt(stddev)

numbers = [1,2,3,4,5]
print('Summary of {0}: mean={1}, stdev={2}'.format(numbers, mean(numbers), stdev(numbers)))

'''
  求每一个属性的mean, stdev.
  结果是每一个对象有多个属性，求所有对象的各个属性mean, stdev
'''
def summarize(dataset):
    zipDataset = zip(*dataset)

    summaries = []

    for lAttribOneKind in zipDataset:
        meanVal = mean(lAttribOneKind)
        attribSummary = (meanVal, stdev(lAttribOneKind))
        summaries.append(attribSummary)

    del summaries[-1]
    return summaries

dataset = [[1, 20, 0], [2, 21, 1], [3, 22, 0]]
summary = summarize(dataset)
print("Attribute summaries<summarize>: {0}".format(summary))

def summarizeByClass(dataset):
    seperatedClasses = separateByClass(dataset)
    summarizedClasses = {}
    for instance, eachClassObjs  in seperatedClasses.items():
        summarizedClasses[instance] = summarize(eachClassObjs)

    return summarizedClasses

dataset = [[1,20,1], [2,21,0], [3,22,1], [4,22,0]]
val = summarizeByClass(dataset)
# 每个对象有两个属性，每个属性有两个值（mean, stdev）,因此返回的属性列表有两个属性summary表示
print("summarize by class<summarizeByClass>: {0}".format(val))

import math
'''
我们知道一个attribute的probabilty 的mean以及stdev,求相应的attribute对于具体值的probability
                          2
            -  (x - mean)
            -----------
               2 * stdev * stdev
exponent = e

p =  exponent / sqrt( 2 * stdev * stdev * pi)
'''
def calculateProbability(x, mean, stdev):
    exponent = math.exp(- (math.pow(x - mean, 2)) / (2 * math.pow(stdev, 2)))
    return (exponent / (math.sqrt(2 * math.pi) * stdev) )

x = 71.5
meanVal = 73
stdevVal = 6.2
probability = calculateProbability(x, meanVal, stdevVal)
print("Probability of belonging to this class<calculateProbability>: {0}".format(probability))

def calculateClassProbabilities(summaries, inputVector):

    probabilities = {}

    for instance, classSummaries in summaries.items():
        probability = 1
        for i in range(len(classSummaries)):
            mean, stdev =  classSummaries[i]
            x = inputVector[i]
            probability = probability * calculateProbability(x, mean, stdev)

        probabilities[instance] = probability
    return probabilities


# class 0两个属性，当前只定义了一个属性的mean, stdev值
summaries = {0: [(1, 0.5)], 1:[(20, 5.0)]}

# 一个对象的两个属性值，然后求哪个class的可能性, 这个对象的第二个属性用?表示,表示不计算，因为上面的只给出一个属性特征
# 比如上面要是定义成这样 summaries = {0: [(1, 0.5), (meanatt0, stdevatt0)], 1:[(20, 5.0), (meanatt1, stdevatt1)]}
inputVector = [1.1, '?']
probabilities = calculateClassProbabilities(summaries , inputVector)
print("Calculate class probabilites<calculateClassProbabilities>: {0}".format(probabilities))


def predict(summaries, inputVector):
    classProbabilities = calculateClassProbabilities(summaries, inputVector)

    candidate, probability = None, 0
    for instance, classProbability in classProbabilities.items():
        if (classProbability > probability) or candidate  is None:
            probability = classProbability
            candidate = instance

    return candidate

#
summaries = {'A': [(1, 0.5)], 'B':[(20, 5.0)]}
inputVector = [1.1, '?']
result = predict(summaries, inputVector)
print('Prediction<predict>: {0}'.format(result))


def getPredictions(summaries, testSet):
    predictions = []
    for i in range(len(testSet)):
        prediction = predict(summaries, testSet[i])
        predictions.append(prediction)

    return predictions


summaries = {'A': [(1, 0.5)], 'B': [(20, 5)]}
testSet = [[1.1, '?'], [19.1, '?']]
predictions = getPredictions(summaries, testSet)
print("Predictions<getPredictions>: {0}".format(predictions))

def getAccuracy(testSet, predictions):
    correct = 0
    for i in range(len(testSet)):
        if (testSet[i][-1] == predictions[i]):
            correct += 1

    return (correct / float(len(predictions))) * 100.0


testSet = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
predictions = ['a', 'a', 'a']
accuracy = getAccuracy(testSet, predictions)
print("Accuracy<getAccuracy> : {0}".format(accuracy))

def main():
    dataset = loadCsv("pima-indians-diabetes.csv")
    trainSet, testSet = splitDataset(dataset, 0.67)

    # get mean, stdev
    classSummaries = summarizeByClass(trainSet)

    preidctions = getPredictions(classSummaries, testSet)
    accuracy = getAccuracy(testSet, preidctions)

    print("accuracy: {0}".format(accuracy))

main()
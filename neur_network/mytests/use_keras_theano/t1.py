from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import number

dataset = np.loadtxt("pima-indians-diabetes.csv", delimiter=",")

X = dataset[:,0:8]
Y = dataset[:, 8]

model = Sequential()
model.add(Dense(12, input_dim= 8, init = 'uniform', activation='relu'))
model.add(Dense(8, init = 'uniform', activation='relu'))
model.add(Dense(1, init = 'uniform', activation='sigmoid'))

# compile
model.compile(loss = 'binary_crossentropy', optimizer='adam', metrics =['accuracy'])

model.fit(X, Y, nb_epoch=150, batch_size=10, verbose= 2)

Evalulate = False
if Evalulate == True:
    scores = model.evaluate(X, Y)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

ToPredict = True
if ToPredict == True:
    # calculate predictions
    predictions = model.predict(X)
    rounded = [x for x in predictions]
    print(rounded)

import numpy as np
import theano.tensor as T

# https://www.youtube.com/watch?v=GbYWEOjjsAI&list=PLXO45tsB95cKpDID642AjNkygrSR5X15T&index=7
import theano
import matplotlib.pyplot as plt

def compute_accuracy(y_target, y_predict):
    correct_prediction = np.equal(y_predict, y_target)
    accuracy = np.sum(correct_prediction) / len(correct_prediction)
    return accuracy

rng = np.random

N = 400
feats = 784

# generate a dataset : D=(input_values, target_class)
D = (rng.randn(N, feats), rng.randint(size = N, low =0, high=2))

# Declare Theano symbolic variables
x = T.dmatrix('x')
y = T.dvector('y')


# initialize the weights and biases
W = theano.shared(rng.randn(feats), name='w')
b = theano.shared(0., name='b')

# Construct Theano expression graph
p_1 = T.nnet.sigmoid(T.dot(x, W) + b)
prediction = p_1 > 0.5
#xent = -y * T.log(p_1) - (1- y) * T.log(1-p_1) # cost
xent = T.nnet.binary_crossentropy(p_1, y)
cost = xent.mean() + 0.01 *  (W ** 2).sum()       # to solve over-fitting
gW, gb = T.grad(cost, [W, b])

# Compile
learning_rate = 0.1
train = theano.function(
    inputs=[x, y],
    outputs=[prediction, xent.mean()],
    updates=(
        (W, W- learning_rate * gW),
        (b, b - learning_rate * gb))
    )

predict = theano.function(inputs=[x], outputs=prediction)
# Training:
for i in range(500):
    pred, err = train(D[0], D[1])

    if i % 50:
        print('cost:', err)
        print('accuracy:', compute_accuracy(D[1], predict(D[0])))

print("target values for D:")
print(D[1])
print("predicion on D:")
print(predict(D[0]))
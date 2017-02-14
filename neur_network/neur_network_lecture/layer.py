import numpy as np
import theano.tensor as T

# https://www.youtube.com/watch?v=GbYWEOjjsAI&list=PLXO45tsB95cKpDID642AjNkygrSR5X15T&index=7
import theano
import matplotlib.pyplot as plt
'''
to define the layer like this:
l1 = Layer(inputs, in_size =1, out_size =10, activation_function)
l2 = Layer(l1.outputs, 10, 1, None) : None indicate output directly just like linear operation
'''

class Layer(object):
    def __init__(self, inputs, in_size, out_size, activation_function):
        self.W = theano.shared(np.random.normal(0, 1, (in_size, out_size)))
        self.b = theano.shared(np.zeros((out_size,)) + 0.1)
        self.Wx_plus_b = T.dot(inputs, self.W) + self.b
        self.activation_function = activation_function

        if activation_function is None:
            self.outputs = self.Wx_plus_b
        else:
            self.outputs = self.activation_function(self.Wx_plus_b)

# Make up some fake data
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]

noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise   # x^2 -0.5 + noise




# determine the inputs dtype
x = T.dmatrix('x')
y = T.dmatrix('y')

# add layer
# 1 property and output 10 elements output
l1 = Layer(x, 1, 10, T.nnet.relu)

# l1 is 10 output, and the l2 is the ultimate result, just is y_data, so it is 1
l2 = Layer(l1.outputs, 10, 1, None)

# compute the cost
cost = T.mean(T.square(l2.outputs - y))

# compute the gradients
gW1, gb1, gW2, gb2 = T.grad(cost, [l1.W, l1.b, l2.W, l2.b])

# apply gradient descent
learning_rate = 0.05
train =  theano.function(
    inputs= [x, y],
    outputs= cost,       # to use cost express define above
    # each updates use ()
    #  1. UPDATE (l1.W - learning_rate * gW1) -> l1.W
    #  2.
    updates = [(l1.W, l1.W - learning_rate * gW1),
               (l1.b, l1.b - learning_rate * gb1),
               (l2.W, l2.W - learning_rate * gW2),
               (l2.b, l2.b - learning_rate * gb2)])



# prediction
predict = theano.function(inputs=[x], outputs= l2.outputs)

# show the fake data
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.scatter(x_data, y_data)
plt.ion() # no block while show.
plt.show()

for i in range(1000):
    # training
    err = train(x_data, y_data)

    if i % 50:
        #print(err)
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        # to visualize the result and improvement
        predict_value = predict(x_data)
        lines = ax.plot(x_data, predict_value, 'r-', lw=5)
        plt.pause(1)    # 1 second

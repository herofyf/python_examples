import numpy as np
import theano.tensor as T

from theano import function
import theano
import matplotlib.pyplot as plt

# activation function example
x = T.dmatrix('x')

s = 1 / (1 + T.exp(-x))
f = function([x], s)

from theano import pp
print(pp(s))
print(f([[2, 3], [0, -1]]))

# multiple outputs for a function
a, b = T.dmatrices('a', 'b')
diff = a - b
abs_diff = abs(diff)
diff_squared = diff **2
f = function([a, b], [a, b, diff, abs_diff, diff_squared])
print(f(np.ones((2,2)),
        np.arange(4).reshape(2,2))
     )

# name for a function
x, y, w = T.dscalars('x', 'y', 'w')
z = (x+y) * w
f = function([x, theano.In(y, value=1),
              theano.In(w, value=2, name='weights')]
              , z)
print(f(2, 1, 3))
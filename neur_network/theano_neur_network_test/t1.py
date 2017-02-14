import numpy

import theano
import theano.tensor as T

from theano import function
# 3- dimentsion ndarray
x = T.dtensor3('x')
y = T.dtensor3('y')

z = x + y

f = function([x, y], z)

print(f(
    [
        [
            [2,3], [1,1]
        ],
        [
            [3,3], [6,6]
        ]
    ],
    [
        [
            [4,3], [1,11]
        ],
        [
            [13,3], [16,6]
        ]
    ]))

debugStr = theano.printing.debugprint(f)
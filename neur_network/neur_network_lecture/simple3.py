import numpy as np
import theano.tensor as T

# https://www.youtube.com/watch?v=GbYWEOjjsAI&list=PLXO45tsB95cKpDID642AjNkygrSR5X15T&index=7
import theano

# pass value and name into shared
state = theano.shared(np.array(0, dtype= np.float64), 'state')

inc = T.scalar('inc', dtype= state.dtype)
accumulator = theano.function([inc], state, updates=[(state, state + inc)])

print(accumulator(10))
print(accumulator(10))

# get variable value
print(state.get_value())

# to set variable value onlyh for shared var
state.set_value(-1)
accumulator(2)
print(state.get_value())

# temporarily replace shared variable with another va

tem_func = state * 2 + inc
a = T.scalar(dtype= state.dtype)
# to achive tem_func, with var: a, inc
skip_shared = theano.function([inc, a], tem_func, givens=[(state, a)])

# at here: inc=2, a =2, and because givens to let state= 2, so result 8
print(skip_shared(2, 3))

# no change
print(state.get_value())

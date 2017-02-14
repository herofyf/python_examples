import numpy as np

x = np.linspace(0, 1, 10)
y = np.ones(5)
revertx = x[::-1]

'''
https://www.zybuluo.com/tankle/note/51606
http://blog.csdn.net/garfielder007/article/details/51378296
'''

# just like: np.concatenate((a, b), axis=0). y direction change, x not change
x = np.hstack((x, revertx))
print(x)

def holt_winters_second_order_ewma(x, span, beta):
    N = x.size
    alpha = 2.0 / (1 + span)

    s = np.zeros(N)
    b = np.zeros(N)

    s[0] = x[0]

    for i in range(1, N):

        s[i] = alpha * x[i] + (1 - alpha) (s[i - 1] + b[i -1])
        b[i] = beta * (s[i] - s[i -1]) + (1 - beta) * b[i -1]

    return s

x = np.linspace(0, 9, 10)
holt_winters_second_order_ewma(x, 3, 0.1)
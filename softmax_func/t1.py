import numpy as np
'''
They're both correct but yours has an unnecessary term.
You start with
e ^ (x - max(x)) / sum(e^(x - max(x))
By using the fact that a^(b - c) = (a^b)/(a^c) we have
= e ^ x / e ^ max(x) * sum(e ^ x / e ^ max(x))
= e ^ x / sum(e ^ x)
Which is what the other answer says. You could replace max(x) with any variable and it would cancel out.
'''
def softmax(x):
    fractions = np.exp(x)  # 分子
    numerator = np.sum(np.exp(x), axis = 0)
    return fractions / numerator

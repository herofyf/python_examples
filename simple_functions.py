__author__ = 'Land'

import math

def even_numbers_only(thelist):
    '''
    Returns a list of even numbers in thelist

    '''
    return [x for x in thelist if x%2 == 0]

def is_perfect_square(x):
    thesqrt = int(math.sqrt(x))
    return thesqrt * thesqrt ==x

text = "test"
def print_text():
    print(text)
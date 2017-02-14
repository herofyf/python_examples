'''
Essentially, decorators work as wrappers,
modifying the behavior of the code before and after a target function execution,
without the need to modify the function itself, augmenting the original functionality, thus decorating it.

'''

def greet(name):
    return "hello" + name

greetSomeone = greet
print(greetSomeone('john'))

# *param like tuple, ** like dictionary
def callPosFunc(func, *params):
    return func(*params)
    # or turn func(params[0])

def callNameFunc(func, **params):
    return func(**params)

print(callPosFunc(greetSomeone, 'ddd'))
print(callNameFunc(greetSomeone, name = 'ddd'))
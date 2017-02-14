# http://www.artima.com/weblogs/viewpost.jsp?thread=240845

# 对于有参数的，先绑定参数，再绑定函数根据绑定参数返回的函数结果
class decoratorWithArguments(object):
    def __init__(self, arg1, arg2, arg3):
        """
         If there are decorator arguments, the function
         to be decorated is not passed to the constructor!
         """
        print("Inside __init__()")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    # 当参数bind后，再bind 函数
    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print("__Inside __call__()")
        def wrapped_f(*args):
            print("Decorator arguments:", self.arg1, self.arg2, self.arg3)
            f(*args)

        return wrapped_f

# 先将"hello", 'world', 42
# 将sayHello函数传给 decoratorWithArguments, 然后返回sayHello 函数decorator,
# 最后当再调用 sayHello就调用 decoratorWithArguments.__call__
@decoratorWithArguments('hello', 'world', 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)

sayHello('say', 'hello', 'list', 'test')
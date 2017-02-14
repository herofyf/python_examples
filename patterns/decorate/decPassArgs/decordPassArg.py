# http://thecodeship.com/patterns/guide-to-python-function-decorators/

def tags(tag_name):
    def tags_decorator(func):
        # define innter wrapper
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))

        # return innter wrapper for tags decorator
        return func_wrapper

    return tags_decorator

# decorate with parameter 分两个层次，先绑定参数，再通过绑定参数的函数返回的函数再绑定目标函数
#
@tags('p')
def get_text(name):
    return "Hello" + name

print(get_text("John "))

print(get_text.__name__)
print(get_text.__doc__)
print(get_text.__module__)



#  函数调用就是不断压栈出栈

def p_decorate(func):
    def func_wrapper(name):
        return "<p> {0} </p>".format(func(name))

    return func_wrapper


def string_decorate(func):
    def func_wrapper(name):
        return "<strong> {0} </strong>".format(func(name))

    return func_wrapper


def div_decorate(func):
    def func_wrapper(name):
        return "<div> {0} </div>".format(func(name))

    return func_wrapper


# get_text = div_decorate(p_decorate(strong_decorate(get_text)))

@div_decorate
@p_decorate
@string_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

print(get_text("Jon"))
# http://thecodeship.com/patterns/guide-to-python-function-decorators/


def p_decorate(func):

    # inner function can call outter var
    def func_wrapper(name):
        return "<p> {0} </p>".format(func(name))

    return func_wrapper

# get_text = p_decorate(get_text)
@p_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)


print(get_text('john'))
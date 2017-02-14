__author__ = 'Land'

def myx(**kargs):
    for x in kargs.iteritems():
        print(x[1])


myx(a=1, b=2)

myxdict = {'a': 1, 'c':2}
myx(**myxdict)
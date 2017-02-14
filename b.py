__author__ = 'Land'


class C(object):
    def __init__(self):
        self._x = None

    @property
    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    def __iter__(self):
        self.count = 10;
        print("iter")
        return self

    def internalnext(self):
        if (self.count <= 0):
            raise  StopIteration
        else:
            self.count -=1
        print("next")
        return self.count

    # for python 2
    def next(self):
        self.internalnext()

    def __next__(self):
        self.internalnext()


c = C()
for item in c:
    print(item)

Cat = type("Cat", (object,), dict())
cat = Cat()

setattr(cat, "weight", 10)
val = getattr(cat, "weight")
print(val)

if not hasattr(cat, "name"):
    print("no name property")
else:
    print("no name property")

